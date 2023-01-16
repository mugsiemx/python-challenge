# Python Challenge - PyBank

# Analyze a file with profit and loss (p&l) numbers for a number of consecutive months and years. Create a financial analysis to report the total months, total net p&l, total p&l variance from month to month, average p&l change, month and year and amount for the greatest increase and decrease in p&l. Display this information to the screen and output the information to a file.

# created on 1/15/2023 by Sheila LaRoue
# ----------------
# import required  modules
import os
import csv

# get the financial data file, and open a new write file
budget_file = os.path.join("", "Resources", "budget_data.csv")
analysis_file = os.path.join("", "analysis", "analysis_data.csv")

# define list variable
analysis_hdr = ("Total Months", "Total Net Amount", "Total Variance Amount", "Average Change",
                "Greatest Increase in Profits", "Greatest Decrease in Profits", "-", "Financial Analysis")
mon_lst = []
pl_lst = []
pl_var_lst = []
analysis_lst = []

# define and initialize variables to a number zero
(
    pl_tmp, min_idx, max_idx, min_value, max_value,
    total_months,
    total_months_amount,
    total_variance_amount,
    total_avg_change,
) = (0, 0, 0, 0, 0, 0, 0, 0, 0)

# big formatting variables after calcs are made
total_big_increase = ""
total_big_decrease = ""

# open the .cvs file; begin defining and processing the data
with open(budget_file, 'r') as budget_csv:
    budget_rdr = csv.reader(budget_csv, delimiter=",")
    # skips the first/header row
    budget_hdr = next(budget_rdr)
    # into lists:  add count number of months, add profit/loss variances
    for row in budget_rdr:
        mon_lst.append(row[0])
        pl_lst.append(int(row[1]))
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
    # [01] The total number of months included in the dataset
    total_months = len(mon_lst)
    analysis_lst.append(total_months)
    # [02] The net total amount of "Profit/Losses" over the entire period
    total_months_amount = sum(pl_lst)
    analysis_lst.append(total_months_amount)
    # [03] The changes in "Profit/Losses" over the entire period, and then the average of those changes
    total_variance_amount = sum(pl_var_lst)
    analysis_lst.append(total_variance_amount)
    # [04] average
    total_avg_change = round((total_variance_amount/(total_months - 1)), 2)
    analysis_lst.append(total_avg_change)
    # [06] check for largest p & l variance increase month to month
    max_value = max(pl_var_lst)
    max_idx = pl_var_lst.index(max(pl_var_lst))
    # account for list index difference
    total_big_increase = f"{mon_lst[max_idx - 1]} $({pl_var_lst[max_idx]})"
    analysis_lst.append(total_big_increase)
    # [07] check for largest p & l variance decrease month to month
    min_value = min(pl_var_lst)
    min_idx = pl_var_lst.index(min(pl_var_lst))
    # account for list index difference
    total_big_decrease = f"{mon_lst[min_idx - 1]} $({pl_var_lst[min_idx]})"
    analysis_lst.append(total_big_decrease)

# on screen header
print("\n" * 3)
print(f"{analysis_hdr[-2]}" * 30)
print(f"{analysis_hdr[-1]}")
print(f"{analysis_hdr[-2]}" * 30)
# on screen detail
print(f"{analysis_hdr[0]}: {analysis_lst[0]}")
print(f"{analysis_hdr[1]}: ${analysis_lst[1]}")
print(f"{analysis_hdr[2]}: ${analysis_lst[2]}")
print(f"{analysis_hdr[3]}: ${analysis_lst[3]}")
print(f"{analysis_hdr[4]}: {total_big_increase}")
print(f"{analysis_hdr[5]}: {total_big_decrease}")
# on screen footer
print(f"{analysis_hdr[-2]}" * 30)
print("\n" * 3)

# ready to output the data; initialize the output file
with open(analysis_file, 'w') as analysis_csv:
    analysis_wtr = csv.writer(analysis_csv, delimiter=",")
    # write two rows
    analysis_wtr.writerow(analysis_hdr[0:6])    # write the first/header row
    analysis_wtr.writerow(analysis_lst)         # write the second row of data
