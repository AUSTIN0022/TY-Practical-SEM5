import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("D:\Computer Science\TY\SEM5\FDS\iris.csv")
df['Species'].value_counts().plot.pie(explode=[0.1,0.1,0.1],autopct='%1.1f%%',shadow=True)
plt.title("Iris Species %")
plt.show()
