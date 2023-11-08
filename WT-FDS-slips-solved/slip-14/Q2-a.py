#Q. 2 A) Write a Python NumPy program to compute the weighted average along the specified 
#axis of a given flattened array. 
import numpy as np

# Create a flattened array
arr = np.array([1, 2, 3, 4, 5])
# Compute the weighted average of the flattened array
weights = np.array([1, 2, 3, 4, 5])
avg = np.average(arr, weights=weights)
# Print the weighted average
print('Weighted average of the flattened array:',avg)
