
## Instrukcje

1. Upewnij się, że jesteś w regionie Irlandia
2. Przejdź następnie do usługi SageMaker a później do SageMaker Studio.
3. Utwórz nową konfigurację - podaj swoje imię oraz utwórz nową role dającą wszelki dostęp do S3.
4. Utworzenie instancji SageMaker Studio może potrwać kilka minut. Po kilku minutach w tabelce pojawi się nowo utworzony użytkownik oraz opcja "Open Studio" - którą należy wybrać.
5. Skopiuj (przeciągnij) do swojego notebook-a plik "autopilot_customer_churn.ipynb".
6. Utwórz notebook a następnie ustaw Kernel "Data Scence"
7. W pierwszym kroku 'skryptowym' jest linijka gdzie musisz podać nazwę bucketu, który zostanie utworzony i w którym będą przechowywane dane. Zaktualizuj jego nazwę (pamiętaj, że musi być unikatowa). Przykładowa nazwa: "workshop-tomek-customerchurn-auto[ilot]"
8. W innym oknie przeglądarki, przejdź do usługi S3 i upewnij się, że bucket S3 został utworzony i jest pusty.
9. Wykonaj wszystkie kroki skryptu aż do kroku kopiujacego dane do S3. Zweryfikuj dane w S3.
10. Wykonaj kolejne kroki skryptu (nauki i hostowania)
11. W trakcie nauki, zweryfikuj konsolę SageMaker-a i zobacz, że nowe joby nauki pojawiły się w zakładce 'Training jobs'. Całość może zająć nawet do 20 minut.
12. Kolejnym krokiem będzie wystawienie wdrożonego modelu jako usługi REST-owej.
13. Przejdź do usługi IAM i utwórz rolę IAM dającą odpowiednie dostępy.
14. Przejdź do usługi Lambda i utwórz nową funkcję. Nazwij ją "AutoChustomerChurnInvoker", środowisko Python. Wybierz rolę, utworzoną w poprzednim punkcie.
15. Wprowadź kod z pliku "autopilot-customerchurn-ep-invoker-lambda.py".
19. Ustaw nową zmienną środowiskową o nazwie "ENDPOINT_NAME" z wartością twojego endpointa SageMakerowego.
20. W pliku "autopilot-customerchurn-ep-invoker-lambda-input-test.txt" masz przykładową wartość wywołania funkcji. Przetestuj ją.
21. Dodaj Trigger APIGAteway do swojej funkcji.
- HTTP API
- Security Open
- Cross-origin resource sharing (CORS)
22. Utwórz nowy bucket S3 w ramach, którego wdrożymy testową stronę WWW.
23. Ustaw możliwość tworzenia publicznych obiektów w tym buckecie.
24. Zaktualizuj plik "autopilot-customerchurn-website.html" poprzez podanie swojego adresu http api gateway.
25. Wrzuć plik do S3.
26. Upublicznij plik.
27. W konfiguracji bucketu S3 ustaw możliwość hostowania statycznych stron WWW.
28. Przetestuj czy strona działa.
29. PROCES "retrenowania" zostanie opisany przez prowadzącego.
