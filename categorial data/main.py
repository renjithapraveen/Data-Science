import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("Titanic Dataset.csv")

# Display first 5 rows
print("First 5 rows of dataset:")
print(data.head())


print("\nData Types:")
print(data.dtypes)


nominal_cat = ['Name', 'Ticket', 'Cabin']

# Ordinal categorical variables (ordered)
ordinal_cat = ['Embarked', 'Gender']

print("\nNominal Categorical Features:", nominal_cat)
print("Ordinal Categorical Features:", ordinal_cat)

print("\nGender Value Counts:")
print(data['Gender'].value_counts())

gender_categories = ['Female', 'Male']

data['Gender'] = pd.Categorical(
    data['Gender'],
    categories=gender_categories,
    ordered=True
)

median_index_gender = int(np.median(data['Gender'].cat.codes))
median_gender = gender_categories[median_index_gender]

print("Median Gender:", median_gender)


print("\nEmbarked Value Counts:")
print(data['Embarked'].value_counts())

embarked_categories = ['S', 'C', 'Q']

data['Embarked'] = pd.Categorical(
    data['Embarked'],
    categories=embarked_categories,
    ordered=True
)

median_index_embarked = int(np.median(data['Embarked'].cat.codes))
median_embarked = embarked_categories[median_index_embarked]

print("Median Embarked:", median_embarked)
