# Lab 9 Solution 4/3/2025 Larbi Moukhlis
import pandas as pd
from statistics import *
from scipy import stats

fares_df = pd.read_json("faresfloat.json")
print(fares_df.columns)

#Print out the mean and median values for fare

print("\nThe mean and median fares are:",mean(fares_df.fare), median(fares_df.fare))


#Print out a correlation matrix for the fare and tips 

print("\nThe correlation matrix of fares and tips:")
print(fares_df[["fare","tips"]].corr())

#Uuse the SciPy package to fit a linear regression model
#with tips being the dep. var. and fare being the ind. var.


slope, intercept, r_value, p_value, std_err = \
       stats.linregress(fares_df.fare, fares_df.tips)
       

#Print out regression model and the R squared value.

print("\nThe linear regression model is:")
print(f"tip = {round(intercept,3)} + {round(slope,3)} * fare ")

print("\nThe R squared value is ", round(r_value**2,3))

