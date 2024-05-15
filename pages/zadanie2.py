import streamlit as st
import codes as code
import texts as texts


# Funkcja główna do wyświetlenia danych
def main():
    # Wyświetlenie tytułu
    st.markdown("<h1 style='font-size: 30px; text-align: center; color: silver;'>Dodanie kolumny z poprzednią liczbą qty(quantity - ilość produktów) dla wcześniejszego zamówienia danego klienta </h1>", unsafe_allow_html=True)
    
    # Wyświetlenie kodu SQL
    st.code(body=code.zad2_sql, language='SQL')


if __name__ == "__main__":
    main()
