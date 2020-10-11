import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import seaborn as sns

print(np.__version__)
a = np.array([1 ,2 ,3 ,4 ,5])
print(a)
print(a.shape)
print(a.dtype)

print(pd.__version__)
a = pd.Series([10 ,20, 30], index = ['a','b','c'])
print(a)
print(type(a))

a = [10,20,30,40,50]
df = pd.DataFrame(a)
print(df)

plt.plot([1,2,3,4], [10,20,30,40])
plt.title("Sales plot")
plt.xlabel("month")
plt.ylabel("sales")
plt.show()

# IRIS flower species prediction :
iris = pd.read_csv("IRIS.csv")
print(iris.shape)
print(iris.columns)
print(iris["species"].value_counts())

iris.plot(kind = 'scatter', x = 'sepal_length',y = 'sepal_width')
sns.set_style("whitegrid")
sns.FacetGrid(iris, hue = "species", size = 4).map(plt.scatter, "sepal_length","sepal_width").add_legend()
# plt.show()
# plt.close()
sns.set_style("whitegrid")
sns.pairplot(iris, hue = "species", size = 5)
plt.show()


