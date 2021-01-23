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

This project consists of four sub-projects, all using python scripts to analyse a source csv/txt file, print results to the terminal (save for pyboss), and (for all save pyparagraph) output a new csv containing the analysis results. 
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
            - for loop to write each key-value pair in bank_dictionary as a row in a csv (pybank_results.csv)    
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
            - for loop to write each key-value pair in election_dictionary as a row in a csv (pypoll_results.csv)
- pyboss:
    - goal ouput:

        a. splitting 'Name' column in source csv into 'First Name' and 'Last Name' columns

        b. re-formatting birth-date column into MM/DD/YYYY

        c. hiding the first 5 numbers in the Social Security Number column

        d. using State abbreviations instead of full State name


    - procedure:
        - importing dependencies and source csv (employee_data.csv)
        - finding the goal outputs:
            - creating variables for goal outputs: lists to hold the employee IDs (empIDlist), employee full names, dates of birth, and Social Security Numbers after being split (name_split, date_split, ssn_split), first and last names of employees (first_name_list, second_name_list), dates in MM/DD/YYY format (date_mdy), edited Social Security Numbers (ssn_starred), and State abbreviations (state_abbrev_list); and a dictionary with the United States State abbreviations (us_state_abbrev) 
            - for loop to append values to list empIDlist, to split names, dates, and Social Security Numbers, append them to their respective lists (name_split, date_split, ssn_split), edit the values as needed, then append them to final lists (first_name_list, second_name_list, date_mdy, ssn_starred), and look up state names in the us_state_abbrev dictionary, and append abbreviations to the state_abbrev_list
            - zipping the lists together (info_zip) and making a combined list (info_zip_list)
        - outputting the results as a csv
            - using csv.writer to append each item in the info_zip_list as a row in a csv (new_employee_data.csv)      
