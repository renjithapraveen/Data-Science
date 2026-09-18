import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import the dataset using Pandas
df = pd.read_csv("IMDB Dataset.csv")

# 2. Print the first three and last three rows of the dataset
print("First 3 rows:")
print(df.head(3))
print("\nLast 3 rows:")
print(df.tail(3))

# 3. Detailed information of the dataset
print("\nDataset Info:")
print(df.info())

# 4. Check for null values
print("\nNull Values Check:")
print(df.isnull().sum())

# 5. Subset of rows between 41 and 75
subset_df = df.iloc[40:75]
print("\nSubset (Rows 41–75):")
print(subset_df)

# 6. Movie having the highest number of votes
max_votes_movie = df[df['No_of_Votes'] == df['No_of_Votes'].max()]
print("\nMovie with Highest Votes:")
print(max_votes_movie)

# 7. Boxplot for IMDB_Rating and Runtime
plt.figure(figsize=(10,5))
sns.boxplot(data=df[['IMDB_Rating','Runtime']])
plt.title("Boxplot of IMDB Rating & Runtime")
plt.show()

# 8. Relationship between IMDB_Rating and Runtime
plt.figure(figsize=(8,5))
plt.scatter(df['Runtime'], df['IMDB_Rating'])
plt.xlabel("Runtime (minutes)")
plt.ylabel("IMDB Rating")
plt.title("IMDB Rating vs Runtime")
plt.grid(True)
plt.show()

# 9. Distribution of IMDB_Rating and Runtime
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.hist(df['IMDB_Rating'])
plt.title("Distribution of IMDB Rating")

plt.subplot(1,2,2)
plt.hist(df['Runtime'])
plt.title("Distribution of Runtime")
plt.show()

# 10. Count plot of Rating feature
plt.figure(figsize=(10,5))
sns.countplot(x=df['IMDB_Rating'])
plt.xticks(rotation=90)
plt.title("Count of Movies by IMDB Rating")
plt.show()
