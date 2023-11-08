#Q.2 B) Use the heights and weights dataset and load the dataset from a given csv file into a 
#dataframe. Print the first, last 5 rows and random 10 row
import pandas as pd

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\SOCR-HeightWeight.csv")

print("First five: \n",df.head(5))
print("Last five:\n",df.tail(5))
print("Random Ten:\n",df.sample(n=10))
