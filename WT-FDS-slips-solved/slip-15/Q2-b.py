import matplotlib.pyplot as plt

subjects = ['WT', 'FDS', 'OS', 'CN', 'TCS']
marks = [90, 88, 78, 95, 70]

# Pie chart
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
