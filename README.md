# python_challenge

### Contains:
- pybank:
    - analysis
        - pybank_results.csv (data output)
    - resources
        - budget_data.csv (source data)
    - main.py (script)
- pypoll
    - analysis
        - pypoll_results.csv (data output)
    - resources
        - election_data.csv (source data)
    - main.py (script)
- pyboss
    - employee_data.csv (source data)
    - new_employee_data.csv (data output)
    - pybossconversion.py (script)
- pyparagraph
    - paragraph_3.txt (text sample)
    - txt_analysis.py (script)
### Description

This project consists of four sub-projects, all using python scripts to analyse a source csv/txt file, print results to the terminal, and (for all save pyparagraph) output a new csv containing the analysis results. 
- pybank:
    - goal ouput:

        a. total number of months

        b. net total profits/losses

        c. changes in profits/losses

        d. greatest increase in profits, and the date and amount of that occurrence

        e. greatest decrease in profits, and the date and amount of that occurrence

    - procedure:
        - importing dependencies and source csv (budget_data.csv)
        - finding the goal outputs:
            - creating variables for goal outputs: lists to hold month names (months), money made for each month (money_made), profits made each month (profit_change_list); variables, set to zero, for greatest increase/decrease in profits (max_inc, max_dec), and a dictionary (bank_dictionary) to hold all the above variables for eventual output to a csv
            - for loop to append values to lists months and money_made (towards goals a, b)
            - for loop on money_made list to determine profits across each month, and append to proft_change_list (towards goal c)
            - setting the sum of the profit_change_list as the total change in profits (total_change), and the length of the profit_change_list (number_of_changes) (towards goal c)
            - for loop on profit_change_list to find the maximum increase and decrease in profits over the time period (achieving goals d, e)
        - printing the results to the terminal
            - print statements of variables to appear in the terminal
            - doing some final analysis within the print statement: taking the length of the months list (achieving goal a), taking the sum of the money_made list (achieving goal b), and dividing total_change by number_of_changes (achieving goal c)
            - appending variables to bank_dictionary
        - outputting the results as a csv
            - for loop to write each key-value pair in bank_dictionary as a row in a csv    
- pypoll:
    - goal ouput:

        a. total number of votes

        b. list of candidates voted for

        c. percentage of votes for each candidate

        d. total number of votes for each candidate

        e. winner of election by popular vote

    - procedure:
        - importing dependencies and source csv (election_data.csv)
        - finding the goal outputs and printing results to the terminal:
            - creating variables for goal outputs: list to hold votes/candidate names (votes) and dictionary (election_dictionary) to hold the variables for eventual export to a csv
            - for loop to append values to list votes (towards all goals)
            - setting variable total equal to length of the votes list (achieving goal a)
            - creating counter, a list for holding tuples of candidate data (cand_list), sorting votes list, finding the index length of the votes list, in preparation for another for loop (towards goals b-e)
            - for loop on votes_sorted list with conditionals to determine where votes_sorted changes from one candidate to another, calculating percentage of votes, number of votes, and candidate name, printing those results to the terminal, and saving them to election_dictionary (towards goals b-d)
            - finding the data for the last candidate from the filled lists after the close of the for loop (achieving goals b-d)
            - sorting the tuples in cand_list by values for number of votes to find the greatest share of votes, then assigning the candidate name with the greatest share of votes as the winner (achieving goal e)
        - outputting the results as a csv
            - for loop to write each key-value pair in election_dictionary as a row in a csv    
