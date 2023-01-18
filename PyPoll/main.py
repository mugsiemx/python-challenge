# Python Challenge - PyPoll

# created on 1/15/2023 by Sheila LaRoue

import os
import csv

candidate_lst = []
election_lst = []
votes_lst = []
votes_pct = []
summary_lst = []

candidate_pct = 0.0
candidate_votes = 0
max_votes = 0
total_votes = 0
idx = 0
max_idx = 0
max_value = 0
tmp_value = 0

candidate = ''
summary_dtl = ''
election_summary = ''
winner = ''

# function to count the number of votes based on one vote per ballot


def vote_count(candidate):
    # total of individual candidate's votes
    candidate_votes = candidate_lst.count(candidate)

    votes_lst.append(str(candidate_votes))
    # percentage of the total vote the candidate received
    candidate_pct = round(float((candidate_votes/total_votes)*100), 3)
    votes_pct.append(candidate_pct)

    summary_dtl = str(candidate) + ': ' + str(candidate_pct) + \
        '% ' + '(' + str(candidate_votes) + ')'
    summary_lst.append(summary_dtl)
    return candidate_votes, votes_lst, votes_pct, summary_lst

    # get the election data file and create the analysis file to write data
election_file = os.path.join('', 'Resources', 'election_data.csv')
analysis_file = os.path.join('', 'analysis', 'analysis_data.txt')

# read the election data file
with open(election_file, 'r') as election_csv:
    election_rdr = csv.reader(election_csv, delimiter=',')
    # skips the first/header row
    election_hdr = next(election_rdr)
    # for each row in the file create a list of only the candidates
    # each ballot line equals one vote, sum vote number upon iteration
    for row in election_rdr:
        candidate_lst.append(row[2])
        total_votes += 1
    # simplify the list of candidates voted for
    for name in candidate_lst:
        if name not in election_lst:
            election_lst.append(name)
    # using a function, calculate the number of votes received per candidate
    for candidate in election_lst:
        idx = int(election_lst.index(candidate))
        if candidate in candidate_lst:
            vote_count(candidate)
   # max_value = votes_lst[0]
max_pct = max(votes_pct)
max_idx = votes_pct.index(max(votes_pct))
winner = election_lst[max_idx]

# on screen header
print('\n' * 3)
print(f'-' * 30)
print(f'Election Results')
print(f'-' * 30)
print(f'Total Votes: {total_votes}')
print(f'-' * 30)
# on screen candidate detail
print(*summary_lst, sep='\n')
print(f"-" * 30)
# on screen print the winning candidate
winner = election_lst[max_idx]
print(f'Winner: {winner}')
# on screen footer
print(f"-" * 30)
print("\n" * 3)

# print results to a text file
with open(analysis_file, 'w') as analysis_txt:
    analysis_txt.write(f'Election Results')
    analysis_txt.write('\n')
    analysis_txt.write(f'-' * 30)
    analysis_txt.write('\n')
    analysis_txt.write(f'Total Votes: {total_votes}')
    analysis_txt.write('\n')
    analysis_txt.write(f'-' * 30)
    analysis_txt.write('\n')

    i = 0
    for i in range(len(summary_lst)):
        analysis_txt.write(summary_lst[i])
        analysis_txt.write('\n')

    analysis_txt.write(f"-" * 30)
    analysis_txt.write('\n')
    analysis_txt.write(f'Winner: {winner}')
    analysis_txt.write('\n')
    analysis_txt.write(f"-" * 30)
