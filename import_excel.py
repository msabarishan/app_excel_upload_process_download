import streamlit as st
import pandas as pd

st.write("""
# Machine_Utilization_Calculation
""")

uploaded_file = st.file_uploader("Choose a file")

df=pd.read_csv(uploaded_file)
        
                




