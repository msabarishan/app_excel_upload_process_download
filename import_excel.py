import streamlit as st
import pandas as pd

st.write("""
# Machine_Utilization_Calculation
""")

uploadedFile = st.file_uploader(fileUploadLabel, type=['csv','xlsx'],accept_multiple_files=False,key="fileUploader")

try:
        df=pd.read_csv(dataUploaded, error_bad_lines=True, warn_bad_lines=False,sep=chosenFileSeparator)
  except:
        try:
              df = pd.read_excel(dataUploaded)
        except:      
              df=pd.DataFrame()
                
st.dataframe(df)



