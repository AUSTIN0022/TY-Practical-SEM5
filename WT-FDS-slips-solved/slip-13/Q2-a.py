# Q.2 A) Write a Python program to create a graph to find relationship between the petal length 
# and petal width.(Use iris.csv dataset)
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # For loading the Iris dataset

# Load the Iris dataset
df = pd.read_csv("D:\Computer Science\TY\SEM5\FDS\iris.csv")
# Create a scatter plot
sns.scatterplot(data=df, x="PetalLengthCm", y="PetalWidthCm", hue="Species")
plt.title("Relationship Between Petal Length and Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()
