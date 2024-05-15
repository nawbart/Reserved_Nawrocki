import pandas as pd
import streamlit as st
import codes as code
import texts as texts

# Wyświetlenie danych
def main():
    st.title("Zadanie 2 - naprawa kodu SQL")
    st.code(body=code.zad3_sql, language='SQL')
    st.write(texts.poprawa_sq1)
    
if __name__ == "__main__":
    main()
