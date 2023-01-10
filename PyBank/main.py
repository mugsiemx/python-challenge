# Python Challenge - PyPoll

# created on 1/7/2023 by Sheila LaRoue

import os
import csv
# import datetime

# get the financial data file
budget_file = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# define variables
c = ": "  # used for a better view on screen
analysis_hdr = ("Total Months", "Total Net Amount", "Average Change",
                "Greatest Increase in Profits", "Greatest Decrease in Profits")
total_rows = 0
total_months_amount = 0
total_avg_change = 0
total_big_increase = 0
total_big_decrease = 0

with open(budget_file, 'r') as budget_csv:
    budget_rdr = csv.reader(budget_csv, delimiter=",")
    budget_hdr = next(budget_rdr)   # skips the first/header row

 #   total_rows_ck = (sum(1 for row in budget_rdr))
 #   print(total_rows_ck)
    for row in budget_rdr:
        total_months_amount += int(row[1])
    print(f"Total amount is: {total_months_amount}")


# total_avg_change == total_months_amount/total_rows_ck
#
# print(f"{total_months_amount} {total_avg_change}")

# if int(row[1]) != 0:  # and row < total_rows_ck + 1:
# total_months_amount == total_months_amount + int(row[1])
#  if int(row[1]) == 382539:
#    print(f"{total_months_amount}")


# for row in budget_rdr to row[5]:
#    if row[0] != " ":
#       print(row[0])
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
#
