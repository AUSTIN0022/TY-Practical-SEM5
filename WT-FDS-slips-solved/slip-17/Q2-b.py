#Q.2 B) Write a Python program to create a data frame containing columns name, age , salary, department
# Add 10 rows to the data frame. View the data frame.

import pandas as pd

df = pd.DataFrame(columns = ['name','age','salary','department'])

df.loc[0] = ['jitu',16,85000,'Biology']
df.loc[1] = ['Austin',19,95000,'computer']
df.loc[2] = ['nyaz',17,65000,'commerce']
df.loc[3] = ['saquib',20,77000,'Blockchain']
df.loc[4] = ['Naufil',18,80000,'Electronices']
df.loc[5] = ['anjali',11,65000,'science']
df.loc[6] = ['Kunal',19,65000,'agriculture']
df.loc[7] = ['Tanishq',18,77000,'Networks']
df.loc[8] = ['Arpita',30,65000,'Math']
df.loc[9] = ['vaishavi',15,85000,'computer']

print(df)
