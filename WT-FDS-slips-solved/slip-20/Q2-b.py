#Q.2 B) Add two outliers to the above data and display the box plot
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
#np.random.seed(0)
data = np.random.randint(0, 100, 50)

# Adding outliers
data = np.append(data, [150, 200])

# Box plot with outliers
plt.boxplot(data, vert=False)
plt.title('Box Plot with Outliers')
plt.xlabel('Value')
plt.show()
