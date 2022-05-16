import streamlit as st
import pandas as pd

st.write("""
# Machine_Utilization_Calculation
""")

dataUploaded=st.file_uploader("fileUploader")

try:
        df=pd.read_csv(dataUploaded)
except:
        try:
              df = pd.read_excel(dataUploaded)
        except:      
              df=pd.DataFrame()
                
st.dataframe(df)



