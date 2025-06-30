#lab 11 solution 4/17/2025 Larbi Moukhlis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

trips_df = pd.read_json('TaxiTripsWithYearCoding_new.json')
#Create a plot that shows a regression model using the lmplot()
#function that plots the trip_miles values on the x-axis and the
#fare values on the y-axis, using different colors (blue and green)
#for the Post2016 values. 
ax = sns.lmplot(x="trip_miles", y="fare",
                markers=["o", "x"], hue="Post2016",
                palette=["b", "g"],
                data=trips_df, ci=99)

#Display this plot on screen.
plt.show()


#Use the seaborn FacetGrid function to map different values for
#Post2016 into different plots.

FacGr = sns.FacetGrid(data=trips_df, col ="Post2016")
#Use the distplot function to show
#the distribution of the fare variable in each of the plots.
ax = FacGr.map(sns.distplot,"fare")

#Save this plot to a high quality (dpi = 300) jpg file.
plt.savefig("Distrubutions before and after 2016.jpg", dpi=300)


