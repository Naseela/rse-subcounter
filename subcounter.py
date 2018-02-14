#-------------------------------------------------------------------------------
# Name: Subscription Counter
# Purpose: Calculate the number of subscriptions made each month.
#
# Author:      rsg
#
# Created:     13/02/2018
# Copyright:   (c) rsg 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a data frame from the csv file.
df = pd.read_csv("RSE_members.csv")

# Format the date column
# Create a new column where the dates contain only the month and year.
# Map function lambda which removes preceeding numerical values from sub dates.
df["Sub month"]=df["Sub date"].map(lambda x: x.lstrip('0123456789').rstrip())

# Convert string into datetime data type then format and overwrite column.
df["Month"]=pd.to_datetime(df["Sub month"])
df["Month"]=df["Month"].dt.strftime('%m/%Y')

# Count the subscriptions per month.
# Group months and create new column from the amount of times the group appears.
df["Sub count"] = df.groupby(df["Month"])["Month"].transform('count')

# Removes all duplicate rows from the data frame.
df.drop_duplicates(subset="Month", inplace=True)

# Create a new data frame containing only the necessary columns.
subdf = df[["Month","Sub count"]].copy()

print (subdf)
# Export the new data frame into a csv file.
subdf.to_csv('Subscription_count.csv')

# Plot data into line graph with setttings
subdf.plot(x="Month", y="Sub count", kind='line', title="Subscriptions per Month", legend=False, color="r")

# Format settings on axis.
plt.xticks(range(len(subdf)),df["Month"],size="small",rotation=270)

plt.xticks(np.arange(0,len(subdf)+1, 1.0))
plt.xlabel("Month")
plt.ylabel("Subscriptions")
plt.tight_layout()

# Export to png file.
plt.savefig("Subscription_count.png")

# Create a new column for the cumulative sum in the sub data frame.
subdf["Total"]= subdf["Sub count"].cumsum()

# Create a new data frame from the sub data frame with desire columns.
cumdf = subdf[["Month","Total"]].copy()


# Plot a graph of the total subscribers.
cumdf.plot(x="Month",y="Total",kind='line', title="Total Subscribers",legend=False,color="b")


# Format the graph and axis.
plt.xticks(range(len(cumdf)),cumdf["Month"],size="small",rotation=270)
plt.xlabel("Month")
plt.ylabel("Total Subscribers")

plt.tight_layout()

# Export data frame into image.
plt.savefig("Total_subs.png")

print(cumdf)