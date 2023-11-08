"""Q.2) Dataset Name: winequality-red.csv Write a program in python to perform following tasks 
a. Rescaling: Normalised the dataset using MinMaxScaler class 
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\winequality-red.csv")

print('\n\n Data Scaled between 0 to 1')
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(df)
print(scaled.round(2))
