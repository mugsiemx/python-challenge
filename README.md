# python-challenge

# Unit 3 Homework: Python

- Using GitHub created a new repository for this project called 'python-challenge' and cloned the repository to my computer.
- Using the Terminal, created directories within this repository called 'PyBank' and 'PyPoll";

  - to each of these directories, added folders  
    'Resources' and 'analysis' and files main.py
  - files budget_data.csv and election_data.csv were copied via a windows process to their respective PyBank and PyPoll directories

- Somewhere in the process, changes were pushed to GitHub; adds, commits, and push commands were done with the GitBash terminal

## PyBank

- Using the Python csv reader python, created a python file to perform financial analasis of the file budget_data.csv to pull out the following as per the README.md file included with the homework assignment:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

\*\* PLUS added an extra line for the total profit and loss variance amount

- The changes in "Profit/Losses" over the entire period, and then the average of those changes

- The greatest increase in profits (date and amount) over the entire period

- The greatest decrease in profits (date and amount) over the entire period

\*\* The program begins with a small paragraph of comments to explain the purpose of the program, import modules, open two .csv files for reading and writing.

- define list variables, define number variables and set to a value of zero, define string variables

- append the month list and profit_loss list to contain the data from the budge_data file for python processing

- calculate the profit change keeping in mind the list will be shorter due to no calculation for the first profit_loss value

\*\* to add to the analysis list for screen display and file writing at the end of the program, perform the following:

- calculate the total months included in the data
- sum the net profit and loss total amount
- sum the total profit and loss variance
- calculate the average change over the month to month variances
- using the minimum and maximum functions determine the biggest increase/decrease in the list

\*\* display Financial Analysis to screen

- print the header to screen with a few blank lines preceeding the data and a line of dashes both before and after the header
  -print the detail financial information on the next six lines of the screen and a line of dashes to close the output

\*\* create analysis file and write two rows to it

- write the header row from the analysis header list
- write the detail row from the detail analysis list

## PyBank
