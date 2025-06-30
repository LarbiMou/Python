# Assignment 4, 4/7/2025
# Larbi Moukhlis

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Load data
url = "https://data.cityofchicago.org/resource/xzkq-xp2w.json"
df = pd.read_json(url)

# Clean and convert data
df['annual_salary'] = pd.to_numeric(df['annual_salary'], errors='coerce')
df['hourly_rate'] = pd.to_numeric(df['hourly_rate'], errors='coerce')
df = df.dropna(subset=['annual_salary', 'department'])

# Add is_police dummy variable
df['is_police'] = df['department'].str.upper().apply(lambda x: 1 if 'POLICE' in x else 0)

# --- Verify dataset has both classes ---
print("\n--- Police Department Breakdown ---")
print(df['is_police'].value_counts())

# --- MULTIPLE REGRESSION ---
# Dependent variable: annual_salary
# Independent variables: is_police (dummy variable)

model = smf.ols('annual_salary ~ is_police', data=df).fit()
print("\n--- MULTIPLE REGRESSION RESULTS ---")
print(model.summary())

# --- LOGISTIC REGRESSION ---
# Dependent variable: is_police
# Independent variable: annual_salary

# --- MULTIPLE REGRESSION RESULTS ---
# R-squared: 0.058
# The coefficient for 'is_police' is positive and statistically significant (p < 0.001),
# indicating that individuals in the police department earn a higher salary compared to non-police employees.
# Specifically, being in the police department increases annual salary by about $12,260 on average.
# 
# --- LOGISTIC REGRESSION RESULTS ---
# The coefficient for 'annual_salary' is positive and statistically significant (p < 0.001),
# indicating that higher salaries increase the likelihood of being in the police department.
# Specifically, as annual salary increases, the odds of being in the police department increase by about
# 0.00002033 for each dollar increase in salary.
