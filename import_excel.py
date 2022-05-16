import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.dataframe(df)
    st.table(df)
