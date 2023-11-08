# Q.2 B)Write a Python program to create a histogram of the three species of the Iris data
import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the CSV file into a pandas DataFrame
df = pd.read_csv('D:\Computer Science\TY\SEM5\WT-1\slips-solved\iris.csv')

# Create a histogram of the petal length for each species
setosa = df[df['Species'] == 'Iris-setosa']
versicolor = df[df['Species'] == 'Iris-versicolor']
virginica = df[df['Species'] == 'Iris-virginica']

plt.hist(setosa['PetalLengthCm'], label='Iris-setosa')
plt.hist(versicolor['PetalLengthCm'], label='Iris-versicolor')
plt.hist(virginica['PetalLengthCm'], label='Iris-virginica')

# Add labels and title to the plot
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.title('Histogram of Petal Length for Three Species of Iris')
plt.legend()
plt.show()
