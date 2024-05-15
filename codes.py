zad3_sql = """
–- Oryginał
SELECT customer_id,
AVG(revenue)
FROM x
WHERE AVG(revenue) > 75
GROUP BY customer_id

–- Poprawna wersja
SELECT
customer_id,
AVG(revenue) AS average_revenue
FROM
zadanie_rekrutacyjne
GROUP BY
customer_id
HAVING
AVG(revenue) > 75;
"""

zad4_sql = """
SELECT
product_id,
SUM(units) AS total_units_last_7_days
FROM
zadanie_rekrutacyjne
WHERE
date >= date('now', '-7 days')
GROUP BY
product_id;
"""

zad5_1 = """
def find_customers_acquired_by_app_first_transaction(data_frame):
    # Konwersja kolumny 'date' na typ datetime
    data_frame['date'] = pd.to_datetime(data_frame['date'])

    # Sortowanie danych po dacie transakcji
    data_frame.sort_values(by=['customer_id', 'date'], inplace=True)

    # Grupowanie po kliencie i wybieranie pierwszej wartości 'source' dla każdego klienta
    first_transaction_source = data_frame.groupby('customer_id')['source'].first().reset_index()

    # Filtrowanie klientów, którzy zostali pozyskani przez 'app' w pierwszej transakcji
    customers_acquired_by_app_first_transaction = first_transaction_source[first_transaction_source['source'] == 'app']

    return customers_acquired_by_app_first_transaction[['customer_id', 'source']]
"""

zad5_2 = """
def find_customers_changed_source(data_frame):
    # Zapytanie: Klienci, którzy zmienili źródło transakcji między pierwszą a drugą transakcją
    data_frame['date'] = pd.to_datetime(data_frame['date'])
    data_frame.sort_values(by=['customer_id', 'date'], inplace=True)

    first_transaction_source = data_frame.groupby('customer_id')['source'].first().reset_index()
    second_transaction_source = data_frame.groupby('customer_id')['source'].nth(1).reset_index()
    merged_sources = pd.merge(first_transaction_source, second_transaction_source, on='customer_id', suffixes=('_first', '_second'))
    customers_changed_source = merged_sources[merged_sources['source_first'] != merged_sources['source_second']]

    return customers_changed_source[['customer_id', 'source_first', 'source_second']]
"""

zad5_3 = """
def find_customers_with_consecutive_transactions(data_frame):
    # Zapytanie: Klienci, którzy mieli co najmniej dwie transakcje następujące po sobie z tym samym źródłem
    data_frame['date'] = pd.to_datetime(data_frame['date'])
    data_frame.sort_values(by=['customer_id', 'date'], inplace=True)

    data_frame['prev_source'] = data_frame.groupby('customer_id')['source'].shift(1)
    customers_with_consecutive_transactions = data_frame[
        (data_frame['source'] == data_frame['prev_source']) &
        (data_frame['customer_id'] == data_frame['customer_id'].shift(1))
    ]

    return customers_with_consecutive_transactions[['customer_id', 'prev_source', 'source']]
"""


zad2_sql = """
ALTER TABLE zadanie_rekrutacyjne
ADD COLUMN qty INTEGER;
UPDATE zadanie_rekrutacyjne
SET qty = (
SELECT LAG(units) OVER (PARTITION BY customer_id ORDER BY date)
FROM zadanie_rekrutacyjne AS sub
WHERE sub.customer_id = zadanie_rekrutacyjne.customer_id
AND sub.date < zadanie_rekrutacyjne.date
ORDER BY sub.date DESC
LIMIT 1
);
"""

