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

pl_tmp = 0
total_months = 0
total_months_amount = 0
total_avg_change = 0
total_big_increase = 0
total_big_decrease = 0

with open(budget_file, 'r') as budget_csv:
    budget_rdr = csv.reader(budget_csv, delimiter=",")
    budget_hdr = next(budget_rdr)
    # skips the first/header row
    # into lists:  add count number of months, add profit/loss values
    for row in budget_rdr:
        mon_lst.append(row[0])
        pl_lst.append(int(row[1]))

    i = 0
    j = 1
    for i in range(len(pl_lst)):
        if i == 0 or j == len(mon_lst):
            analysis_lst.append(0)
        else:
            pl_tmp = (int(pl_lst[i]))-(int(pl_lst[j]))
            analysis_lst.append(pl_tmp)
        j += 1

    total_months = len(mon_lst)
    total_months_amount = sum(pl_lst)

    # if
    # total_months = [pl_lst].count()
    # total_months_amount = [pl_lst].sum()
    #  analysis_lst[i].append([pl_lst[i]-pl_tmp[1]])
    #  pl_tmp == (int(row[1]))

    #    analysis_lst.append
#        print(pl_lst)
    # for i, v enumerate(pl_lst):
    #     if i != 0:
    #         analysis_lst[i] = analysis_lst[i].append.pl_lst[i]
    #     print(analysis_lst)

# for i in range(len((analysis_lst[i+1])-(analysis_lst[i])))
# pl_lst.append((pl_lst[i+1]=profit[i]))

# sum_months = budget_df["Profit/Losses"].sum(axis=1)
# pl_lst.append(row)
#  for column in budget_df[]:
#     mon_amt = budget_df.ilocindex[i]

# print(pl_lst)

# amount += amount


print(f"MONTHS {mon_lst}")
print(f"BASIC {pl_lst}")
print(f"CALCULATIONS {analysis_lst}")
print(f"SINGLE {total_months}")
print(f"SINGLE {total_months_amount}")


# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
#
