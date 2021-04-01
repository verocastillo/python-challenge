# Homework 3: Python
# Python Challenge #1: Py Bank
#
# I created a Python script for analyzing the financial records of a company
# from a csv file. It calculates the total profits/losses and the average
# change, as well as displaying the months, greatest increase and decrease.

# Import modules
import os
import csv

# Create path for csv
bank_csv = os.path.join('/Users/vero1296/Documents/BOOTCAMP_2021/github/python-challenge/PyBank/Resources/budget_data.csv')
output_path = os.path.join('/Users/vero1296/Documents/BOOTCAMP_2021/github/python-challenge/PyBank/Analysis/results.txt')

# Define initial variables
counter = 0
net_total = 0
prev_profit = 0
prev_change = 0
months = []
changes = []

# Open file and calculate values, skip header
with open(bank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:
        # Define variable
        month = str(row[0])
        profit = int(row[1])
        
        # Count each row for each month
        counter = counter + 1

        # Sum total net profit/losses
        net_total = net_total + profit

        # Calculate change between past value and current value
        # Change is zero if equal
        if prev_profit != 0:
            mchange = profit - prev_profit 
            months.append(month)
            changes.append(mchange)     
            # Define next value to compare if
        else:
            mchange = 0
        
        # Values for new loop
        prev_profit = int(row[1])
        prev_change = mchange
        
    # Calculate average change, max and min values
    avg_change1 = sum(changes)/len(changes)
    gincrease = max(changes)
    gdecrease = min(changes)
    incmonth = months[changes.index(gincrease)]
    decmonth = months[changes.index(gdecrease)]
    
    # Display values
    print(f"Financial Analysis")
    print(f"___________________________")
    print(f"Total Months: {counter}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${avg_change1}")
    print(f"Greatest Increase in Profits: {incmonth} (${gincrease})")
    print(f"Greatest Decrease in Profits: {decmonth} (${gdecrease})")

# Create txt file with results
with open(output_path, 'w', newline='') as txtfile:

    print(f"Financial Analysis",file=txtfile)
    print(f"___________________________",file=txtfile)
    print(f"Total Months: {counter}",file=txtfile)
    print(f"Total: ${net_total}",file=txtfile)
    print(f"Average Change: ${avg_change1}",file=txtfile)
    print(f"Greatest Increase in Profits: {incmonth} (${gincrease})",file=txtfile)
    print(f"Greatest Decrease in Profits: {decmonth} (${gdecrease})",file=txtfile)
