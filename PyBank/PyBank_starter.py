# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
monthly_changes = [] #(Xpert)
monthly_changes = [] #(Xpert)
previous_profit_loss = None #(Xpert)
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit_loss = int(first_row[1])
    
    # Track the total and the net change
    for row in reader:
        total_months += 1
        current_profit_loss = int(row[1]) #(Xpert)
        total_net += current_profit_loss #(Xpert)
        # Calculate the change
        change = current_profit_loss - previous_profit_loss #(Xpert) (Google)
        monthly_changes.append(change) #(Xpert)
        #print (greatest_increase)
        # Calculate the greatest increase in profits (month and amount)
        if change > greatest_increase:
            greatest_increase = change #(Xpert)
            greatest_increase_date = (row[0])
            #print (greatest_increase_date)
        # Calculate the greatest decrease in losses (month and amount)
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = (row[0])
        # Update previous_profit_loss for the next iteration
        previous_profit_loss = current_profit_loss

# Calculate the average net change across the months
if monthly_changes: #(Xpert)
    average_change = sum(monthly_changes) / len(monthly_changes) #(Xpert)
else: #(Xpert)
    average_change = 0 #(Xpert)

# Generate the output summary
output = ( #(Xpert) 
    "Financial Analysis\n" #(Xpert)
    "-------------------\n" #(Xpert)
    f"Total Months: {total_months}\n" #(Xpert)
    f"Total: ${total_net}\n" #(Xpert)
    f"Average Change: ${average_change:.2f}\n" #(Xpert)
    f"Greatest Increase in Profits: {greatest_increase_date} {greatest_increase} \n" #(Xpert)
    f"Greatest Decrease in Profits: {greatest_decrease_date} {greatest_decrease} \n" #(Xpert)
)

# Print the output
print(output)

# Calculate the net total amount of "Profit/Losses"
# net_total = financial_data['Profit/Losses'].sum()

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


