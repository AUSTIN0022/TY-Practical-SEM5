"""Q.2) Create a dataset data.csv having two categorical column (the country column, and the 
purchased column). [15] 
a. Apply OneHot coding on Country column. 
b. Apply Label encoding on purchased column"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\Data.csv")
#a. Apply OneHot coding on Country column. 
hot_en = OneHotEncoder()
enc_df = pd.DataFrame(hot_en.fit_transform(df[['Country']]).toarray())
df = df.join(enc_df)
print('\n\nOneHot encoding on country column')
print(df)
#b. Apply Label encoding on purchased column 
label_en = LabelEncoder()
df['Purchased'] = label_en.fit_transform(df['Purchased'])
print('\n\n Label encoding on purchased column')
print(df)
