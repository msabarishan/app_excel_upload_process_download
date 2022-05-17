import streamlit as st
import pandas as pd
import numpy as np
st.write("""
# Machine Allocation
""")
mc_availability=pd.read_excel('mc_avail.xlsx')
mc_priority=pd.read_excel('mc_prior.xlsx')

df_mc_avail = mc_availability.reset_index(drop=True, inplace=True)
df_mc_prior = mc_priority.reset_index(drop=True, inplace=True)

st.table(mc_availability)
def convert_df(machine):
       return machine.to_csv().encode('utf-8')


mc_prior_csv = convert_df(df_mc_prior)
st.subheader('Click here to download sample files')
st.download_button(
      "Press to Download machine Priority file",
      mc_prior_csv,
      "mc-prior.csv",
      "text/csv",
      key='download-csv'
      )
mc_avail_csv = convert_df(df_mc_avail)
st.download_button(
      "Press to Download machine availability file",
      mc_avail_csv,
      "mc_avail.csv",
      "text/csv",
      key='download-csv'
      )
st.subheader('UPLOAD THE MACHINE PRIORITY AND MACHINE AVAILABILITY FILE BELOW IN CSV FORMAT')
mc_prior_ip= st.file_uploader("Choose a Machine Priority CSV file")
mc_avail_ip= st.file_uploader("Choose a Machine Availability CSV file")


try:
    if mc_prior_ip is not None:
           mp = pd.read_csv(mc_prior_ip) #mp-machine priority data frame
    if mc_avail_ip is not None:
           ma = pd.read_csv(mc_avail_ip) #ma-machine availabilty data frame

    
    ndf = pd.merge(mp,ma,on ='location',how ='inner') #ndf-merged data frame

    n_p=ndf['location'].count() #Counting no of location
    j=1
    mac_data={} #mac_data new dictionary
    start='maf' 
    mac_data1=[start] 
    d=1000 #initialize location value to 1000
    

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
    st.subheader('Export Plan in CSV format')

    def convert_df(ndf):
       return ndf.to_csv().encode('utf-8')


    csv = convert_df(ndf)

    st.download_button(
      "Press to Download",
      csv,
      "file.csv",
      "text/csv",
      key='download-csv'
      )
    st.subheader('Machine Plan')
    st.table(ndf)
    st.write('m1- Time taken by Material for machinining in machine1,m1p-Machine 1 Priority level,ma1-machine available time for the particular location,ma1-machine1')
except:
    pass

