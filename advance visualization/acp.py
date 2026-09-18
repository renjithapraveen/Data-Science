import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("weathersample.csv")

print("\nFIRST 5 ROWS OF DATA:")
print(data.head())

print("\nDATA INFO:")
print(data.info())
numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = data.select_dtypes(include=['object']).columns

sns.pairplot(data)
plt.suptitle("Pairplot of Weather Dataset", y=1.02)
plt.show()

sns.jointplot(x="humidity", y="temperature", data=data, kind="scatter")
sns.jointplot(x="humidity", y="temperature", data=data, kind="hex")
sns.jointplot(x="humidity", y="temperature", data=data, kind="kde")
plt.show()


plt.figure(figsize=(10, 6))
sns.heatmap(data[numeric_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=data[numeric_cols])
plt.title("Boxplot of Numeric Variables")
plt.show()

plt.figure(figsize=(12, 6))
sns.stripplot(x="weather_type", y="temperature", data=data, jitter=True)
plt.title("Stripplot: Temperature vs Weather Type")
plt.show()

plt.figure(figsize=(12, 6))
sns.swarmplot(x="weather_type", y="temperature", data=data)
plt.title("Swarmplot: Temperature vs Weather Type")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data["humidity"], kde=True, bins=8)
plt.title("Distribution of Humidity")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x="weather_type", data=data)
plt.title("Count of Each Weather Type")
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x="weather_type", y="temperature", data=data)
plt.title("Average Temperature by Weather Type")
plt.show()

data["date"] = pd.to_datetime(data["date"])

plt.figure(figsize=(12, 6))
sns.lineplot(x="date", y="temperature", data=data, marker="o")
plt.title("Temperature Over Time")
plt.show()
