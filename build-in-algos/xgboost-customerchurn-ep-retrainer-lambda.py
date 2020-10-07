import json
import boto3
import os
import datetime

sm = boto3.client('sagemaker')

def lambda_handler(event, context):

    endpoint_name = os.environ['ENDPOINT_NAME']
    model_role = os.environ['MODEL_ROLE'];
    source_training_job_name = os.environ['SOURCE_TRAINING_JOB_NAME'];
    job = sm.describe_training_job(TrainingJobName=source_training_job_name)
    container = "683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:1.0-1-cpu-py3";

    print("Job found:");
    print(job);

    prefix = os.environ['PREFIX']
    timesufix = str(datetime.datetime.today()).replace(' ', '-').replace(':', '-').rsplit('.')[0];
    training_job_name = prefix+timesufix + "-job";

    print("Starting training job %s" % training_job_name)

    job['AlgorithmSpecification'].pop('MetricDefinitions',None)

    resp = sm.create_training_job(
        TrainingJobName=training_job_name,
        AlgorithmSpecification=job['AlgorithmSpecification'],
        RoleArn=job['RoleArn'],
        InputDataConfig=job['InputDataConfig'],
        OutputDataConfig=job['OutputDataConfig'],
        ResourceConfig=job['ResourceConfig'],
        StoppingCondition=job['StoppingCondition'],
        HyperParameters=job['HyperParameters'] if 'HyperParameters' in job else {},
        Tags=job['Tags'] if 'Tags' in job else []
    )

    #Waiting for job to finish training
    sm.get_waiter('training_job_completed_or_stopped').wait(TrainingJobName = training_job_name);

    new_job = sm.describe_training_job(TrainingJobName=source_training_job_name)

    #Creating Model
    model_data = new_job['ModelArtifacts']['S3ModelArtifacts']
    primary_container = {
        'Image': container,
        'ModelDataUrl': model_data
    }
    model_name = prefix + timesufix + "-model";
    model_arn = sm.create_model(
        ModelName = model_name,
        ExecutionRoleArn = model_role,
        PrimaryContainer = primary_container
    )

    #Creating Endpoint Configuration
    epc_name = prefix + timesufix + "-epc"
    ep_config = sm.create_endpoint_config(EndpointConfigName = epc_name, ProductionVariants=[{'InstanceType': 'ml.m5.large', 'InitialInstanceCount': 1, 'ModelName': model_name,'VariantName': 'main'}])

    #Updating Endpoint
    sm.update_endpoint( EndpointName=endpoint_name, EndpointConfigName=epc_name)


    print(resp)

    return "OK"
