import pandas as pd
import streamlit as st
import codes as code
import texts as texts


# Wyświetlenie danych
def main():
    st.title("Zadanie 4 ")
    st.subheader("dodanie kolumny zawierającej sumę qty każdego produktu za poprzednie 7 dni")
    st.code(body = code.zad4_sql , language='SQL')
    

if __name__ == "__main__":
    main()
