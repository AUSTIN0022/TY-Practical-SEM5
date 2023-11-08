#c. Normalizing Data ( rescale each observation to a length of 1 (a unit norm). For this, use the Normalizer class.)
import pandas as pd
import scipy.stats as s
from sklearn import preprocessing

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\winequality-red.csv")
dn = preprocessing.normalize(df,norm = 'l1')
print("\n L1 Normalized Data")
print("-----------------------")
print(dn.round(2))
