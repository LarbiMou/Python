# Name: Larbi Moukhlis
# Date: April 24, 2025
# This program reads in data from the City of Chicago salaries dataset
# and creates two types of visualizations using seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
url = "https://data.cityofchicago.org/resource/xzkq-xp2w.json"
df = pd.read_json(url)

# Clean column names: lowercase, replace spaces with underscores
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# Print again after cleaning
print("\nCleaned column names:")
print(df.columns)

# Convert 'annual_salary' to numeric
df['annual_salary'] = pd.to_numeric(df['annual_salary'], errors='coerce')

# Drop rows with missing or zero salary
df = df[df['annual_salary'] > 0]

# Filter for top 6 departments by number of employees
top_departments = df['department'].value_counts().nlargest(6).index
df_filtered = df[df['department'].isin(top_departments)]

# Set Seaborn theme
sns.set(style="whitegrid")

# Visualization 1: Two side-by-side plots
plt.figure(figsize=(14, 6))

# Plot 1: Barplot - average salary by department
plt.subplot(1, 2, 1)
sns.barplot(data=df_filtered, x='department', y='annual_salary', estimator='mean')
plt.title("Average Salary by Department")
plt.xticks(rotation=45)

# Plot 2: Boxplot - salary distribution by department
plt.subplot(1, 2, 2)
sns.boxplot(data=df_filtered, x='department', y='annual_salary')
plt.title("Salary Distribution by Department")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("salary_comparison_plots.png")
plt.show()

# Visualization 2: Histogram of Annual Salary
plt.figure(figsize=(8, 5))
sns.histplot(df['annual_salary'], bins=40, kde=True)
plt.title("Distribution of Annual Salaries")
plt.xlabel("Annual Salary")
plt.ylabel("Frequency")
plt.savefig("salary_histogram.png")
plt.show()

# Visualization Write-Up – Larbi Moukhlis
# For this assignment, I created two types of visualizations using Seaborn
# to analyze data from the City of Chicago salaries dataset:
#
# 1. Barplot and Boxplot Combination:
#    This visualization compares the average annual salary across the top six
#    departments with the highest number of employees. The barplot provides a
#    view of which departments offer higher average compensation, while the boxplot
#    reveals the spread and distribution of salaries within each department,
#    highlighting medians, variability, and outliers.
#
# 2. Histogram with KDE (Kernel Density Estimate):
#    The second visualization displays the distribution of all annual salaries
#    in the dataset. The histogram shows the frequency of different salary ranges,
#    and the KDE overlay helps visualize the shape of the distribution. This plot
#    shows a right-skewed distribution, indicating that most employees earn moderate
#    salaries while a smaller group earns significantly higher wages.
#
# These visualizations provide insight into salary disparities across departments
# and the overall distribution of compensation among city employees. They help
# identify trends and areas for further analysis.

