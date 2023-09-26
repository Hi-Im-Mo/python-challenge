#It's just monkeys singing songs, mate. Don't think too hard about it.
import os
import csv

#find the file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#don't get too excited now, cupcake. We need some variables established
total_months = 0
net_profit = 0
current = 0
last_amt = 0
change = 0
change_total = 0
max_increase_amount = 0
max_increase_month = ''
max_decrease_amount = 0
max_decrease_month = ''

#break to scream into the void
#OPEN THE FILE KRONK
with open(budget_data_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        if len(row)==2:
            total_months += 1
            net_profit += float(row[1])
            
            current = float(row[1])
            change = last_amt - current
            change_total += change
            last_amt = float(row[1])
            
            if max_increase_amount < change:
                max_increase_amount = change
                max_increase_month = str(row[0])
            if max_decrease_amount > change:
                max_decrease_amount = change
                max_decrease_month = str(row[0])
        #WHY ISNT THE AVERAGE JUST THE FRICKIN AVERAGE THAT DONT MAKE SENSE
        #This still isnt returning right somehow send help
    
    average = change_total/(total_months-1)

print("Financial Analysis")
#now make it *cute*
print(" ")
print("---------------------")
print(" ")
print(f"Total Months: {total_months}")
print(' ')
print(f"Total: {net_profit}")
print(f"Average Change: {average}")
print(f"Greatest Increase in Profits: {max_increase_month} {max_increase_amount}")
print(f"Greatest Decrease in Profits: {max_decrease_month} {max_decrease_amount}")

#open txt file to write to
with open("output.txt", "a") as f:
#print the results
    print("Financial Analysis", file=f)
#now make it *cute*
    print(" ",file=f)
    print("---------------------",file=f)
    print(" ",file=f)
    print(f"Total Months: {total_months}",file=f)
    print(' ',file=f)
    print(f"Total: {net_profit}",file=f)
    print(f"Average Change: {average}",file=f)
    print(f"Greatest Increase in Profits: {max_increase_month} {max_increase_amount}",file=f)
    print(f"Greatest Decrease in Profits: {max_decrease_month} {max_decrease_amount}",file=f)