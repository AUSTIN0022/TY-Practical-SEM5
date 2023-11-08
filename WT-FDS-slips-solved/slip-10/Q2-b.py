# Q.2 B) Write a python program to compute sum of Manhattan distance between all pairs of points. 
import numpy as np

# Define a list of points as NumPy arrays
points = [np.array([1, 2]), np.array([3, 4]), np.array([5, 6])]
# Initialize the sum of Manhattan distances
manhattan_sum = 0
# Calculate the sum of Manhattan distances
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        manhattan_sum += np.sum(np.abs(points[i] - points[j]))

print("Sum of Manhattan distances between all pairs of points:", manhattan_sum)
