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

# Remove all duplicate domain counts.
areadf.drop_duplicates(subset="Email domain",inplace=True)

print(areadf["Email domain"])

id
# Create a lookup table in the form of a dictionary.
location = {"uk":"United Kingdom","org":"Unkwown","com":"Unkwown","edu":"Unknown",
            "ie":"Ireland","et":"Ethiopia" ,"fr":"France" ,"ca":"Canada",
            "au":"Australia","dk":"Denmark","ch":"Switzerland","se":"Sweden",
            "gov":"America","ac":"United Kingdom","no":"Norway","me":"Montenegro",
            "io":"Unknown","za":"South Africa","it":"Italy","nz":"New Zealand",
            "us":"United States","kr":"South Korea","eu":"Europe","int":"Unknown",
            "fi":"Finland","nl":"Netherlands","be":"Belgium","at":"Austria",
            "pl":"Poland","tw":"Taiwan","mu":"Mauritius","scot":"Scotland"}