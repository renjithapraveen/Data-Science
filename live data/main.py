# Import libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for statistical data visualization
from sklearn.datasets import load_iris # for loading the Iris dataset
from sklearn.preprocessing import LabelEncoder, MinMaxScaler # for preprocessing
from sklearn.cluster import KMeans # for clustering
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Exploratory data analysis
print("Shape of the dataset:", df.shape)
print(df.head())
print(df.info())
print("Missing values in each column:\n", df.isnull().sum())

# Declare feature vector and target variable
X = df
y = iris.target  # Using the actual target variable from the dataset

# Feature Scaling
ms = MinMaxScaler()
X_scaled = ms.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# K-Means model with two clusters
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X_scaled)

# Print cluster centers
print("Cluster centers for 2 clusters:", kmeans.cluster_centers_)

# Check quality of classification by the model
labels = kmeans.labels_
correct_labels = sum(y == labels)
print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))
print('Accuracy score: {0:0.2f}'.format(correct_labels / float(y.size)))

# Use elbow method to find optimal number of clusters
cs = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X_scaled)
    cs.append(kmeans.inertia_)

plt.plot(range(1, 11), cs)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# Fit K-Means with a specified number of clusters (e.g., 3 for Iris)
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X_scaled)
labels = kmeans.labels_
print("Final cluster labels with 3 clusters:", labels)
