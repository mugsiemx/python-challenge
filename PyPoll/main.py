# Python Challenge - PyPoll

# created on 1/15/2023 by Sheila LaRoue

import os
import csv

election_lst = []
votes_lst = []
candidate_lst = []

x = 0
candidate_votes = 0
total_votes = 0
idx = 0
candidate = ''


def vote_count(candidate_lst[]):
    candidate_votes = candidate_lst.count(candidate)
    return election_lst.count(candidate_votes)


# get the election data file
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

    for name in candidate_lst:
        if name not in election_lst:
            election_lst.append(name)

    for candidate in range(len(election_lst)):
        if candidate in candidate_lst:
            election_lst[idx] = candidate_votes

           #  c_votes = (candidate_votes[idx]) + 1
           #  candidate_votes[idx] = c_votes

print(election_lst)
print(candidate_votes)
print(candidate_lst)

# i = 0

#     election_rdr = csv.reader(election_csv, delimiter=',')
#     # skip past the header row
#     election_hdr = next(election_rdr)

#     for row in election_rdr:  # [19719:19728]:
#         candidate_lst = list(election_rdr)
#         for row in candidate_lst:
#             if candidate <> candidate_lst[row]
#                 candidate = candidate_lst[row]
