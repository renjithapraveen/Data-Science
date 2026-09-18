import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the built-in penguins dataset from seaborn
df = pd.read_csv("C:\Users\USER\Desktop\data science\Capstone\penguins_size.csv")

# Display top 10 rows
print(df.head(10))

# Basic info
print(df.shape)
print(df.tail())
print(df.isnull().sum())

# Statistical summaries
print(df.describe().T)
print(df.describe(include="all"))

# Data types and info
print(df.dtypes)
print(df.info())

# Correlation matrix (only numeric columns)
print(df.corr(numeric_only=True))

# Corrected colormap name and heatmap
sns.heatmap(df.corr(numeric_only=True), cmap="Wistia", annot=True)

# Histogram for all numeric columns
df.hist(figsize=(12, 9))
plt.show()

# Value counts for categorical columns
print(df['sex'].value_counts())
print(df['island'].value_counts())
print(df['species'].value_counts())

# Count plots — corrected palette spelling
sns.countplot(data=df, x="sex", palette="summer")
plt.show()

sns.countplot(data=df, x="island", palette="RdPu")
plt.show()

sns.countplot(data=df, x="species", palette="YlOrRd")
plt.show()

sns.countplot(data=df, x="island", hue="sex", palette="spring")
plt.show()

# Pairplot of numeric features with hue by species
sns.pairplot(data=df, hue="species", palette="mako")
plt.show()
