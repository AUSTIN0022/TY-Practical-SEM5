# Q.2 A) Import dataset “iris.csv”. Write a Python program to create a Bar plot to get the 
# frequency of the three species of the Iris data
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\iris.csv")

x= df["Species"]
y = df["SepalLengthCm"]
plt.bar(x,y,color='green')
plt.xlabel("Classes")
plt.ylabel("Sepal Lenght")
plt.title("Iris Species Count")
plt.show()
