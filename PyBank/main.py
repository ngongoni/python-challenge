#import file

import os
import csv

#path to the csvfile

csvpath = os.path.join('budget_data.csv')

#initializing the variables 
total_months = 0
total_revenue =0
changes =[]
date_count = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0

# Open the CSV
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)
# calculating the total number of months and total revenue
    previous_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]

    for row in csvreader:
 
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        # Calculate change from this month to previous months
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])
        
        #calculating the greatest increase
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]
            
        #calculating the greatest decrease
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_month = row[0]  
      
    # calculating the average and date
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    # printing all values
    print("Financial Analysis")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_revenue))
    print('Average Change: ${:.2f}'.format(average_change))
    print(f"Greatest increase in profits: Feb-2012 {greatest_inc_month}, ${max(changes)}")
    print(f"Greatest decrease in profits: Sep-2013 {greatest_dec_month}, ${min(changes)}")

# HEAD
    # writing output files

    
# de204e9898626d9e3a7f41e0238b32c04ea7bfeb
    PyBank = open("output.txt","w+")
    PyBank.write("Financial Analysis") 
    PyBank.write('\n' +"Total Months" + str(total_months)) 
    PyBank.write('\n' +"Total Amount" + str(total_revenue)) 
    PyBank.write('\n' +"Average" + str(average_change)) 
    PyBank.write('\n' +greatest_inc_month) 
    PyBank.write('\n' +str(high))
    PyBank.write('\n' +greatest_dec_month) 
    PyBank.write('\n' +str(low))     
        