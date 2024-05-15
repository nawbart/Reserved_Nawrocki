home_text = """
Aplikacja opiera się na języku python3 z wykorzystaniem takich biblitek jak: streamlit, pandas, matplotlib, io itp. oraz z kodu HTML.
Niestety poświęciłem na torzenie tego rozwiązania dużo mniej czasu nie zaplanowałem z powodów pywatnych, dlatego chciałbym
napisać co jeszcze planowałem dodać do mojego raportu:
- interaktywne narzędzia pozwalające na maanipulowanie i filtrowanie danych.
- opis wykresów w zadaniu 1
- Analiza data science na podstawie danych z wykorzystaniem min. Scikit-learn
- w projekcie nie została zrealizowana najoptymalniejsza sturktura, natomiast wszystko działa i pozwoliło mi to zaoszczędzić trochę czasu.

Jestem świadom, że projekt nie jest wizualnie dopracowany, tzn. wycentrowanie tekstów oraz dataframe'ów nie jest idealne, ale myśle,
że nie to jest ważne w takich zadaniach.
"""


analiza_kazdej_kolumny = """
1. unique_key: Wygląda na to, że jest to unikalny klucz identyfikujący każdy rekord w zbiorze danych.

2. taxi_id: Unikalny identyfikator taksówki.

3. trip_start_timestamp, trip_end_timestamp: Czas rozpoczęcia i zakończenia podróży taksówką.

4. trip_seconds, trip_miles: Czas i odległość podróży w sekundach i milach.

5. pickup_census_tract, dropoff_census_tract: Terytorium spisu powszechnego, z którego pochodzi pickup i dropoff.

6. pickup_community_area, dropoff_community_area: Obszary społeczności, w których znajdują się pickup i dropoff.

7. fare, tips, tolls, extras, trip_total: Koszty związane z podróżą, w tym opłata podstawowa, napiwki, opłaty drogowe, dodatkowe opłaty i łączny koszt podróży.

8. payment_type: Typ płatności.

9. company: Firma taksówkowa.

10. pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude: Szerokość i długość geograficzna punktu początkowego i końcowego podróży.

11. pickup_location, dropoff_location: Lokalizacja początkowa i końcowa podróży.

12. year, month: Rok i miesiąc podróży.

Dane te zawierają informacje na temat podróży taksówkowych, takie jak czas, odległość, koszty, lokalizacje i inne metadane. Przy odpowiedniej obróbce i analizie można z nich uzyskać różnorodne wnioski dotyczące ruchu ulicznego, preferencji klientów, tendencji sezonowych itp."""



opis_statystyczny= """Analiza danych może obejmować różne aspekty, w zależności od celów badawczych. Oto kilka potencjalnych analiz, które można przeprowadzić na podstawie tych danych:

1. Średnia długość i czas podróży: Sprawdzenie, jaka jest średnia długość casu przejazdu oraz jakie były średnie koszty podróży.

2. Rozkład kosztów podróży: Sprawdzenie rozkładu kosztów podróży, w tym opłaty podstawowej, napiwków, opłat drogowych i dodatkowych opłat.

3. Rozkład czasu podróży w ciągu dnia i roku: Sprawdzenie, jak rozkłada się czas podróży w ciągu dnia i roku, czy istnieją wzorce sezonowe.

4. Popularne obszary i firmy: Zidentyfikowanie najczęściej odwiedzanych obszarów i firm taksówkowych.

5. Typy płatności: Analiza różnych typów płatności i ich częstości.

6. Lokalizacje początkowe i końcowe: Sprawdzenie rozkładu lokalizacji początkowych i końcowych podróży, aby zidentyfikować najczęściej odwiedzane miejsca.

7. Porównanie lat i miesięcy: Analiza różnic w podróżach w różnych latach i miesiącach.

"""

informacje_o_danych = """
Przeglądając dane bardziej szczegółowo, możemy postawić kilka dodatkowych wniosków i rozważać dodatkowe kroki analizy:

1. Czas podróży:
Możemy zbadać rozkład czasu podróży (kolumna 'trip_seconds') i odległości podróży (kolumna 'trip_miles') oraz ich korelację. Czy są podróże o długim czasie, ale krótkiej odległości lub vice versa?
Sprawdźmy, czy istnieją podróże z nieprawdopodobnie krótkim lub długim czasem podróży. Czy takie przypadki mogą być wynikiem błędów w danych?

2. Koszty podróży:
Możemy zbadać rozkład kosztów podróży, w tym opłaty podstawowej, napiwków, opłat drogowych i dodatkowych opłat. Czy istnieją podróże z nieproporcjonalnie wysokimi kosztami?
Analizując kolumny związane z kosztami podróży, możemy zbadać średnie wartości, mediany oraz odchylenie standardowe i zidentyfikować potencjalne anomalie.

3. Typy płatności:
Sprawdźmy, jak często występują różne typy płatności i czy istnieją trendy zmian w preferowanych typach płatności w czasie.

4. Lokalizacje początkowe i końcowe:
Możemy wykorzystać dane dotyczące szerokości i długości geograficznej, aby zwizualizować rozkład lokalizacji początkowych i końcowych podróży na mapie. Czy istnieją obszary, które są szczególnie popularne lub rzadko odwiedzane?

5. Rok i miesiąc podróży:
Analizując dane w kontekście roku i miesiąca, możemy zbadać sezonowe trendy w podróżach taksówkowych. Czy występują różnice w częstości podróży między różnymi miesiącami lub latami?

6. Brakujące wartości:
Konieczne będzie zdecydowanie, jak postępować z brakującymi wartościami w danych. Czy możemy uzupełnić brakujące wartości na podstawie innych danych w zbiorze lub czy należy je usunąć?

7. Rozkłady i korelacje:
Przeprowadźmy analizę rozkładów poszczególnych cech oraz ich korelacji. Czy istnieją silne zależności między cechami?

8. Analiza anomalii:
Szukajmy potencjalnych anomalii lub nietypowych wzorców w danych, które mogą wskazywać na błędy lub interesujące przypadki.
Przed przystąpieniem do bardziej zaawansowanych analiz konieczne będzie odpowiednie przetwarzanie danych, w tym usuwanie lub uzupełnianie brakujących wartości, konwersja typów danych oraz ewentualne usuwanie lub korygowanie błędów w danych."""

