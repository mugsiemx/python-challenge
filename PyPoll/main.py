# Python Challenge - PyPoll

# created on 1/15/2023 by Sheila LaRoue

import os
import csv

candidate_lst = []
election_lst = []
votes_lst = [0, 0, 0]

candidate_pct = 0
candidate_votes = 0
total_votes = 0
idx = 0

election_summary = ''
candidate = ''

# function to count the number of votes based on one vote per ballot


def vote_count(candidate):
    candidate_votes = candidate_lst.count(candidate)
    votes_lst[idx] = candidate_votes
    return candidate_votes, votes_lst[idx]


# get the election data file and create the analysis file to write data
election_file = os.path.join('', 'Resources', 'election_data.csv')
analysis_file = os.path.join('', 'analysis', 'analysis_data.csv')

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
       # candidate_votes = 0
        idx = int(election_lst.index(candidate))
        if candidate in candidate_lst:
            vote_count(candidate)


# on screen header
print('\n' * 3)
print(f'-' * 30)
print(f'Election Results')
print(f'-' * 30)
print(f'Total Votes: {total_votes}')
print(f'-' * 30)
# on screen detail
idx = 0
for idx in range(len(election_lst[idx])):
    candidate_pct = int(votes_lst[idx])/{total_votes} * 100
    election_summary = (
        f"{election_lst[idx]}: {candidate_pct}% '('{votes_lst[idx]}')'"
    )
    idx += 1
print(election_summary)
# on screen footer
print(f"-" * 30)
print("\n" * 3)
