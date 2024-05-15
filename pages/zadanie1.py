import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import io
from pathlib import Path
import texts as text
import codes as code

# Constants
# DATA_PATH = Path("/home/nawbart/repos/RESERVED/data/taxi_dane.xlsx")

# # Katalog, w którym znajduje się plik
DATA_DIR = Path.cwd() / "data"
# Nazwa pliku
DATA_FILENAME = "taxi_dane.xlsx"
# Pełna ścieżka do pliku
DATA_PATH = DATA_DIR / DATA_FILENAME

# Funkcja do wyświetlania nagłówka aplikacji
def display_header():
    # Wyświetlenie głównego tytułu i krótkiego opisu analizy
    st.markdown(
        "<h1 style='font-size: 50px; text-align: center; color: purple;'>Analiza danych dotyczących podróży taksówką </h1>",
        unsafe_allow_html=True)
    st.markdown(
        "<h1 style='font-size: 30px; text-align: center; color: silver;'>Oto krótka analiza każdej kolumny:</h1>",
        unsafe_allow_html=True)
    st.write(text.analiza_kazdej_kolumny)
    st.write('')

# Funkcja do wczytania danych z pliku Excel
def load_data():
    return pd.read_excel(DATA_PATH)

# Funkcja do wyświetlania statystyk numerycznych dla danych
def display_numeric_stats(df):
    # Wyświetlenie tytułu i ramki danych zawierającej opis statystyczny danych numerycznych
    st.markdown(
        "<h1 style='font-size: 30px; text-align: center; color: silver;'>Opis statystyczny danych liczbowych</h1>",
        unsafe_allow_html=True)
    st.write(df.describe())
    st.write(text.opis_statystyczny)
    st.write(text.analiza_danych_z_description)
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
    st.write(text.informacje_o_danych)
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
    st.write(text.korelacje)
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
