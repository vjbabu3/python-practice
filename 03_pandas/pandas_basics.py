# Pandas Basics

import pandas as pd

# Creating a simple dataset
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 27, 22],
    "Score": [85, 90, 88]
}

df = pd.DataFrame(data)

# Display DataFrame
print("DataFrame:")
print(df)

# Display column
print("\nNames:")
print(df["Name"])

# Basic statistics
print("\nAverage Score:", df["Score"].mean())
