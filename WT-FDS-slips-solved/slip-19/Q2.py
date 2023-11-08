"""
Q.2) Write a Python program [15] 
1. To create a dataframe containing columns name, age and percentage. Add 10 rows to the dataframe. View the dataframe. 
2. To print the shape, number of rows-columns, data types, feature names and the description of the data 
3. To Add 5 rows with duplicate values and missing values. Add a column remarks with empty values. Display the data. 
"""
import pandas as pd

df = pd.DataFrame(columns = ['name','age','Per'])
# Q1
df.loc[0] = ['jitu',3,85]
df.loc[1] = ['Austin',19,95]
df.loc[2] = [None,20,77]
df.loc[3] = ['Naufil',30,80]
df.loc[4] = [None,21,650]
df.loc[5] = ['Tanishq',18,77]
df.loc[6] = ['Arpita',17,65]
df.loc[7] = ['vaishavi',19,85]
print(df)
# Q2
print('\nShape:', df.shape)
print('\nrows & columns:', df.shape[0], 'rows,', df.shape[1], 'columns')
print('\nData types:\n',df.dtypes)
print('\nFeature:\n',df.columns)
print('\nDescription:\n',df.describe())
# Q3
df['remarks'] = None
print(df)
