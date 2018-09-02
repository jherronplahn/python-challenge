# import modules
import os
import csv

# file path for input
csvpath = os.path.join("Resources", "election_data.csv")

# create empty list that will hold candidate names (each time they appear in data)
candidates = []

# create variable for total votes and set to zero
total_votes = 0

# open and read file
with open(csvpath, newline="") as csvdata:
    read = csv.reader(csvdata, delimiter=",")
    # read header
    header = next(read)

# loop through rows of data and create list of each time candidate appears
    for row in read:
        candidates.append(row[2])

total_votes = len(candidates)

# create a set for a unique list of candidates
canset = {*candidates}

# create empty list for loop results - will hold: (can) (can_percent) (can_votes) for each candidate
results = []
# create an empty dictionary for loop results to calculate winner - will hold: key(can): value(can_votes)
votes_win = {}

# retrieve candidate data 
for can in canset:
    can_votes = candidates.count(can)
    can_percent = round((can_votes/total_votes) * 100)
    # populate list
    results.append(f"{can}: {can_percent}% ({can_votes})")
    # populate dictionary
    votes_win.update({can:can_votes})

# # caluclate and print winner
winner = max(votes_win, key=votes_win.get)

# file path for output
output = os.path.join("Output", "results.txt")

# open and write to text file
with open(output, "w") as target:
    target.write(f"""
Election Results
---------------------
Total Votes: {total_votes}
---------------------""")
    target.write("\n")
    target.write("\n".join(results)) #this format replaces list comma delimiter with new line
    target.write(f"""
---------------------
Winner: {winner}
---------------------
""")

#open, read and print text file to terminal
with open(output, "r") as target:
    print(target.read())

# close text file
target.close()
# close csv file
csvdata.close()