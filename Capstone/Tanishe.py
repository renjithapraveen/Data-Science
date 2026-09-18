import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

# Load the CSV
weather = pd.read_csv(r"C:\Users\Tinashe Mehta\New folder\Python Course\Module 22\Advance Visualizations in Python\weather.csv")

# Preview data
print(weather.head())
print(weather.info())

# Bar plot
sns.barplot(x='humidity', y='temperature', data=weather)
plt.title("Barplot of Humidity vs Temperature")
plt.show()

# Distribution plot (replaces deprecated distplot)
sns.histplot(weather['humidity'], kde=True)
plt.title("Distribution of Humidity")
plt.show()

# Histogram without KDE, with rug
sns.histplot(weather['humidity'], kde=False)
sns.rugplot(weather['humidity'])
plt.title("Histogram with Rug Plot (Humidity)")
plt.show()

# Joint plot (scatter + hist)
sns.jointplot(x='humidity', y='temperature', data=weather)
plt.show()

# Joint plot (hex)
sns.jointplot(x='humidity', y='temperature', data=weather, kind='hex')
plt.show()

# Joint plot (kde)
sns.jointplot(x='humidity', y='temperature', data=weather, kind='kde')
plt.show()
