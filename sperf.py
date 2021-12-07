import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataframe = pd.read_csv("StudentsPerformance.csv")

x = dataframe['reading score']
y = dataframe['math score']

plt.scatter(x, y)
plt.show()