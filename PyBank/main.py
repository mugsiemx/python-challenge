# Python Challenge - PyBank

# created on 1/7/2023 by Sheila LaRoue

import os
import csv

# import datetime

# get the financial data file
budget_file = os.path.join("", "Resources", "budget_data.csv")

# define variables
c = ": "  # used for a better view on screen
analysis_hdr = ("Total Months", "Total Net Amount", "Total Variance Amount", "Average Change"
                "Greatest Increase in Profits", "Greatest Decrease in Profits")
mon_lst = []
pl_lst = []
pl_var_lst = []
analysis_lst = []

pl_tmp = 0
min_idx = 0
max_idx = 0
min_value = 0
max_value = 0
total_months = 0
total_months_amount = 0
total_variance_amount = 0
total_avg_change = 0
# total_big_increase = f"{mon_lst} {[analysis_lst[min_idx]]}"
# total_big_decrease = f"{mon_lst} {[analysis_lst[max_idx]]}"
# open the .cvs file; begin defining and processing the data
with open(budget_file, 'r') as budget_csv:
    budget_rdr = csv.reader(budget_csv, delimiter=",")
    # skips the first/header row
    budget_hdr = next(budget_rdr)
    # into lists:  add count number of months, add profit/loss variances
    for row in budget_rdr:
        mon_lst.append(row[0])
        pl_var_lst.append(int(row[1]))
    # find the profit and loss variances, record them in the ProfitLoss Variance List
    i = 0
    j = 0
    for i in range(len(pl_lst)):
        if i == 0:
            # do nothing at the first value, keep moving
            continue
        else:
            # next variance less the previous variance
            pl_tmp = (int(pl_lst[i]))-(int(pl_lst[j]))
            pl_var_lst.append(int(pl_tmp))
        j += 1
# match analysis values with the initial analysis header list defined in the variables
    # The total number of months included in the dataset
    total_months = len(mon_lst)
    analysis_lst.append(total_months)
    # The net total amount of "Profit/Losses" over the entire period
    total_months_amount = sum(pl_lst)
    analysis_lst.append(total_months_amount)
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    total_variance_amount = sum(pl_var_lst)
    analysis_lst.append(total_variance_amount)
    # average
    total_avg_change = sum(pl_var_lst)/(len(mon_lst - 1))
    analysis_lst.append(total_avg_change)
    # check for largest increase month to month p & l variance
    max_value = max(pl_var_lst)
    analysis_lst[4] = pl_var_lst.index(max_value)
    # check for largest decrease month to month p & l variance
    min_value = min(pl_var_lst)
    analysis_lst[5] = pl_var_lst.index(min_value)

print(f"MONTHS {mon_lst}")
print(f"BASIC {pl_lst}")
print(f"CALCULATIONS {analysis_lst}")
print(f"SINGLE {total_months}")
print(f"SINGLE {total_months_amount}")
print(f"SINGLE {total_avg_change}")
print(f"SINGLE {total_big_increase}")
print(f"SINGLE {total_big_decrease}")


# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
#
