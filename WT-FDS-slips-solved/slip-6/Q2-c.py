#Q.2 C) Download the heights and weights dataset and load the dataset froma given csv file into a 
#dataframe. Print the first, last 10 rows and random 20 rows also display shape of the  dataset. 
import random

import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\SOCR-HeightWeight.csv")

# 1. Print the first row
print("First row:")
print(df.head(10))

# 2. Print the last 10 rows
print("\nLast 10 rows:")
print(df.tail(10))

# 3. Print random 20 rows
print("\nRandom 20 rows:")
print(df.sample(20))

print("Shape of dataframe: ",df.shape)
