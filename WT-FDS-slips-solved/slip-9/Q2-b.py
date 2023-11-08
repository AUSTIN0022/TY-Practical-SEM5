#Q.2 B) Create two lists, one representing subject names and the other representing marks 
#obtained in those subjects. Display the data in a pie chart.

import matplotlib.pyplot as plt

subjects = ['WT', 'FDS', 'OS', 'CN', 'TCS']
marks = [90, 88, 78, 95, 70]

# Pie chart
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title('Pie Chart')

plt.show()
