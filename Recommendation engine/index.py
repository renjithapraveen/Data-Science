# IMPORT LIBRARIES AND DATASET

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# Importing Dataset
ratings_df = pd.read_csv('ratings.csv')
print("Ratings Dataset:")
print(ratings_df.head())

# Importing Movies Dataset
movies_df = pd.read_csv('movies.csv')
print("\nMovies Dataset:")
print(movies_df.head())

# DATA PREPROCESSING

# Extract year from title
movies_df['year'] = movies_df.title.str.extract(r'(\(\d\d\d\d\))', expand=True)
print("\nAfter Extracting Year:")
print(movies_df.head())

# Remove parentheses from year
movies_df['year'] = movies_df.year.str.extract(r'(\d\d\d\d)', expand=True)
print("\nYear Column:")
print(movies_df.head())

# Remove year from title
movies_df['title'] = movies_df.title.str.replace(r'(\(\d\d\d\d\))', '', regex=True)
print("\nAfter Removing Year from Title:")
print(movies_df.head())

# Remove whitespaces
movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())

# Convert genres into a list
movies_df['genres'] = movies_df.genres.str.split('|')
print("\nGenres Converted to List:")
print(movies_df.head())

# One Hot Encoding
movies_copy = movies_df.copy()

for index, row in movies_df.iterrows():
    for genre in row['genres']:
        movies_copy.at[index, genre] = 1

print("\nOne Hot Encoded Data:")
print(movies_copy.head())

# Fill NaN values with 0
movies_copy = movies_copy.fillna(0)
print("\nAfter Filling NaN Values:")
print(movies_copy.head())
# Ratings Dataset
print("\nRatings Dataset:")
print(ratings_df.head())
# Drop timestamp column
ratings_df = ratings_df.drop(['timestamp'], axis=1)
print("\nRatings Dataset After Dropping Timestamp:")
print(ratings_df.head())

user_input = [
    {'title': 'Grand Slam', 'rating': 5.6},
    {'title': 'Zero', 'rating': 7},
    {'title': 'Jumanji', 'rating': 8.5},
    {'title': 'Toy Story', 'rating': 4.5}
]
movies_input = pd.DataFrame(user_input)
print("\nUser Input:")
print(movies_input)
input_id = movies_df[movies_df['title'].isin(movies_input['title'].tolist())]
movies_input = pd.merge(input_id, movies_input)
print("\nMerged User Input:")
print(movies_input)
movies_input = movies_input.drop(['genres', 'year'], axis=1)
print("\nMovies Input After Dropping Columns:")
print(movies_input)
movies_user = movies_copy[movies_copy['movieId'].isin(movies_input['movieId'].tolist())]
print("\nMovies User:")
print(movies_user)
movies_user = movies_user.reset_index(drop=True)
print("\nMovies User After Resetting Index:")
print(movies_user)
UserGenreTable = movies_user.drop(['movieId', 'title', 'genres', 'year'], axis=1)
print("\nUser Genre Table:")
print(UserGenreTable)
# Dot product to get weights
UserProfile = UserGenreTable.transpose().dot(movies_input['rating'])
print("\nUser Profile:")
print(UserProfile)
# Genre Table for all movies
GenreTable = movies_copy.set_index(movies_copy['movieId'])
GenreTable = GenreTable.drop(['movieId', 'title', 'genres', 'year'], axis=1)
print("\nGenre Table:")
print(GenreTable.head())
# Recommendation values
Recommendation_df = ((GenreTable * UserProfile).sum(axis=1)) / UserProfile.sum()
print("\nRecommendation Scores:")
print(Recommendation_df.head())
Recommendation_df = Recommendation_df.sort_values(ascending=False)
print("\nTop Recommendation Scores:")
print(Recommendation_df.head())
RecommendationTable = movies_df.loc[movies_df['movieId'].isin(Recommendation_df.head(20).keys())]
print("\nTop 20 Recommended Movies:")
print(RecommendationTable)