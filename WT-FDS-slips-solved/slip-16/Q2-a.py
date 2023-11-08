# Q.2 A) Write a python program to create two lists, one representing subject names and the other 
# representing marks obtained in those subjects. Display the data in a pie chart and bar chart
import matplotlib.pyplot as plt

subjects = ['WT', 'FDS', 'OS', 'CN', 'TCS']
marks = [90, 88, 78, 95, 70]

# Pie chart
plt.subplot(121)
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title('Pie Chart')

# Bar chart
plt.subplot(122)
plt.bar(subjects, marks, color='skyblue')
plt.title('Bar Chart')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()
