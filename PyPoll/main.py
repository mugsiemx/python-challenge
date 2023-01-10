# Python Challenge - PyPoll

# created on 1/7/2023 by Sheila LaRoue

import os
import csv
# from itertools import islice

# get the financial data file
cfile = os.path.join('..', 'Resources', 'budget_data.csv')

row_count = 0
# read the financial data file
with open(cfile, encoding='utf') as csvfile:
    rfile = csv.reader(cfile, delimiter=',')

# analyze the records to make calculations:
with open("rfile") as PollCalcs:
    for line in PollCalcs:
        if row_count < 10:
            print(line)
row_count += 1


# for row in budget_rdr to row[5]:
#    if row[0] != " ":
#       print(row[0])
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
#
