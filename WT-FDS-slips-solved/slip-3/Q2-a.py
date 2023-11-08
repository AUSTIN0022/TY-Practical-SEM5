# Q.2 A)Write a Python program to create box plots to see how each feature i.e. Sepal Length, 
# Sepal Width, Petal Length, Petal Width are distributed across the three species
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the Iris dataset
iris = pd.read_csv("D:\Computer Science\TY\SEM5\WT-1\slips-solved\iris.csv")
# Create box plots for each feature across the three species
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
sns.boxplot(x="Species", y="SepalLengthCm", data=iris)
plt.title("Sepal Length by Species")

plt.subplot(2, 2, 2)
sns.boxplot(x="Species", y="SepalWidthCm", data=iris)
plt.title("Sepal Width by Species")

plt.subplot(2, 2, 3)
sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
plt.title("Petal Length by Species")

plt.subplot(2, 2, 4)
sns.boxplot(x="Species", y="PetalWidthCm", data=iris)
plt.title("Petal Width by Species")

plt.tight_layout()
plt.show()