analiza_danych_z_description = """Analizując wyniki funkcji describe(), możemy:
Zidentyfikować potencjalne anomalie lub wartości odstające w danych.
Zrozumieć zakres wartości w poszczególnych kolumnach.
Ocenić, czy dane są skoncentrowane wokół średniej czy rozproszone.
Zobaczyć, czy są ewentualne problemy z rozkładem danych (np. duża różnica między
średnią a medianą).

*Wartość średnia trip_seconds wynosi około 897 sekund, z odchyleniem standardowym 1760
sekund, co sugeruje, że dane są mocno rozproszone.\n
*Minimalna liczba sekund w podróży wynosi 0, co może wymagać dalszej analizy.\n
*Wartość 75% kolumny trip_miles wynosi 4.73, co oznacza, że 75% podróży miało długość do
4.73 mil, a wartość maksymalna to 529.3, co może sugerować obecność wartości
odstających.

"""


korelacje = """Współczynniki korelacji:
trip_seconds i trip_miles mają współczynnik korelacji wynoszący około 0.297. Jest to
dodatnia korelacja, co może sugerować, że dłuższe podróże są zazwyczaj związane z
większym przebytym dystansem.\n
trip_seconds i tips mają współczynnik korelacji wynoszący około 0.12. To również
dodatnia korelacja, co sugeruje, że dłuższe podróże mogą być związane z wyższymi
napiwkami.\n
trip_seconds i fare mają współczynnik korelacji wynoszący około 0.1. Jest to ponownie
dodatnia korelacja, co sugeruje, że dłuższe podróże mogą być związane z wyższymi
opłatami.\n

Interpretacja:
Współczynniki korelacji pozwalają zrozumieć, czy i jak dwie zmienne są ze sobą
powiązane. Współczynniki korelacji Pearsona w zakresie od -1 do 1, gdzie 1 oznacza silną
dodatnią korelację, -1 oznacza silną ujemną korelację, a 0 oznacza brak korelacji.\n
Wartości bliskie 1 wskazują na silną dodatnią korelację, co oznacza, że zmienne rosną
razem. Wartości bliskie -1 wskazują na silną ujemną korelację, co oznacza, że zmienne
mają tendencję do maleć razem. Wartości bliskie 0 sugerują brak liniowej zależności.

Dalsza analiza:
Analizując współczynniki korelacji, można zidentyfikować relacje między różnymi
zmiennymi w danych. Na przykład, zidentyfikowano, że czas podróży (trip_seconds) jest
pozytywnie skorelowany z przebytym dystansem (trip_miles), co jest zgodne z intuicją.\n
Korelacje te mogą również pomóc w zrozumieniu, które zmienne są ze sobą najbardziej
związane, co może być istotne w kontekście dalszej analizy danych.
"""

poprawa_sq1 = """
W oryginalnym zapytaniu:

1. Brakujący alias: W kolumnie AVG(revenue) nie został nadany alias, co sprawia, że kolumna w wynikowym zestawie danych nie ma czytelnego nazewnictwa.
2. Błędna tabela w FROM: Zamiast konkretnej tabeli, występuje "x", co nie wskazuje na żadną konkretną tabelę, co prowadziłoby do błędu.
3. Brak klauzuli HAVING: Chociaż warunek WHERE jest prawidłowy, w przypadku agregatów należy używać klauzuli HAVING zamiast WHERE.\n

Poprawione zapytanie:

1. Dodanie aliasu: AVG(revenue) zostało nazwane jako average_revenue, co sprawia, że kolumna w wynikowym zestawie danych jest bardziej czytelna.
2. Użycie prawidłowej tabeli: Zamiast "x" użyto prawidłowej tabeli zadanie_rekrutacyjne.
3. Użycie klauzuli HAVING: Warunek AVG(revenue) > 75 został przeniesiony do klauzuli HAVING, co jest poprawną praktyką dla warunków dotyczących agregatów.
W wyniku tych zmian zapytanie jest bardziej czytelne, łatwiejsze do zrozumienia i bardziej odporna na błędy.
"""