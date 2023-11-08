# 2.Create two lists, one representing subject names and the other representing marks obtained in 
# those subjects. Display the data in bar chart
import matplotlib.pyplot as plt

subjects = ['WT', 'FDS', 'OS', 'CN', 'TCS']
marks = [90, 88, 78, 95, 70]

# Bar chart
plt.bar(subjects, marks, color='skyblue')
plt.title('Bar Chart')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()