zad1_py = """
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import io
from pathlib import Path
import texts as texts
import codes as code

# Constants
DATA_PATH = Path("/home/nawbart/repos/Data_Science/reserved/data/taxi_dane.xlsx")


# Funkcja do wyświetlania nagłówka aplikacji
def display_header():
    # Wyświetlenie głównego tytułu i krótkiego opisu analizy
    st.markdown(
        "<h1 style='font-size: 50px; text-align: center; color: purple;'>Analiza danych dotyczących podróży taksówką </h1>",
        unsafe_allow_html=True)
    st.markdown(
        "<h1 style='font-size: 30px; text-align: center; color: silver;'>Oto krótka analiza każdej kolumny:</h1>",
        unsafe_allow_html=True)
    st.write(texts.analiza_kazdej_kolumny)
    st.write('')

# Funkcja do wczytania danych z pliku Excel
def load_data():
    return pd.read_excel(DATA_PATH, nrows=100)

# Funkcja do wyświetlania statystyk numerycznych dla danych
def display_numeric_stats(df):
    # Wyświetlenie tytułu i ramki danych zawierającej opis statystyczny danych numerycznych
    st.markdown(
        "<h1 style='font-size: 30px; text-align: center; color: silver;'>Opis statystyczny danych liczbowych</h1>",
        unsafe_allow_html=True)
    st.write(df.describe())
    st.write(texts.opis_statystyczny)
    st.write(texts.analiza_danych_z_description)
    st.write('')


# Funkcja do wyświetlania informacji o danych
def display_data_info(df):
    # Wyświetlenie tytułu i informacji o danych
    st.markdown(
        "<h1 style='font-size: 30px; text-align: center; color: silver;'>Informacje na temat danych</h1>",
        unsafe_allow_html=True)
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
    st.write(texts.informacje_o_danych)
    st.write('')


# Funkcja do wyświetlania procentowego udziału brakujących wartości w kolumnach
def display_missing_values(df):
    st.subheader('Procentowy brak danych w kolumnach')
    per_null = df.isnull().mean() * 100
    st.dataframe(data=per_null, width=500, height=900, use_container_width=True)
    st.write('')

# Funkcja do wyświetlania korelacji między kolumnami numerycznymi
def display_correlations(df):
    st.title("Korelacje")
    korelacje = df.corr()
    st.dataframe(data=korelacje, use_container_width=True)
    st.write(texts.korelacje)
    st.write('')

# Funkcja do wyświetlania histogramu dla kolumny czasu podróży

def display_trip_seconds_histogram(df):
    st.title("Histogram czasu podróży")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df['trip_seconds'], bins=50, color='skyblue', edgecolor='black')
    ax.set_title('Histogram czasu podróży')
    ax.set_xlabel('Czas podróży (sekundy)')
    ax.set_ylabel('Liczba podróży w tysiącach')
    ax.grid(True)
    st.pyplot(fig)
    plt.close(fig)
    st.write('')


# Funkcja do wyświetlania wykresu punktowego odległości podróży od czasu podróży
def display_trip_distance_time_scatter(df):
    st.title("Zależność między odległością a czasem podróży")
    plt.scatter(df["trip_seconds"].dropna(), df["trip_miles"].dropna(), alpha=0.5, color='green')
    plt.xlabel('Czas podróży (s)')
    plt.ylabel('Odległość podróży (mile)')
    plt.title('Zależność między odległością a czasem podróży')
    plt.grid(True)
    st.pyplot()
    plt.close()
    st.write('')


# Funkcja do wyświetlania wykresu pudełkowego kosztów podróży
def display_trip_cost_boxplot(df):
    st.title("Rozkład kosztów podróży")
    plt.boxplot(df["trip_total"].dropna(), vert=False)
    plt.xlabel('Koszt podróży')
    plt.title('Rozkład kosztów podróży')
    plt.grid(True)
    st.pyplot()
    plt.close()


# Główna funkcja do uruchomienia aplikacji
def main():
    display_header()
    df = load_data()
    display_numeric_stats(df)
    display_data_info(df)
    display_missing_values(df)
    display_correlations(df)
    display_trip_seconds_histogram(df)
    display_trip_distance_time_scatter(df)
    display_trip_cost_boxplot(df)
    st.code(body=code.zad1_py, language='python')


st.set_option('deprecation.showPyplotGlobalUse', False)


if __name__ == "__main__":
    main()

"""