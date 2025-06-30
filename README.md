# Python
Academic Data Analysis Projects
Author: Larbi Moukhlis

This repository contains a collection of Python scripts for data analysis, statistical modeling, and visualization, developed as part of an advanced data science course. Projects range from basic descriptive statistics to API-driven data aggregation and regression modeling, with a focus on real-world datasets (e.g., Chicago city salaries, transportation metrics).

Project Overview
1. Grade Distribution Analysis
File: grade_distribution_analyzer.py

Description: Compares user-input grades against class statistics (min, median, max) and evaluates proximity to the median using nested conditionals.

Key Techniques: List operations, descriptive statistics, user input validation.

2. Salary Data Cleaning Pipeline
File: salary_data_cleaning_pipeline.py

Description: Cleans and transforms a CSV of employee salaries by filtering invalid entries, converting data types, and generating dummy variables for categorical departments.

Key Techniques: Pandas data wrangling, pd.to_numeric(), pd.get_dummies().

3. Police Salary API Aggregation
File: police_salary_api_aggregator.py

Description: Queries the Chicago Data Portal API to aggregate average salaries for police roles using SoQL, then saves results to JSON.

Key Techniques: API requests (requests), SoQL filtering, pandas aggregation (groupby).

4. Salary Regression Modeling
File: salary_regression_analysis.py

Description: Analyzes salary disparities between police/non-police departments using OLS and logistic regression (statsmodels).

Key Techniques: Dummy variable creation, regression diagnostics, interpretation of p-values/R².

5. Salary Distribution Visualization
File: salary_distribution_visualizer.py

Description: Generates comparative visualizations (barplots, boxplots, histograms) of salary distributions across Chicago city departments using seaborn.

Key Techniques: Data filtering, KDE plots, multi-panel figures (plt.subplot()).

Technical Stack
Languages: Python

Libraries:

Data Wrangling: pandas, numpy

Statistics: scipy, statsmodels

Visualization: matplotlib, seaborn

APIs: requests

Data Sources:

City of Chicago Open Data Portal

Local JSON/CSV files (e.g., trip_data.json, Salaries.csv)

How to Use
Dependencies: Install requirements via pip install -r requirements.txt (see below for template).

Data: Place datasets in a /data directory (or update file paths in scripts).

Execution: Run files individually (e.g., python salary_regression_analysis.py).

requirements.txt Template
text
pandas>=1.4.0
numpy>=1.22.0
requests>=2.28.0
statsmodels>=0.13.0
seaborn>=0.12.0
matplotlib>=3.6.0
scipy>=1.9.0
Key Insights
Policy Implications: Regression models (Lab 4) reveal significant salary gaps for police vs. non-police roles.

Data Quality: Lab 2 highlights challenges in cleaning real-world salary data (e.g., null values, mixed types).

Visual Trends: Lab 5 identifies right-skewed salary distributions and departmental outliers.

License
This project is licensed under the MIT License. See LICENSE for details.

This README is designed to:

Highlight academic rigor with clear technical descriptions.

Emphasize reproducibility with setup instructions.

Showcase analytical insights for potential collaborators or instructors.

Let me know if you'd like to add a project structure diagram or expand any section!
