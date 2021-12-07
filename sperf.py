import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("StudentsPerformance.csv")

x = dataframe['gender']
y = dataframe.groupby('gender').get_group('female')['math score'].mean()
z = dataframe.groupby('gender').get_group('male')['math score'].mean()

a = dataframe['lunch']
b = dataframe.groupby('lunch').get_group('standard')['math score'].mean()
c = dataframe.groupby('lunch').get_group('free/reduced')['math score'].mean()

plt.subplot(1, 2, 1)
plt.xlabel("Gender")
plt.ylabel("Math Score")

plt.bar(x.unique(), [z, y])

plt.subplot(1, 2, 2)
plt.xlabel("Lunch Type")
plt.ylabel("Math Score")

plt.bar(a.unique(), [b, c])

plt.show()