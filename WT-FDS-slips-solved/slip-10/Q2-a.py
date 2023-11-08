#Q.2 A) Write a python program to Display column-wise mean, and median for SOCR HeightWeight dataset.
import pandas as pd

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\SOCR-HeightWeight.csv")

print("Column-Wise Mean:")
print(df.mean())
print("\nColumn-Wise Median:")
print(df.median())
