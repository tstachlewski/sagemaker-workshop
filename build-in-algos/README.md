
## Instrukcje

1. Upewnij się, że jesteś w regionie Irlandia
2. Przejdź następnie do usługi SageMaker a później do SageMaker Studio.
3. Utwórz nową konfigurację - podaj swoje imię oraz utwórz nową role dającą wszelki dostęp do S3.
4. Utworzenie instancji SageMaker Studio może potrwać kilka minut. Po kilku minutach w tabelce pojawi się nowo utworzony użytkownik oraz opcja "Open Studio" - którą należy wybrać.
5. Skopiuj (przeciągnij) do swojego notebook-a plik "xgboost_customer_churn.ipynb".
6. Utwórz notebook a następnie ustaw Kernel "Data Scence"
7. W pierwszym kroku 'skryptowym' jest linijka gdzie musisz podać nazwę bucketu, który zostanie utworzony i w którym będą przechowywane dane. Zaktualizuj jego nazwę (pamiętaj, że musi być unikatowa). Przykładowa nazwa: "workshop-tomek-customerchurn"
8. W innym oknie przeglądarki, przejdź do usługi S3 i upewnij się, że bucket S3 został utworzony i jest pusty.
9. Wykonaj kolejne 2 kroki skryptu. Przy drugim zostanie zwrócony bład. Zrestartuj kernel.
10. Wykonuj kolejne kroki aż dojdziesz do kroku pobierania danych. Będziesz musiał tutaj na chwilę przełączyć się na kernel "Basic"
11. Wróć do poprzedniego Kernela i sesji.
12. Wykonaj wszystkie kroki skryptu aż do kroku kopiujacego dane do S3. Zweryfikuj dane w S3.
13. Wykonaj kolejne kroki skryptu (nauki i hostowania)
14. W trakcie nauki, zweryfikuj konsolę SageMaker-a i zobacz, że nowy job nauki pokajwił się w zakładce 'Training jobs'
15. Kolejnym krokiem będzie wystawienie wdrożonego modelu jako usługi REST-owej.
16. Przejdź do usługi IAM i utwórz rolę IAM dającą odpowiednie dostępy.
17. Przejdź do usługi Lambda i utwórz nową funkcję. Nazwij ją "ChustomerChurnInvoker", środowisko Python. Wybierz rolę, utworzoną w poprzednim punkcie.
18. Wprowadź kod z pliku "xgboost-customerchurn-ep-invoker-lambda.py".
19. Ustaw nową zmienną środowiskową o nazwie "ENDPOINT_NAME" z wartością twojego endpointa SageMakerowego.
20. W pliku "xgboost-customerchurn-ep-invoker-lambda-testinput.txt" masz przykładową wartość wywołania funkcji. Przetestuj ją.
21. Dodaj Trigger APIGAteway do swojej funkcji.
- HTTP API
- Security Open
- Cross-origin resource sharing (CORS)
22. Utwórz nowy bucket S3 w ramach, którego wdrożymy testową stronę WWW.
23. Ustaw możliwość tworzenia publicznych obiektów w tym buckecie.
24. Zaktualizuj plik "xgboost-customerchurn-website.html" poprzez podanie swojego adresu http api gateway.
25. Wrzuć plik do S3.
26. Upublicznij plik.
27. W konfiguracji bucketu S3 ustaw możliwość hostowania statycznych stron WWW.
28. Przetestuj czy strona działa.
