# Import libraries
import pandas as pd
import seaborn as sb
import numpy as np
from matplotlib import pyplot as plt

# OPTION 1: Load Seaborn built-in dataset

print("Loading built-in 'iris' dataset...")
df = sb.load_dataset("iris")

# Display first few rows
print("\nSample of built-in dataset:")
print(df.head())

# Plot distribution of one column
sb.displot(df['petal_length'],kde=True)
plt.title("Distribution of Petal Length (Built-in Iris Dataset)")
plt.show()

# OPTION 2: Load your own local CSV dataset
print("\nLoading local Iris.csv file (if available)...")
df_local = pd.read_csv("Iris.csv")
print("\nSample of local dataset:")

# OPTION 3:  Load Seaborn's built-in Iris dataset
# Plot the distribution of petal_length (only KDE curve, no histogram)
sb.distplot(df['petal_length'], hist=False)
plt.show()

#fitting parametric distribution
df = sb.load_dataset('iris')
sb.distplot(df['petal_length'])
plt.show()

#scatter plot
sb.jointplot(x='petal_length', y='petal_width', data=df)
plt.show()

#pairplot
sb.set_style("ticks")
sb.pairplot(df, hue='species', diag_kind="kde", kind="scatter", palette="husl")
plt.show()

#seaborn
# Generate a 10x12 matrix of random numbers between 0 and 1
uniform_data = np.random.rand(10, 12)

# Create a heatmap from the generated data
ax = sb.heatmap(uniform_data)
plt.show()




   