import streamlit as st
import pandas as pd
import numpy as np
st.write("""
# Machine Allocation
""")
mp1= st.file_uploader("Choose a Machine Priority XLSX file", type="xlsx")
ma1= st.file_uploader("Choose a Machine Availability XLSX file", type="xlsx")

if mp1:
    mp = pd.read_excel(mp1)
if ma1:
    ma = pd.read_excel(ma1)
    
ndf = pd.merge(mp,ma,on ='location',how ='inner')

n_p=ndf['location'].count()
j=1
mac_data={}
start='maf'
mac_data1=[start]
d=1000
    

for i in range(n_p):
        
        if(d!=ndf.iloc[j-1,0]):
            a=ndf.iloc[j-1,8]
            b=ndf.iloc[j-1,9]
            c=ndf.iloc[j-1,10]
            d=ndf.iloc[j-1,0]
    
            
        if (ndf.iloc[j-1,5]==1.0)and(ndf.iloc[j-1,2]<=a):
            mac_data='ma1'
            a=a-ndf.iloc[j-1,2]
        
        elif (ndf.iloc[j-1,6]==1.0)and(ndf.iloc[j-1,3]<=b):
            mac_data='ma2'
            b=b-ndf.iloc[j-1,3]
        
        elif (ndf.iloc[j-1,7]==1.0)and(ndf.iloc[j-1,4]<=c):
            mac_data='ma3'
            c=c-ndf.iloc[j-1,4]
    # Above condtion to check first machine
        elif (ndf.iloc[j-1,5]==1.0)and(ndf.iloc[j-1,2]>a)and(ndf.iloc[j-1,3]<=b)and(ndf.iloc[j-1,6]==2.0):
            mac_data='ma2'
            b=b-ndf.iloc[j-1,3]
        elif (ndf.iloc[j-1,6]==1.0)and(ndf.iloc[j-1,2]>a)and(ndf.iloc[j-1,4]<=c)and(ndf.iloc[j-1,7]==2.0):
            mac_data='ma3'
            c=c-ndf.iloc[j-1,4]
        
        elif (ndf.iloc[j-1,6]==1.0)and(ndf.iloc[j-1,3]>b)and(ndf.iloc[j-1,2]<=a)and(ndf.iloc[j-1,5]==2.0):
            mac_data='ma1'
            a=a-ndf.iloc[j-1,2]
        elif (ndf.iloc[j-1,6]==1.0)and(ndf.iloc[j-1,3]>b)and(ndf.iloc[j-1,4]<=c)and(ndf.iloc[j-1,7]==2.0):
            mac_data='ma3'
            c=c-ndf.iloc[j-1,4]
        
        elif (ndf.iloc[j-1,7]==1.0)and(ndf.iloc[j-1,4]>c)and(ndf.iloc[j-1,2]<=a)and(ndf.iloc[j-1,5]==2.0):
            mac_data='ma1'
            a=a-ndf.iloc[j-1,2]
        elif (ndf.iloc[j-1,7]==1.0)and(ndf.iloc[j-1,4]>c)and(ndf.iloc[j-1,3]<=b)and(ndf.iloc[j-1,6]==2.0):
            mac_data='ma2'
            b=b-ndf.iloc[j-1,3]
    # Above condition to check second machine
        elif (ndf.iloc[j-1,5]==3.0)and(ndf.iloc[j-1,2]<=a):
            mac_data='ma1'
            a=a-ndf.iloc[j-1,2]
        
        elif (ndf.iloc[j-1,6]==3.0)and(ndf.iloc[j-1,3]<=b):
            mac_data='ma2'
            b=b-ndf.iloc[j-1,3]
        
        elif (ndf.iloc[j-1,7]==3.0)and(ndf.iloc[j-1,4]<=c):
            mac_data='ma3'
            c=c-ndf.iloc[j-1,4]
    # Above condition to check third machine
        
        else:
            mac_data='nm'
        mac_data1.append(mac_data)
        j=j+1
mac_data1.remove("maf")
ndf['Machine_allocated']=pd.DataFrame(mac_data1)

st.table(ndf)

