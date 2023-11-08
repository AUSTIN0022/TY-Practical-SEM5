# c. Binarizing Data using we use the Binarizer class (Using a binary threshold, it is possible 
# to transform our data by marking the values above it 1 and those equal to or below it, 0) 
import pandas as pd
import scipy.stats as s
from sklearn import preprocessing

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\winequality-red.csv")

df_binarized = preprocessing.Binarizer(threshold=5).transform(df)
print("\n Binarized data")
print("-------------------")
print(df_binarized)
