import os
import csv

#variables
empIDlist = []
name_split = []
first_name_list = []
second_name_list = []
date_mdy = []
ssn_starred = []
state_abbrev_list = []

date_split = []

ssn_split = []

info_edited = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#csv file path
csvpath = os.path.join("employee_data.csv")
#opening csv file w/ reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #skipping the header
    csv_header = next (csvreader)

    for row in csvreader:
        empID = row[0]
        #creating a list for IDs, no changes needed
        empIDlist.append(empID)

        #splitting the row with the name at the space, holding each name as a variable, appending to first and second name new lists
        name_split = row[1].split(" ")
        first_name = name_split[0]
        second_name = name_split[1]
        first_name_list.append(first_name)
        second_name_list.append(second_name)

        #splitting date by dashes, holding each section as a variable, combining them using slashes into a new list
        date_split = row[2].split("-")
        months = date_split[1]
        days = date_split[2]
        years = date_split[0]
        date_mdy.append(f"{months}/{days}/{years}")

        #splitting ssn by dashes, taking the last 4 digits, appending them to new list with stars
        ssn_split = row[3].split("-")
        ssn_last4 = ssn_split[2]
        ssn_starred.append(f"***-**-{ssn_last4}")

        #looking up state in the dictionary, appending to new list with abbreviations
        state_key = row[4]
        state_abbrev = us_state_abbrev[state_key]
        state_abbrev_list.append(state_abbrev)

    #zipping all the lists together
    info_zip = zip(empIDlist, first_name_list, second_name_list, date_mdy, ssn_starred, state_abbrev_list)
    info_zip_list = list(info_zip)

    #creating a header row    
    employee_header = ['Employee ID', 'Name', 'DOB', 'SSN', 'State']
    
    #creating path to output csv
    data_output = os.path.join("new_employee_data.csv")

    with open (data_output, "w", newline = "") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')

        #writing header row
        csvwriter.writerow(employee_header)

        #writing rows as entries in the zip
        csvwriter.writerows(info_zip_list)