import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("\nLoading Titanic Dataset...")
Titanic = pd.read_csv(r"Titanic.csv")

print("\nFirst 5 Rows of Dataset:")
print(Titanic.head())

print("\nColumns in Dataset:")
print(Titanic.columns)

print("\nShape of Dataset (Rows, Columns):")
print(Titanic.shape)

# Checking Missing Values
print("\nMissing Values in Each Column:")
print(Titanic.isnull().sum())

# Heatmap Before Cleaning
print("\nDisplaying Heatmap of Missing Values...")

plt.figure(figsize=(12,6))
sns.heatmap(Titanic.isnull(), cmap="spring", yticklabels=False)

plt.title("Missing Values Before Cleaning")
plt.xlabel("Columns")
plt.ylabel("Passengers")
plt.xticks(rotation=45)

plt.show()

# Dropping Deck / Cabin Safely
print("\nDropping 'deck' or 'Cabin' column if present...")

Titanic.drop(["deck", "Cabin"], axis=1, inplace=True, errors="ignore")

print("\nDataset After Dropping Deck/Cabin:")
print(Titanic.head())

# Removing Remaining Missing Rows
print("\nRemoving Remaining Rows with Missing Values...")
print(Titanic.dropna(inplace=True))

# Heatmap After Cleaning
print("\nHeatmap After Removing Missing Values...")

plt.figure(figsize=(12,6))
sns.heatmap(Titanic.isnull(), cmap="spring", yticklabels=False, cbar=False)

plt.title("Missing Values After Cleaning")
plt.xlabel("Columns")
plt.ylabel("Passengers")
plt.xticks(rotation=45)

plt.show()

print("\nChecking Missing Values Again:")
print(Titanic.isnull().sum())

# Converting Sex Column Safely
print("\nConverting 'sex' Column into Numeric...")

sex_column = [col for col in Titanic.columns if col.lower() == "sex"]

if sex_column:
    print(pd.get_dummies(Titanic[sex_column[0]]).head())
    sex = pd.get_dummies(Titanic[sex_column[0]], drop_first=True)
    print("\nSex Dummy Column:")
    print(sex.head())
else:
    print("Sex column not found")
    sex = pd.DataFrame()

# Converting Embarked Column Safely
print("\nConverting 'embarked' Column into Numeric...")

emb_column = [col for col in Titanic.columns if col.lower() == "embarked"]

if emb_column:
    print(pd.get_dummies(Titanic[emb_column[0]]).head())
    arked = pd.get_dummies(Titanic[emb_column[0]], drop_first=True)
else:
    print("Embarked column not found")
    arked = pd.DataFrame()

# Converting Passenger Class
print("\nConverting 'pclass' Column into Numeric...")

if "pclass" in Titanic.columns:
    pclass = pd.get_dummies(Titanic["pclass"], drop_first=True)
    print(pclass.head())
else:
    print("pclass column not found")
    pclass = pd.DataFrame()

# Combining Dummy Columns
print("\nCombining Dummy Columns with Original Dataset...")

Titanic = pd.concat([Titanic, sex, pclass, arked], axis=1)

# Final Dataset
print("\nFinal Updated Dataset:")
print(Titanic.head())

print("\nFinal Dataset Shape:")
print(Titanic.shape)
