import streamlit as st
import pandas as pd

st.write("""
# Machine_Utilization_Calculation
""")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
        try:
                df1=pd.read_csv(uploaded_file)
        except:
                try:
                      df1=pd.read_excel(uploaded_file)
                except:      
                      df1=pd.DataFrame()
                
st.dataframe(df1)



