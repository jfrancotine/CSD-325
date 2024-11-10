#Jose Franco
#11/08/2024
#Assignment 4.2 - High/Low Temperatures
#Brownfield development on an existing program written to display temperatures. 

import csv
from datetime import datetime
#Import sys to help end program.
import sys
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

#Load the data from csv file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Getting dates, highs and lows from this csv file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)


#This is a function to display the temperature plot
def plot_temperatures(dates, temperatures, label, color):
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)

    #Format plot using a label to show what the user is asking to be displayed.
    plt.title(f"Daily {label} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    #Show plot
    plt.show()

#Display instructions for the user to understand how to use the program.
print("Welcome to the Temperature Visualization Program!")
print("Instructions:")
print("You can view the daily high or low temperatures for 2018 by selecting an option from the menu.")
print("1 - High Temperatures: Displays a graph of daily high temperatures.")
print("2 - Low Temperatures: Displays a graph of daily low temperatures.")
print("3 - Exit: Close the program.\n")

#Main menu loop for selecting highs, lows, or exit the program.
while True:
    print("Select an option:")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        print("Displaying high temperatures...\n")
        plot_temperatures(dates, highs, "high", 'red')
    elif choice == '2':
        print("Displaying low temperatures...")
        plot_temperatures(dates, lows, "low", 'blue')
    elif choice == '3':
        print("Thank you for using the High/Low temperature program. Have a good rest of your day!")
        sys.exit()
    #Input validation to make sure an integer and either 1, 2 or 3 is entered as an option.
    else:
        print("Invalid choice. Please select 1, 2, or 3.\n")
