# Homework 3: Python
# Python Challenge #2: PyPoll
#
# I created a Python script to create an efficient and modern voting system, 
# as I was tasked with this in order to help a small, rural town modernize its 
# vote counting process, by using several python functions.
# Make sure to run the script from the right directory for the relative path to work.

# Import modules
import os
import csv
import numpy

# Create path for csv and output
election_csv = os.path.join("Resources","election_data.csv")
output_path = os.path.join("Analysis","results.txt")

# Function to calculate percentage
def percents(array,totalv,outarray):
    for i in range(len(array)):
        percents = (array[i]/totalv)*100
        outarray.append(percents)

# Define initial variables
candidates = []
votes = []
percentages = []
counter = 0
votenum = 0

# Open file and calculate values, skip header
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:
        voteid = str(row[0])
        county = str(row[1])
        candidate = str(row[2])

        # Count total votes
        counter = counter + 1

        # Get candidate names
        if candidate not in candidates:
            candidates.append(candidate)
            votes.append(0)
        
        # Get votes for each candidate
        for i in range(len(candidates)):         
            if candidates[i] == candidate:
                votes[i] = votes[i] + 1

    # Calculate percentages
    percents(votes,counter,percentages)
    # Round percentages
    final_percent = numpy.around(percentages)

    # Calculate winner with most votes
    mostvoted = max(votes)
    for i in range(len(candidates)):
        if votes[i] == mostvoted:
            winner = candidates[i]
    
    # Display final values
    print(f"Election Results")
    print(f"_________________________")
    print(f"Total Votes: {counter}")
    print(f"_________________________")
    print(f" ")
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {final_percent[i]}% ({votes[i]})")
    print(f"_________________________")
    print(f" ")
    print(f"Winner: {winner}")

# Create txt file with results
with open(output_path, 'w', newline='') as txtfile:
    print(f"Election Results",file=txtfile)
    print(f"_________________________",file=txtfile)
    print(f"Total Votes: {counter}",file=txtfile)
    print(f"_________________________",file=txtfile)
    print(f" ",file=txtfile)
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {final_percent[i]}% ({votes[i]})",file=txtfile)
    print(f"_________________________",file=txtfile)
    print(f" ",file=txtfile)
    print(f"Winner: {winner}",file=txtfile)
    