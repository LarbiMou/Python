import pandas as pd
import requests

endpoint = "https://data.cityofchicago.org/resource/tfm3-3j95.json"

# Add SoQL parameters to obtain
#    a list of companies with active licenses

#    and the number of active licenses each has.

#    Only have companies with at least 30 active licenses

#    and sort in descending order of the number of licenses.


rest_results = requests.get(endpoint + "?" +
                            "$select=company_name,count(status)" +
                            "&$where=status='ACTIVE'" +
                            "&$group=company_name" +
                            "&$having=count_status>=30" +
                            "&$order=count_status desc"
    





                                                ).json()

print("number of resulting records: ", len(rest_results))
results_df = pd.DataFrame.from_records(rest_results)

print("The results of the rest query:")
print(results_df)


