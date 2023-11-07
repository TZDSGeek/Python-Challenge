# Import the Dependencies
import csv
import os

# set the file path for the "play button"
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# List the contstants:
CSV_PATH=os.path.join("Resources","election_data.csv")
ANALYSIS_PATH=os.path.join("Analysis","results_analysis.txt")

# Define the variables
total_votes = 0
candidate_votes = {}
candidates = []
winning_count_of_votes = 0

# Retrieve the contents of the CSV File:
with open(CSV_PATH) as csv_file:
    csv_reader=csv.reader(csv_file)

# Read the header row
    row_headers = next(csv_file)

# Election Analysis: 
#-----------------------------------------------------------------------------------------------
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote
#-----------------------------------------------------------------------------------------------

    # Loop through each row and count the votes
    for row in csv_reader:

        # Calculate the total votes
        total_votes = total_votes + 1

        # Retrieve the candidate name from each row
        candidate_name = row[2]

        #Determine if all candidates are included in the list of candidates, and add the ones missing
        if (candidate_name not in candidates):
            candidates.append(candidate_name)

        # Track the count of votes for the added candidate
            candidate_votes[candidate_name] = 0

        # begin aggregating the votes per candidate
        candidate_votes[candidate_name] += 1
    
# Create the Output summary for the Total votes,print to the termnial, and write the results in the text file    
with open(ANALYSIS_PATH,"w") as txt_file:
    total = (
        f"Election Results\n\n"
        f"------------------------------\n"
        f"\nTotal Votes: {total_votes}\n\n"
        f"------------------------------\n\n"
    )

    print(total)
    txt_file.write(total)

    # Determine the winner by creating a second loop, to loop through all candidates
    for x in candidate_votes:

        # Calculate the total number and percentage of votes each candidate won
        votes_per_candidate = candidate_votes.get(x)
        vote_percentage = (float(votes_per_candidate)/float(total_votes)*100)

         #Create the Output Summary, print the result to the terminal, and write in the text file        
        votes_per_candidate_summary =(f"{x}: {vote_percentage:.3f}% ({votes_per_candidate})\n\n")
        print(votes_per_candidate_summary)
        txt_file.write(votes_per_candidate_summary)

        # Determine the Winning candidate and number of votes recieved
        if(votes_per_candidate > winning_count_of_votes):
            winning_count_of_votes = votes_per_candidate
            winning_candidate = x

    #Create the output for the winning cadndiate, print the result to the terminal, and write in the text file
    winner=(
        f"------------------------------\n\n"
        f"\nWinner: {winning_candidate}\n\n\n"
        f"------------------------------\n\n")  
    print(f'Winner: {winning_candidate}')
    txt_file.write(winner)


    







