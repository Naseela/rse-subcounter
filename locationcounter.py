#-------------------------------------------------------------------------------
# Name:        Location Mapper
# Purpose:           Show the location of subscribers.
#
# Author:      Naseela Amboorallee
#
# Created:     15/02/2018
# Copyright:   (c) Naseela Amboorallee 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv
import pandas as pd
import numpy as np

# Create a data frame from the csv file.
df = pd.read_csv("RSE_members.csv")

# Create a new data frame column of email domains.
# Function slices to the last three characters and removes leading period.
df["Email domain"]=df["Email"].map(lambda x: x[-3:].lstrip('.'))

df["Domain count"] = df.groupby(df["Email domain"])["Email domain"].transform('count')

# Load information into new data frame.

areadf = df[["Email domain","Domain count"]].copy()

areadf.drop_duplicates(subset="Email domain",inplace=True)


print(areadf)