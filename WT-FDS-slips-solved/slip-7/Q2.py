#Q.2) Write a Python program to perform the following tasks : 
#a. Apply OneHot coding on Country column. 
#b. Apply Label encoding on purchased column 
#(Data.csv have two categorical column the country column, and the purchased column)
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\Data.csv")
#a. Apply OneHot coding on Country column. 
hotencoder = OneHotEncoder()
enc_df = pd.DataFrame(hotencoder.fit_transform(df[['Country']]).toarray())
df = df.join(enc_df)
print('\n\nOneHot encoding on country column')
print(df)
#b. Apply Label encoding on purchased column 
labelencoder = LabelEncoder()
df['Purchased'] = labelencoder.fit_transform(df['Purchased'])
print('\n\n Label encoding on purchased column')
print(df)
