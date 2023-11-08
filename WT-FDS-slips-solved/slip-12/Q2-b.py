# Q.2 B) Write a Python program to create data frame containing column name, salary, department 
# add 10 rows with some missing and duplicate values to the data frame. Also drop all null and 
# empty values. Print the modified data frame

import pandas as pd

df = pd.DataFrame(columns = ['name','salary','department'])

df.loc[0] = ['jitu',85000,'Biology']
df.loc[1] = ['Austin',95000,'computer']
df.loc[2] = [None,65000,'commerce']
df.loc[3] = ['saquib',77000,'Blockchain']
df.loc[4] = ['Naufil',80000,'Electronices']
df.loc[5] = [None,65000,'science']
df.loc[6] = ['Kunal',65000,'agriculture']
df.loc[7] = ['Tanishq',77000,'Networks']
df.loc[8] = ['Arpita',65000,'Math']
df.loc[9] = ['vaishavi',85000,'computer']
print("Original Data Frame")
print(df)
df = df.dropna()
print("Modified Data Frame")
print(df)
