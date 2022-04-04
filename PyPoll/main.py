import os
import csv

# Create a path for our csv file
election_data.csv_path= os.path.join("..", "Resources", "election_data.csv")

# Open and read csv
with open (election_data.csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter= ",")

# Read the header row first
csv_header= next(csv_reader)

# Initialize variables outside of for loop
votes_count= 0
candidate_list= []
Charles_Casper= []
Charles_Casper_votes= 0
Diana_DeGette = []
Diana_DeGette_votes = 0
Raymon_Anthony = []
Raymon_Anthony_votes= 0

#Read through each row of data after header to get the total number of ballot ids in data set
    for row in cvs_reader:
        votes_count+=1
        print(votes_count)

# Store list of candidates
        candidate_list.append(row[2])
        print(candidate_list)

    for candidate in candidate_list:
        if candidate == "Charles Casper Stockham": 
            Charles_Casper.append(candidate_list)
            Charles_Casper_votes= len(Charles_Casper) 

        elseif candidate == "Raymon Anthony Doane":
            Raymon_Anthony.append(candidate_list) 
            Raymon_Anthony_votes= len(Raymon_Anthony)     
        
        else candidate== "Diana DeGette":
            Diana_DeGette.append(candidate_list)
            Diana_DeGette_votes= len(Diana_DeGette)
    

#Percentage of votes for each candidate
Charles_Casper_percentage = (Charles_Casper_votes/votes_count)* 100
Raymon_Anthony_percentage = (Raymon_Anthony_votes/ votes_count)* 100
Diana_DeGette_percentage = (Diana_DeGette_votes/votes_count)* 100

# Declare winner
    if Charles_Casper_percentage > max(Raymon_Anthony_percentage, Diana_DeGette_percentage):
        winner = "Charles Casper Stockham"
    elif Raymon_Anthony_percentage > max(Charles_Casper_percentage, Diana_DeGette_percentage):
        winner= "Raymon Anthony Doane"
    else:
        winner = "Diana DeGette"    


print(f"Total Votes: {votes_count}")
print(f" Charles Casper Stockham: {Charles_Casper_percentage}")
print(f"Diana DeGette : {Diana_DeGette_percentage} ")
print(f"Raymon Anthony Doane: {Raymon_Anthony_percentage}")