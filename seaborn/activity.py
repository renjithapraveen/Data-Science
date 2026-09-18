import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # pip install seaborn in terminal if red line below
df = pd.read_csv("USA_Housing.csv")
print(df.head(10))
print(df.info())
print(df.describe())
print(df.columns)
sns.pairplot(df)
plt.show()
plt.figure(figsize=(10,6))
df_num = df.select_dtypes(include=np.number)
sns.heatmap(df_num.corr(), annot=True, cmap='viridis')
plt.show()