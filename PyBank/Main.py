import os
import csv

#Set path for the budget data CSV file
budget_data_csv = os.path.join('..','PyBank','Resources','budget_data.csv')

#Initialize variables
total_months = 0
net_total = 0
prev_profit = 0
profit_changes = []
months = []

#Read the CSV file
with open(budget_data_csv)as csvfile:
 csvreader = csv.reader(csvfile, delimiter =",")

#Read the header row
 csv_header = next(csvreader)

#Loop through the rows in the CSV file
 for row in csvreader:

#Calculate the total number of months
  total_months = len(months)+ 1

 #Count the total amount of "Profit/Losses"
  net_total += int(row[1])

#Calculate the change in profit from the previous month
  profit_change = int(row[1]) - prev_profit
  prev_profit = int(row[1])
  profit_changes.append(profit_change)
  months.append(row[0])

#Calculate the average change in profits
 a = sum(profit_changes[1:])
 b = len(profit_changes[1:])
 if b == 0:
  print("Cannot divide by zero")
 else:
  (a/b)

#Find the greatest increase and decrease in profits
max_increase = max(profit_changes)
max_decrease = min(profit_changes)
max_increase_month = months[profit_changes.index(max_increase)]
max_decrease_month = months[profit_changes.index(max_decrease)]

#Print the analysis results to the terminal
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${(a/b):2f}")
print(f"Greatest Increase in Profits: {max_increase_month}(${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_month}(${max_decrease})")          

#Export the analysis results to a text file
output_file = os.path.join('..','PyBank','analysis','Financial_analysis.txt')
with open(output_file,'w') as txtfile:
 txtfile.write("Financial Analysis\n")
 txtfile.write("-------------------------------- ")

 txtfile.write(f"Total Months: {total_months}\n")
 txtfile.write(f"Total:${net_total}\n")
 txtfile.write(f"Average Change:${(a/b):2f}\n")
 txtfile.write(f"Greatest Increase in Profits: {max_increase_month}(${max_increase})\n")
 txtfile.write(f"Greatest Decrease in Profits: {max_decrease_month}(${max_decrease})\n")

