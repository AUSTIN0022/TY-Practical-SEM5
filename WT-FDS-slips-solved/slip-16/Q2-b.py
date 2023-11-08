#Q.2 B) Write a python program to create a data frame for students information such as name, 
#graduation percentage and age. Display average age of students, average of graduation percentage.
import pandas as pd

df = pd.DataFrame(columns = ['name','age','Per'])

df.loc[0] = ['jitu',3,85]
df.loc[1] = ['Austin',19,95]
df.loc[2] = ['saquib',20,77]
df.loc[3] = ['Naufil',30,80]
df.loc[4] = ['Kunal',21,65]
df.loc[5] = ['Tanishq',18,77]
df.loc[6] = ['Arpita',17,65]
df.loc[7] = ['vaishavi',19,85]

print(df)
# Calculate the average age of students
avg_age = df['age'].mean()
# Calculate the average graduation percentage
avg_pre = df['Per'].mean()
# Print the average age and average graduation percentage
print('Average age of students:', avg_age)
print('Average graduation percentage:', avg_pre)
