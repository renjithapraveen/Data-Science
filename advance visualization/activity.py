import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

weather = pd.read_csv(r"C:\Users\USER\Desktop\data science\advance visualization\Weather Dataset - Trial Activity DataSet.csv.csv")
print(weather.head())
print(weather.info())

#  Barplot
sns.barplot(x='humidity', y='temperature', data=weather)
plt.show()

#  distplot is deprecated → use histplot
sns.histplot(weather['humidity'], kde=True)
plt.show()

#  Histogram + rug
sns.histplot(weather['humidity'])
sns.rugplot(weather['humidity'])
plt.show()

#  Joint plots (with keyword arguments)
sns.jointplot(x='humidity', y='temperature', data=weather)
sns.jointplot(x='humidity', y='temperature', data=weather, kind="hex")
sns.jointplot(x='humidity', y='temperature', data=weather, kind="kde")

# pairplot
sns.pairplot(weather[['humidity', 'temperature']])
plt.show()

# stripplot
sns.stripplot(x='weather_type', y='temperature', data=weather)
plt.show()

# swarmplot
sns.swarmplot(x='weather_type', y='temperature', data=weather)
plt.show()

# boxplot
sns.boxplot(x='weather_type', y='temperature', data=weather)
plt.show()

# barplot
sns.barplot(x='weather_type', y='temperature', data=weather)
plt.show()

# countplot
sns.countplot(data=weather["humidity"])
plt.show()




