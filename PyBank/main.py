#It's just monkeys singing songs, mate. Don't think too hard about it.
import os
import csv

#find the file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#don't get too excited now, cupcake. We need some variables established
total_months = 0
net_profit = 0
month_values = []
max_increase = 0
min_increase = 0

#break to scream into the void
#OPEN THE FILE KRONK
with open(budget_data_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        if len(row)==2:
            total_months += 1
            net_profit += float(row[1])
            month_values.append(row[1])
            

#print the results
print("Financial Analysis")
#now make it *cute*
print(" ")
print("---------------------")
print(" ")
print(f"Total Months: {total_months}")
print(' ')
print(f"Total: {net_profit}")
