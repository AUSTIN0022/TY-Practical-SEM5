#Q.2 A) Write a Python program to draw scatter plots to compare two features of the iris dataset
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # For loading the Iris dataset

iris = pd.read_csv("D:\Computer Science\TY\SEM5\FDS\iris.csv")

sns.scatterplot(data=iris, x="SepalLengthCm", y="SepalWidthCm", hue="Species")
plt.title("Comparison of Sepal Length and Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()
