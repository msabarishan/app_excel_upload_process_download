
Streamlit App for Machine planning using Python.

Applink:https://share.streamlit.io/msabarishan/uploading_excel_file/main/import_excel.py

Assume you are having three machines (m1,m2,m3) and each machine is available say 1440 mins in a day.

'N' no of materials need to be machined in these machines in a day.

Machining time will vary based on the machine and material (Eg: Material A may take 50 mins in machine m1, 
60 mins in machine m2, 50 mins in machine m3. SimilarlyMaterial B may take 80 mins in machine m1,20 mins in machine m2, 90 mins in machine m3 and so on. 

A material may run in all three machines with priority level based on some factors (Eg: For Material A, 1st priority is 
given to machine 3, 2nd priority to machine 1 and third priority to machine 2.Similarly or Material A, 1st priority is 
given to machine 2, 2nd priority to machine 1 and third priority to machine 3 and so on).Allocation need to be done based on priority level.
If available time in 1 st priority machine is exhaused then material need to allocated to 2 nd priority machine and so on.

Additionally these machine may available in different manufacturing locations with different available time.

Required solution is to create a plan by allocating materials to the machines m1,m2,m3 based on the location, machine available time,
priority and machining time for each material.

Guide for using the App:
1. Download Sample files. (For providing input data)
2. Update the sample file with new data in the same format.
3. Upload the file into the app.
4. Machine Plan will be displayed as well it can be downloaded and the last column shows the machine name to which the material is allocated (Eg:ma3- Machine 3)

Sample File Format (Description):
File 1: mc_avail - ma1: machine 1 total available time in respective location mentioned in column A,
ma2: machine 2 total available time in respective location mentioned in column A and so on.
File 2: mc_prior - m1: machining time in machine 1 for respective material (Column B) and location (Column A), m2: machining time in machine 2 for respective material and 
location and so on, m1p: Machine 1 Priority level for respective material (Column B) and location (Column A), m2p: Machine 2 Priority level for respective material and 
location and so on

