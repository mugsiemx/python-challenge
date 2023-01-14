# Python Challenge - PyBank

# created on 1/7/2023 by Sheila LaRoue

import os
import csv

# import datetime

# get the financial data file
budget_file = os.path.join("", "Resources", "budget_data.csv")

# define variables
c = ": "  # used for a better view on screen
analysis_hdr = ("Total Months", "Total Net Amount", "Average Change",
                "Greatest Increase in Profits", "Greatest Decrease in Profits")
mon_lst = []
pl_lst = []
analysis_lst = []

total_avg_change = 0
total_big_increase = 0
total_big_decrease = 0

with open(budget_file, 'r') as budget_csv:
    budget_rdr = csv.reader(budget_csv, delimiter=",")
    # skips the first/header row
    budget_hdr = next(budget_rdr)
    #
  #  budget_df = list(budget_rdr)
   # total_months = len(budget_rdr)

    # total_month_amount = budget_df['Profit\Losses'].sum()

    for row in budget_rdr:
        mon_lst.append(int(row[1]))
        pl_lst.append(int(row[1]))
        print(pl_lst)
    for i enumerate pl_lst
    analysis_lst[i] += pl_lst
    print(analysis_lst)

   # for i in range(len((analysis_lst[i+1])-(analysis_lst[i])))
   # pl_lst.append((pl_lst[i+1]=profit[i]))

    # sum_months = budget_df["Profit/Losses"].sum(axis=1)
    # pl_lst.append(row)
    #  for column in budget_df[]:
    #     mon_amt = budget_df.ilocindex[i]

    # print(pl_lst)

    # amount += amount

print(
    f"Total months is: {total_months}. {pl_lst}. My list is: {analysis_lst}.")


# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
#
