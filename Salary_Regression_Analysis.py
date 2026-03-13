# Assignment 4, 4/7/2025
# Larbi Moukhlis

import pandas as pd
import requests
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Load data
url = "https://data.cityofchicago.org/resource/xzkq-xp2w.json?$limit=50000"
response = requests.get(url, verify=False)
df = pd.DataFrame(response.json())

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
# Independent variable: is_police (dummy variable)
model = smf.ols('annual_salary ~ is_police', data=df).fit()
print("\n--- MULTIPLE REGRESSION RESULTS ---")
print(model.summary())

# --- LOGISTIC REGRESSION ---
# Dependent variable: is_police
# Independent variable: annual_salary
logit_model = smf.logit('is_police ~ annual_salary', data=df).fit()
print("LOGISTIC REGRESSION RESULTS")
print(logit_model.summary())