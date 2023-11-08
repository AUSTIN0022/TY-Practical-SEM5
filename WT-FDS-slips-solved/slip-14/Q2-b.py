 # Q. 2 B) Write a Python program to view basic statistical details of the data (Use advertising.csv)
import pandas as pd

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\Advertising.csv")

print('Description of the dataset:')
print(df.describe())
