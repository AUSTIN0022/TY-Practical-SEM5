# Q.2 A) Generate a random array of 50 integers and display them using a line chart, scatter plot
# Apply appropriate color, labels and styling options

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

plt.tight_layout()
plt.show()
