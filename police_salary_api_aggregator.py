# Larbi Moukhlis
# Assignment 3, 4/3/2025
# Description: This Python program queries the Chicago Data Portal API using SoQL, applies filters, aggregates data (average salary per job title) in Python and saves the results in a JSON file.

# Load required packages
import pandas as pd
import json
import requests

# Define the API endpoint
url = "https://data.cityofchicago.org/resource/xzkq-xp2w.json"

# Set the parameters for the SoQL query
parameters = {
    "$select": "name, job_titles, annual_salary",  # Select columns to return
    "$where": "annual_salary > 50000 AND lower(job_titles) LIKE 'police officer%'",  # Filter data based on conditions
    "$limit": 50  # Limit the number of rows returned to 50
}

# Send the GET request to the API with the parameters
response_with_parameters = requests.get(url, params=parameters)

# Check if the response was successful
if response_with_parameters.status_code == 200:
    
    # the JSON response
    data_with_parameters = response_with_parameters.json()

    # Print the column names of the first record in the returned data
    if len(data_with_parameters) > 0:
        print("\nColumn Names:", list(data_with_parameters[0].keys()))

    # Example Query with parameters that prints the first 50 results
    print("\nFirst 50 Results with Parameters:")
    for entry in data_with_parameters[:50]:
        print(entry)

    # Manually aggregate data (average salary per job title)
    # Convert the JSON data to a pandas DataFrame for easier manipulation
    df = pd.DataFrame(data_with_parameters)

    # Group by 'job_titles' and calculate the average of 'annual_salary'
    aggregated_data = df.groupby('job_titles')['annual_salary'].mean().reset_index()

    # Print out the aggregated data (Job Title and Average Salary)
    print("\nAggregated Data (Job Title and Average Salary):")
    for index, row in aggregated_data.iterrows():
        print(f"Job Title: {row['job_titles']}, Average Salary: {row['annual_salary']}")

    # Save the aggregated data to a JSON file
    aggregated_data_json = aggregated_data.to_dict(orient='records')
    with open('aggregated_data.json', 'w') as json_file:
        json.dump(aggregated_data_json, json_file)

    print("\nAggregated data saved to 'aggregated_data.json'.")
else:
    print(f"Error fetching data: {response_with_parameters.status_code}")
