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

import pandas as pd
import numpy as np

# Create a data frame from the csv file.
df = pd.read_csv("RSE_members.csv")

# Format the date column
# Create a new column where the dates contain only the month and year.
# Map function lambda which removes preceeding numerical values from sub dates.
df["Sub month"]=df["Sub date"].map(lambda x: x.lstrip('0123456789').rstrip())

# Count the subscriptions per month.
# Group months and create new column from the amount of times the group appears.
df["Sub count"] = df.groupby(df["Sub month"])["Sub month"].transform('count')

print(df[["Sub month","Sub count"]])

