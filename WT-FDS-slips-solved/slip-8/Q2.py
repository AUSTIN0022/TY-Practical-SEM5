#Q.2) Write a program in python to perform following task :
#1. Import Dataset from above link. 
#2. Standardizing Data (transform them into a standard Gaussian distribution with a 
#mean of 0 and a standard deviation of 1) (Use winequality-red.csv)
import pandas as pd
import scipy.stats as s
from sklearn import preprocessing

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\winequality-red.csv")
print('\nInitial Mean: ',s.tmean(df).round(2))

print('\n\nInitial StandardvDeviation:')
print('---------------------------------')
print(round(df.std(),2))

df_scaled = preprocessing.scale(df)
df_scaled.mean(axis=0)
df_scaled.std(axis=0)

print('\nStandardized Data\n',df_scaled.round(2))
print("\nScaled Mean:",s.tmean(df_scaled).round(2))
print("\nScaled standard Deviation: ",round(df_scaled.std(),2))
