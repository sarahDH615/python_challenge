import os
import csv

#lists to hold values from months: col1(row[0]) and profits/losses: col2(row[1])
#variables to hold max inc/dec, set to zero
#dictionary for storing summary at end
#dictionary entry header
months = []
money_made = []
profit_change_list = []
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
        #wrap row[1] in integer cast so it can be compared to numerical values
        money_made_int = int(row[1])
        money_made.append(money_made_int)
        
    #creating variable to hold the length of the money_made list to input into range    
    list_length = int(len(money_made))

    #creating a for loop over the money_made list, comparing each element with the previous element
    for x in range(1, list_length):
        profit_change = money_made[x] - money_made[x-1]
        #appending the changes in each month's profit to a list
        profit_change_list.append(profit_change)
    
    #finding the sum of all the changes in profit (numerator in avg change)   
    total_change = sum(profit_change_list)
   
    #creating another variable to hold the length of the profit_change_list (denominator in avg change)
    number_of_changes = int(len(profit_change_list)) 
    
    #creating a for loop to identify the max_inc and max_dec of profits
    for y in range(0, number_of_changes):
        if int(profit_change_list[y]) > max_inc:
            max_inc = int(profit_change_list[y])
            #creating value to hold the index of the max value in the profit_change_list
            maxIindex = y
        if int(profit_change_list[y]) < max_dec:
            max_dec = int(profit_change_list[y]) 
            #creating value to hold the index of the max value in the profit_change_list
            maxDindex = y

    #adding 1 to max indices because the months list is one entry longer
    miiforrow = maxIindex + 1
    mdiforrow = maxDindex + 1

    #variables to hold the months for max values
    max_inc_month = months[miiforrow]
    max_dec_month = months[mdiforrow]


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
avg_change = round((total_change/number_of_changes), 2)
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