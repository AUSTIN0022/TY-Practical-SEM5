# Q.2 B) Write a Python program to print the shape, number of rows-columns, data types, 
# feature names and the description of the data(Use Data.csv) 

import pandas as pd

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\Data.csv")

print('Shape of the DataFrame:', df.shape)
print('Number of rows:', df.shape[0])
print('Number of columns:', df.shape[1])
print('Data types of each column:\n', df.dtypes)
print('Feature names:', list(df.columns))
print('Description of the DataFrame:\n', df.describe())
