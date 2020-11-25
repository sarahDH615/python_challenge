import os
import csv

#setting empty list for holding votes/candidate names
votes = []

#path for csv file
csvpath = os.path.join("Resources", "election_data.csv")
#opening csv file w/ reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #for loop for collecting the votes/candidate names, skipping the header row
    for row in csvreader:
        if row[2] == "Candidate":
            continue
        votes.append(row[2])
    
    #creating a dictionary to hold the end summary
    election_dictionary = {}
    #creating an integer from the vote/candidate list to be the total number of votes
    total = (int(len(votes)))
    #subtracting one from the total to represent the index the votes list goes up to
    last_index = total - 1
    #adding top rows to dictionary, including a new header
    election_dictionary["Election Results"] = " "
    election_dictionary["Total Votes"] = total
    election_dictionary["Candidate"] = "percentage of vote", "number of votes"

    #printing top rows and the total votes
    print(f"                         ")
    print("Election Results")
    print(f"_________________________")
    print(f"                         ")
    print(f"Total Votes: {total}")
    print(f"_________________________")

    #alphabetic list of the candidate names w/in votes list
    votes_sorted = sorted(votes)
    #last value is the last name on the list
    last_value = votes_sorted[last_index]

    #creating a counter to hold the number of times a candidate's name appears on the votes list
    counter = 0
    #creating a list that will only hold the unique names of candidates
    cand_list = []

    #for loop to extract candidate names and number of times they appear
    for n in range(0, last_index):
        #if the current candidate name matches the one after it (reaching the end of a one candidate's names)
        if votes_sorted[n] != votes_sorted[n+1]:
            #increment the counter
            counter = counter + 1
            #calculate percentage of total votes
            percentage_votes = round(((counter/total) *100), 2)
            #append name and statistics to the candidate data tuple
            candidate_data = (votes_sorted[n], percentage_votes, counter)
            #append tuple to candidate list
            cand_list.append(candidate_data)
            #create dictionary entry with name as key, % and number of votes as values
            election_dictionary [candidate_data[0]] = candidate_data[1], candidate_data[2]
            #print the name, % and number of votes
            print(f"{votes_sorted[n]}: {percentage_votes}% ({counter})")
            #reset the counter for next candidate name
            counter = 0
        #if current name matches next name -- if w/in a chunk of names
        elif votes_sorted[n] == votes_sorted[n+1]:
            #increment the counter
            counter = counter + 1  
        #if right before last chunk of names (and therefore, the != next name won't trigger at the end of the data)
        elif rfind(votes_sorted[n+1]) == last_index:
            #for the penultimate candidate name, calculate %ages, increment counter, append to list, tuple, dictionary, print (see if statement)
            counter = counter + 1
            percentage_votes = round(((counter/total) *100), 2)
            candidate_data = (votes_sorted[n], percentage_votes, counter)
            cand_list.append(candidate_data)
            election_dictionary [candidate_data[0]] = candidate_data[1], candidate_data[2]
            print(f"{votes_sorted[n]}: {percentage_votes}% ({counter})")
            #leave counter at one to account for last name in list not triggering the final counter add
            counter = 1
    # at end of loop, counter will hold the amount of votes for the last candidate, so calculate %age, append to tuple/list/dict and print
    percentage_votes = round(((counter/total) *100), 2)
    candidate_data = (votes_sorted[n], percentage_votes, counter)
    cand_list.append(candidate_data)
    election_dictionary [candidate_data[0]] = candidate_data[1], candidate_data[2]
    print(f"{votes_sorted[n]}: {percentage_votes}% ({counter})")

    #sort in ascending order the candidate list by third value (index=2) (is votes for the candidate)
    cand_list.sort(key = lambda x:x[2])
    # add entry to dictionary with 'Winner' as key, and first entry on last tuple on candidate list (candidate name w/ highest number of votes)
    election_dictionary ["Winner"] = cand_list[-1][0]

    #print ending sections with Winner named
    print(f"_________________________")
    print(f"                         ")
    print(f"Winner: {cand_list[-1][0]}")
    print(f"_________________________")


#create path to output file
output_path = os.path.join("Analysis", "pypoll_results.csv")

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    #for loop to print a key and value(s) pair from election_dict in each row of the csvwriter
    for key, value in election_dictionary.items():
        csvwriter.writerow([key, value])

    
    