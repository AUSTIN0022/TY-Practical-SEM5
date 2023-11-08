#B) Write a Python program to view basic statistical details of the data.(Use wineequality-red.csv)
import pandas as pd

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\winequality-red.csv")

print("Statistical Details:")
print(df.describe())
