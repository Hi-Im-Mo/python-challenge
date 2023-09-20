#It's just monkeys singing songs, mate. Don't think too hard about it.
import os
import csv

#find the file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#don't get too excited now, cupcake. We need some variables established
total_months = 0
net_profit = 0
month_changes = []
max_increase = 0
min_increase = 0
#current_month ?????????????????????
#should this be in a function so i can like... establish columns??

#break to scream into the void
#OPEN THE FILE KRONK
with open(budget_data_csv, 'r') as csvfile:
    