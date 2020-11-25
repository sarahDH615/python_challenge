import os
import csv

#lists to hold values from months: col1(row[0]) and profits/losses: col2(row[1])
#variables to hold max inc/dec, set to zero
#dictionary for storing summary at end
#dictionary entry header
months = []
money_made = []
max_inc = 0
max_dec = 0
bank_dictionary = {}
bank_dictionary ["Financial Analysis"] = " "


#csv file path
csvpath = os.path.join("Resources", "budget_data.csv")
#opening csv file w/ reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #for loop to collect the months and money info
    for row in csvreader:
        #skip headers w/ continue
        #if not header, append the month to months list
        if row[0] == "Date":
            continue
        months.append(row[0])
        if row[1] == "Profit/Losses":
            continue
        #if not header, append the money to money list
        money_made_int = int(row[1])
        money_made.append(money_made_int)
        #wrap row[1] in integer cast so it can be compared to numerical values
        #add money to max_inc/_dec depending on whether they are greater or less than zero/last max value
        #retrieve row[0] for the current max value
        if int(row[1]) > max_inc:
            max_inc = int(row[1])
            max_inc_month = row[0]
        if int(row[1]) < max_dec:
            max_dec = int(row[1])
            max_dec_month = row[0]
    

#print starting info
print("                   ")
print("Financial Analysis:")
print("______________________________________")    
print("                   ")

#make an integer out of the length of the months list
months_total = int(len(months))
#add entry to dictionary for total months
#print total months
bank_dictionary ["Total Months"] = months_total
print(f"Total Months: {months_total}")

#sum money made list
net_total = sum(money_made)
#add entry to dictionary for net total
#print net total
bank_dictionary ["Net Total"] = net_total
print(f"Net Total: ${net_total} ")

#calc avg change, round it to 2 decimal places
avg_change = round((net_total/months_total), 2)
#add entry to dictionary for avg change
#print avg change
bank_dictionary ["Average Change"] = avg_change
print(f"Average Change: ${avg_change}")

#add entries to dictionary for max_inc/_dec and their months
#print max_inc/_dec and months
bank_dictionary ["Greatest Increase in Profits"] = max_inc_month, max_inc
print(f"Greatest Increase in Profits: {max_inc_month} (${max_inc})")
bank_dictionary ["Greatest Decrease in Profits"] = max_dec_month, max_dec
print(f"Greatest Decrease in Profits: {max_dec_month} (${max_dec})")

#print end info
print("                   ")
print("______________________________________")    
print("(End of 'Financial Analysis'")
print("                   ")

#create a path for output file, open it
output_path = os.path.join("Analysis", "pybank_results.csv")

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    #for loop to print a key and value(s) pair from bank_dict in each row of the csvwriter
    for key, value in bank_dictionary.items():
        csvwriter.writerow([key, value])