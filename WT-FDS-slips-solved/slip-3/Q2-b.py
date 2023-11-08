#Q.2 B) Write a Python program to view basic statistical details of the data (Use Heights and Weights Dataset) 
import pandas as pd

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\SOCR-HeightWeight.csv")

print("Statistical Detail:")
print(df.describe())
