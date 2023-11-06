#Import Dependencies
import csv
import os

# Define the variables for Pybank
months = []
profit_loss_changes = []

count_of_months=0
net_profit_loss=0
previous_month_profit_loss=0
greatest_increase=["", 0]
greatest_decrease=["", 9999999999999999999]

#configure play button path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#list the contstants:
CSV_PATH = os.path.join("Resources", "budget_data.csv")
ANALYSIS_PATH=os.path.join("Analysis","results_analysis")

#Retreive the contents of CSV File:
with open(CSV_PATH) as csv_file:
    csvreader = csv.DictReader(csv_file)

     # Define the first value of the Profit/Losses column
    prev_net = int(next(csvreader)["Profit/Losses"])
    copy_of_prev_net = prev_net

#Financial Anlysis: 
#-----------------------------------------------------------------------------------------------
# The total number of months included in the dataset 
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
#-----------------------------------------------------------------------------------------------

    #Loop through each row and count the months
    for row in csvreader:
        
        #Calculate the totals(remember to cast values as int's when applicable)
        count_of_months = count_of_months + 1
        net_profit_loss = net_profit_loss + int(row["Profit/Losses"])

        #Calculate the Profit/Loss Changes
        net_change = int(row["Profit/Losses"]) - prev_net
        prev_net = int(row["Profit/Losses"])
        profit_loss_changes = profit_loss_changes + [net_change]
         
        #Determine the greatest increase:

        if (net_change > greatest_increase[1]):
            greatest_increase[0]=row["Date"]
            greatest_increase[1]=net_change

        #Determine the greatest decrease

        if (net_change < greatest_decrease[1]):
            greatest_decrease[0]=row["Date"]
            greatest_decrease[1]=net_change

#Find the average Profit and Loss Change
profit_loss_average_change = round(sum(profit_loss_changes)/len(profit_loss_changes),2)
count_of_months = count_of_months + 1
net_profit_loss = net_profit_loss + copy_of_prev_net

#Create the Output summary
analysis = (   
f"\nFinancial Analysis\n"
f"------------------------------------------------\n"
f"Total Number of Months : {count_of_months}\n"
f"Total: ${net_profit_loss}\n"
f"Average Change: ${float(profit_loss_average_change)}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
print(analysis)

#Export the results to a text file
with open(ANALYSIS_PATH, "w") as txt_file:
    txt_file.write(analysis)