#Lab 7 Solution 3/20/2025 Larbi Moukhlis
# This code reads information from tables in a web page and creates a DataFrame with it
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
pd.set_option('display.max_columns', 7)
pd.set_option('display.width', 200)

tables = pd.read_html("https://en.wikipedia.org/wiki/Chicago")


print("The number of tables: ", len(tables))

#The eight table in the webpage becomes the eight DataFrame and so use index 7 for list
teams_df = tables[7]
print("Columns in DataFrame:", teams_df.columns)


sport = input("please enter a Sport (e.g. Baseball, Football, " +
               "Basketball, Ice Hockey, or Soccer) or 'end' ")

while  sport != "end":
    
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



