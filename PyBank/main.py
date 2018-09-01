# import modules
import os
import csv

# file path across operating systems
csvpath = os.path.join("Resources", "budget_data.csv")

# create empty lists that we will reference for calculations
months = []
revenue = []
change = []

# create and set previous revenue variable
previous_rev = 0

# open and read file
with open(csvpath, newline="") as csvdata:
    read = csv.reader(csvdata, delimiter =",")
    # read header
    header = next(read)

# Loop through rows to populate lists
    for row in read:
        months.append(row[0])
        revenue.append(int(row[1]))
        if previous_rev != 0:
            change.append(int(row[1]) - previous_rev)
        # do not populate first row because it equals zero
        else:
            pass
        # set previous revenue to last row read
        previous_rev = int(row[1])

# calculate total number of months
total_months = len(months)

# calculate net amount of profit/losses over entire period
total_revenue = sum(revenue)

# calculate greatest increase in profits and coresponding month
great_increase = max(change)
# offset corresponding month by +1 due to no change for first row
great_increase_mo = change.index(great_increase) + 1
month_inc = months[great_increase_mo]

#calculate greatest decrease in profits and corresponding month
great_decrease = min(change)
# offset corresponding month by +1 due to no change for first row
great_decrease_mo = change.index(great_decrease) + 1
month_dec = months[great_decrease_mo]

# calculate average change
avg_change = round(sum(change) / len(change))

print(f"""
Financial Analysis
--------------------------------
Total Months: {total_months}
Total: ${total_revenue}
Average Change: ${avg_change}
Greatest Increase in Profits: {month_inc} (${great_increase})
Greatest Decrease in Profits: {month_dec} (${great_decrease})
""")

# file path for output
output = os.path.join("Output/analysis.txt")

# open file for output
with open(output, "w") as target:
    target.write(f"""
Financial Analysis
--------------------------------
Total Months: {total_months}
Total: ${total_revenue}
Average Change: ${avg_change}
Greatest Increase in Profits: {month_inc} (${great_increase})
Greatest Decrease in Profits: {month_dec} (${great_decrease})
""")
# close text file
target.close()
# close csv file
csvdata.close()