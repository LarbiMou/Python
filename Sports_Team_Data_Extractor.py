#Lab 7 Solution 3/20/2025 Larbi Moukhlis
# This code reads information from tables in a web page and creates a DataFrame with it
import pandas as pd
from io import StringIO
import requests

pd.set_option('display.max_columns', 7)
pd.set_option('display.width', 200)

headers = {"User-Agent": "Mozilla/5.0 (compatible; student-lab-script/1.0)"}
response = requests.get("https://en.wikipedia.org/wiki/Chicago", headers=headers)
tables = pd.read_html(StringIO(response.text))

print("The number of tables: ", len(tables))

# Automatically find the sports table
teams_df = None
for i, t in enumerate(tables):
    if "Sport" in t.columns:
        teams_df = t
        print(f"Sports table found at index {i}")
        break

if teams_df is None:
    print("Sports table not found on the page.")
else:
    print("Columns in DataFrame:", teams_df.columns.tolist())

    sport = input("please enter a Sport (e.g. Baseball, Football, " +
                   "Basketball, Ice Hockey, or Soccer) or 'end' ")

    while sport != "end":

        if sport in ["Baseball", "Football", "Basketball",
                      "Ice Hockey", "Soccer"]:
            # The following record line will return all the records in the DF that have teams in that sport
            query_string = "Sport == '" + sport + "'"
            print("The query string is:", query_string)
            teams = teams_df.query(query_string)

            print(f"The Chicago teams in the {sport} are:")
            print(teams)

        else:
            print(f"There are no Chicago teams in the {sport} Sport:")

        sport = input("please enter a Sport (e.g. Baseball, Football, " +
                   "Basketball, Ice Hockey, or Soccer) or 'end' ")