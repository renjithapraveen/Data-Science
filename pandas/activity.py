import pandas as pd
import numpy as np

# Create a dictionary of exam data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
              'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no', 'yes']
}

# Define row labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create the DataFrame
df = pd.DataFrame(exam_data, index=labels)

# Print summary information about the DataFrame
print("Summary of the basic information about this DataFrame and its data:")
df.info()   # <-- just call df.info(), do NOT wrap in print()

# (Optional) Display the DataFrame itself
print("\nDataFrame contents:\n")
print(df)
