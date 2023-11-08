"""
Q.2) Write a Python program [15] 
1. To create a dataframe containing columns name, age and percentage. Add 10 rows to the dataframe. View the dataframe. 
2. To print the shape, number of rows-columns, data types, feature names and the description of the data 
3. To view basic statistical details of the data
4. To Add 5 rows with duplicate values and missing values. Add a column remarks with empty values. Display the data. 
"""
import pandas as pd

df = pd.DataFrame(columns = ['name','age','Per'])
# Q1
df.loc[0] = ['jitu',3,85000]
df.loc[1] = ['Austin',19,95000]
df.loc[2] = [None,20,77000]
df.loc[3] = ['Naufil',30,80000]
df.loc[4] = [None,21,65000]
df.loc[5] = ['Tanishq',18,77000]
df.loc[6] = ['Arpita',17,65000]
df.loc[7] = ['vaishavi',19,85000]
print(df)

# Q2
print('\nShape of the DataFrame:', df.shape)
print('\nrows & columns in the DataFrame:', df.shape[0], 'rows,', df.shape[1], 'columns')
print('\nData types of the DataFrame:')
print(df.dtypes)
print('\nFeature of the DataFrame:')
print(df.columns)
# Q3
print('\nDescription of the DataFrame:')
print(df.describe())

# Q4
df['remarks'] = None

print(df)
