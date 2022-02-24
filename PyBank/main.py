
print("Financial Analysis by Alex Liu")

print("------------------------------")

# Import the pathlib and csv library

from pathlib import Path
import csv

# Set the file path

csvpath = Path("./budget_data.csv")
outputnom = []

with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # discard the header line
    
    header = next(csvreader)
    
    number_of_months = nom = 0

    pnl_list = []
    
    all_dates = []
    
    for row in csvreader:
        date = row[0]
        pnl = int(row[1]) # convert str --> int
        pnl_list.append(pnl)
        all_dates.append(date)
        nom += 1 
        outputnom.append(nom)
        
# The total number of months included in the dataset.

total_no_months = len(outputnom)

print(f'The total number of months included in the dataset is {total_no_months}')

# The net total amount of Profit/Losses over the entire period.

net = sum(pnl_list)

print(f'The net total amount of Profit/Losses over the entire period is ${net}')

# The average of the changes in Profit/Losses over the entire period.

average = (sum(pnl_list)/len(outputnom))

print(f'Average of the changes in Profit/Losses over entire period is ${average:.2f}')

# The greatest increase in profits (date and amount) over the entire period.

greatest_increase_profit = max(pnl_list)

profit_index_pnl = pnl_list.index(max(pnl_list))

profit_index_date = pid = all_dates[profit_index_pnl]

print(f'The greatest increase in profits was on {pid} with ${greatest_increase_profit}')

# The greatest decrease in losses (date and amount) over the entire period.

greatest_decrease_loss = min(pnl_list)

loss_index_pnl = pnl_list.index(min(pnl_list))

loss_index_date = lid = all_dates[loss_index_pnl]

print(f'The greatest decrease in losses was on {lid} with ${greatest_decrease_loss}')