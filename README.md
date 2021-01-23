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
        1. total number of months
        2. net total profits/losses
        3. changes in profits/losses
        4. greatest increase in profits, and the date and amount of that occurrence
        5. greatest decrease in profits, and the date and amount of that occurrence
    - procedure:
        - importing dependencies and source csv
        - finding the goal outputs:
            - for loop to append months and the amount of money made
            - for loop to determine profits across each month
            - variables for total profit over the time period, and number of changes over the time period
            - for loop to find the maximum increase and decrease in profits over the time period
        - printing the results to the terminal
        - outputting the results as a csv    
