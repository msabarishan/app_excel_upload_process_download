import streamlit as st
import pandas as pd

st.write("""
# Machine_Utilization_Calculation
""")

dataUploaded=st.file_uploader("fileUploader")

try:
        df=pd.read_csv(dataUploaded, error_bad_lines=True, warn_bad_lines=False,sep=chosenFileSeparator)
except:
        try:
              df = pd.read_excel(dataUploaded)
        except:      
              df=pd.DataFrame()
                
st.dataframe(df)



