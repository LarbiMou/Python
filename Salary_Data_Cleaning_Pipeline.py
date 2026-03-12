# Author: Larbi Moukhlis
# Date Created: 3/20/20
# Description: This script performs data cleaning and transformation on a CSV dataset.

import pandas as pd

# Step 1: Load the CSV file with low_memory set to False to avoid mixed types warning
file_path = "/Users/larbimoukhlis/Library/CloudStorage/OneDrive-LoyolaUniversityChicago/INFS 394/Homework 2/Salaries.csv"
df = pd.read_csv(file_path, low_memory=False)

# Step 2: Print the names of the columns in the DataFrame to understand the structure
print("Column Names:", df.columns)

# Step 3: Check if 'Department' column exists before selecting it
if "Department" in df.columns:
    # Reduce the number of columns to five specific columns (including 'Department' if it exists)
    df_reduced = df[["JobTitle", "BasePay", "OvertimePay", "Benefits", "Department"]].copy()
else:
    # If 'Department' column doesn't exist, use a fallback
    print("Department column not found, using alternative columns.")
    df_reduced = df[["JobTitle", "BasePay", "OvertimePay", "Benefits"]].copy()

# Step 4: Convert 'BasePay' to numeric, forcing errors to NaN (this will handle all strings)
df_reduced["BasePay"] = pd.to_numeric(df_reduced["BasePay"], errors='coerce')

# Step 5: Use .count() method to report the number of rows in the DataFrame
print("Number of rows before removing any:", df_reduced.count())

# Step 6: Remove rows based on a condition (for example, remove rows where 'BasePay' is 0)
df_reduced = df_reduced.query("BasePay > 0")

# Step 7: Report the number of rows after removing the rows
print("Number of rows after removal:", df_reduced.count())

# Step 8: Create a new column indicating if 'BasePay' is less than 50
# Initialize the new column with 0 for all rows
df_reduced['value_lt_50'] = 0

# Step 9: Use .loc to assign the value 1 where 'BasePay' is less than 50
df_reduced.loc[df_reduced['BasePay'] < 50, 'value_lt_50'] = 1

# Step 10: Use .get_dummies() to create dummy variables for the 'Department' column
# This will turn categorical values in 'Department' into binary indicator columns if the column exists
if "Department" in df_reduced.columns:
    df_reduced_dummies = pd.get_dummies(df_reduced, columns=["Department"], drop_first=True)
else:
    # If 'Department' column is not in the DataFrame, skip this part
    df_reduced_dummies = df_reduced

# Step 11: Use .head() to report the first 4 rows of the cleaned DataFrame
print("\nFirst 4 rows of the DataFrame:")
print(df_reduced_dummies.head(4))

# Step 12: Use .tail() to report the last 7 rows of the cleaned DataFrame
print("\nLast 7 rows of the DataFrame:")
print(df_reduced_dummies.tail(7))

# Step 13: Save the cleaned DataFrame to a new CSV file without the index
df_reduced_dummies.to_csv("Cleaned_Salaries_Updated.csv", index=False)

print("\nData cleaning and transformation complete. Saved as 'Cleaned_Salaries_Updated.csv'.")
