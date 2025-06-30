#lab 10 solution 4/10/2025 Larbi Moukhlis
import pandas as pd
import statsmodels.formula.api as smf

trips_df = pd.read_json("taxi trips 2024.json")

#fit a multiple regression model with dependent
#variable trip_total and independent variables
#trip_miles, trip_seconds, extras, tips, and airport
model_ols = smf.ols(formula=("trip_total ~ trip_miles + trip_seconds + " +
                             "extras + tips + airport"), data = trips_df).fit()


#print out the model summary
print ("\nModel summary:  ", model_ols.summary())


#create a dummy variable tip_gt_5 that equals 1
#when tip is greater than $5, and 0 otherwise
trips_df["tip_gt_5"] = 0
trips_df.loc[trips_df.tips > 5, "tip_gt_5"] = 1



#fit logistic regression model with dependent
#variable tip_gt_5 and independent variables
#trip_miles, trip_seconds, extras, airport, and trip_total
model_logit = smf.logit(formula=("tip_gt_5 ~ trip_miles + " +
                                 "extras + trip_total"), data = trips_df).fit()
                                 


#print out the model summary
print ("\nModel summary:  ", model_logit.summary())

