import pandas as pd

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\winequality-red.csv")

print('Description of the dataset:')
print(df.describe())
print('\nShape of the dataset:', df.shape)
print('\nFirst 3 rows from the dataset:')
print(df.head(3))
