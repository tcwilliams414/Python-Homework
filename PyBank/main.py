import os
import csv

# Create a path for our csv file
budget_data.csv_path = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open (budget_data.csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter= ",")

# Read the header row first
csv_header= next(csv_reader)

# Initialize variables outside of for loop
months_count= 0
current_profit=0
net_total_profit= 0
monthly_changes= []

#Read through each row of data after header to get the total number of months in data set

for row in csv_reader:
    months_count+=1
    print(months_count)

# The net total amount of "Profit/Losses" over the entire period
    current_profit= int(row[1])
    net_total_profit+= current_profit
    print(net_total_profit)

# The average change in "Profit/Losses" from month to month
    current_monthly_profit= int(row[1])
    monthly_profit_change= current_monthly_profit - previous_monthly_profit

#  Monthly profit changes in a montly list
    monthly_changes.append(monthly_profit_change)

# Average change in profit
    average_change_profit= (monthly_profit_change/months_count)

# Greatest decrease in profit and greatest increase in profit look through monthly_changes list created
    greatest_decrease_profit = min(monthly_changes)
    greatest_increase_profit = max(monthly_changes)

    lowest_month= monthly_changes.index(greatest_decrease_profit)
    highest_month= monthly_changes.index(greatest_increase_profit)

    print("Financial Analysis")
    print (f"Total Months: {months_count}")
    print (f" Total: {net_total_profit}")
    print (f" Average Change: {average_change_profit}")
    print(f" Greatest Increase in Profits {highest_month},{greatest_increase_profit}")
    print (f"Greatest Decrease in Profits {lowest_month}, {greatest_decrease_profit}")