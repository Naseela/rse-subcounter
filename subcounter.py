#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      rsg
#
# Created:     13/02/2018
# Copyright:   (c) rsg 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv


# Import the csv file into a dictionary using csv library function.
with open("RSE-members.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        user_dates = {row["Email"]:row["Sub date"]}
        print(user_dates)
