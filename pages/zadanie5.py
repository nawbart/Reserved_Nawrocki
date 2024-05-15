import pandas as pd
from pathlib import Path
import streamlit as st
import io
import codes as codes


path = '/home/nawbart/repos/Nawrocki_Reserved/data/zadanie_rekrutacyjne.csv'


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


def find_customers_changed_source(data_frame):
    # Zapytanie: Klienci, którzy zmienili źródło transakcji między pierwszą a drugą transakcją
    data_frame['date'] = pd.to_datetime(data_frame['date'])
    data_frame.sort_values(by=['customer_id', 'date'], inplace=True)

    first_transaction_source = data_frame.groupby('customer_id')['source'].first().reset_index()
    second_transaction_source = data_frame.groupby('customer_id')['source'].nth(1).reset_index()
    merged_sources = pd.merge(first_transaction_source, second_transaction_source, on='customer_id', suffixes=('_first', '_second'))
    customers_changed_source = merged_sources[merged_sources['source_first'] != merged_sources['source_second']]

    return customers_changed_source[['customer_id', 'source_first', 'source_second']]


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



# Wyświetlenie danych
def main():
    st.markdown("<h1 style='text-align: center; color: purple;'>Rozwiązanie zostało otrzymane przy pomocy Pythona3 oraz Pandasa.</h1>", unsafe_allow_html=True)
    # Wczytanie danych
    df = pd.read_csv(path)

    # podpunkt 1
    st.markdown("<h1 style= 'font-size: 20px; text-align: center; color: silver;'>Zostali pozyskani przez app (source dla pierwszej transakcji = app) </h1>", unsafe_allow_html=True)
    st.code(body=codes.zad5_1, language='python')
    acquired_by_app_result = find_customers_acquired_by_app_first_transaction(df)
    st.dataframe(acquired_by_app_result, use_container_width=True)

    # podpunkt 2
    st.markdown("<h1 style= 'font-size: 20px; text-align: center; color: silver;'>Drugą transakcję dokonali za pomocą innego source niż pierwszą transakcję</h1>", unsafe_allow_html=True)
    st.code(body=codes.zad5_2, language='python')
    changed_source_result = find_customers_changed_source(df)
    st.dataframe(changed_source_result, use_container_width=True)

    # podpunkt 3
    st.markdown("<h1 style= 'font-size: 20px; text-align: center; color: silver;'>W swojej historii mają co najmniej dwie transakcje następujące po sobie, które zrealizowane zostały za pomocą tego samego source (np dla 4 i 5 zamówienia source = web) </h1>", unsafe_allow_html=True)
    st.code(body=codes.zad5_3, language='python')
    consecutive_transactions_result = find_customers_with_consecutive_transactions(df)
    st.dataframe(consecutive_transactions_result, use_container_width=True)

if __name__ == "__main__":
    main()
