#%%
import os
import csv

# Path to collect data from the Resources folder
wrestling_csv = 'C://Users/josrh/Desktop/Stuff/ClassRepo/Module-8/wrestling_functions/Resources/WWE-Data-2016.csv'
# Define the function and have it accept the 'wrestlerData' as its sole parameter
def print_percentages(wrestlerData):
    Name = wrestlerData[0]
    Wins = int(wrestlerData[1])
    Losses = int(wrestlerData[2])
    Draws = int(wrestlerData[3])
# Find the total number of matches wrestled
    total = Wins + Losses + Draws
# Find the percentage of matches won
    percent_won = Wins / total * 100
# Find the percentage of matches lost
    percent_lost = Losses / total * 100
# Find the percentage of matches drawn
    percent_draw = Draws / total * 100
# Super or Not?
    if Losses < 50:
        status = 'Superstar'
    else:
        status = 'Jobber'
# Print out the wrestler's name and their percentage stats
    print(f'Stats for {Name}\n'
            f'WIN PERCENT: {percent_won}\n'
            f'LOSS PERCENT: {percent_lost}\n'
            f'DRAW PERCENT: {percent_draw}\n'
            f'{Name} is a {status}')
# Read in the CSV file
continues = 'y'
while continues == 'y':
    with open(wrestling_csv, 'r') as csvfile:

        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')

        # Prompt the user for what wrestler they would like to search for
        name_to_check = input("What wrestler do you want to look for? ")

        # Loop through the data
        for row in csvreader:
            # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
            if(name_to_check == row[0]):
                print_percentages(row)


        continues = input('Do you wish to continue? (y/n)')
        if continues == 'n':
            break

# %%
