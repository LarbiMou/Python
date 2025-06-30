# Lab 5 Solution 2/27/2025 Larbi Moukhlis
import pandas as pd
pd.set_option('display.max_columns', 7)
#Create a Pandas DataFrame from the data in the trip_data.json file.
trip_data_df = pd.read_json("trip_data.json")

print("The data type of trip_data is: ", type(trip_data_df))
#Print out the columns in the DataFrame.

print("The columns of trip_data are: ", trip_data_df.columns)
#Reduce the columns in the dataframe to the following seven:
# 'trip_seconds', 'trip_miles', 'pickup_community_area',
# 'dropoff_community_area', 'fare', 'tips', 'payment_type'

trip_data_df= trip_data_df[['trip_seconds', 'trip_miles', 'pickup_community_area','dropoff_community_area', 'fare', 'tips', 'payment_type']]
print("The columns of the trip_data_df now are:", trip_data_df.columns)


# Print out the descriptive statistics of the DataFrame.
print("Descriptive statistics of trip_data are:\n", trip_data_df.describe())

#Make the pickup_community_area column the index of the DataFrame and
#then print out the first 7 records of the DataFrame.
trip_data_df.set_index('pickup_community_area', inplace = True)

print("After changing index, first seven records:\n", trip_data_df.head(7))
# Create a Series named trip_payment from the payment_type column 
# and then print out the data type of trip_payment.
trip_payment = trip_data_df['payment_type']


print("The data type of trip_payment is: ", type(trip_payment))
# print out the counts of each payment type in the trip_payment series
print("The counts of payment type are: \n", trip_payment.value_counts())                               


