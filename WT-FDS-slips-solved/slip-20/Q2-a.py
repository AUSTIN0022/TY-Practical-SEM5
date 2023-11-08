# Q.2 A) Generate a random array of 50 integers and display them using a line chart, scatter plot, 
# histogram and box plot. Apply appropriate color, labels and styling options. 
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.randint(0, 100, 50)

# Line chart
plt.subplot(2,2,1)
plt.plot(data, color='blue', marker='o')
plt.title('Line Chart')
plt.xlabel('Index')
plt.ylabel('Value')

# Scatter plot
plt.subplot(2,2,2)
plt.scatter(range(len(data)), data, color='green', marker='x')
plt.title('Scatter Plot')
plt.xlabel('Index')
plt.ylabel('Value')

# Histogram
plt.subplot(2,2,3)
plt.hist(data, bins=10, color='red', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Box plot
plt.subplot(2,2,4)
plt.boxplot(data)
plt.title('Box Plot')
plt.xlabel('Value')

plt.tight_layout()
plt.show()
