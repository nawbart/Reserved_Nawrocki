# imports
import pandas as pd
import streamlit as st
import texts as text 

# const
path = "/home/nawbart/repos/Data_Science/reserved/data/zadanie_rekrutacyjne.csv"
path = "/home/nawbart/repos/Data_Science/reserved/data/taxi_dane.xlsx"

st.set_page_config(page_title="Zadanie 1",
                   page_icon=':one:')

st.write("# Witam w moich wizualizacjach 👋")
st.write(text.home_text)

st.sidebar.success("Wybierz zadanie powyżej")

st.balloons()