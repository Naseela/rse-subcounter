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

import csv
import pandas as pd
import numpy as np

csvfile = "" # The variable used to store the csv file.
user_dates = {} # Dictionary to store subs and dates.

# Import the csv file into a dictionary using csv library function.
with open("RSE_members.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        user_dates = {row["Email"]:row["Sub date"]}
        print(user_dates)

# Create a data frame from the csv file.
df = pd.read_csv("RSE_members.csv")

# Format the date column
df["Sub Date"]=df["Sub date"].map(lambda x: x.lstrip('0123456789').rstrip())
print (df)
