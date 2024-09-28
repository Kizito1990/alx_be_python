#!/bin/bash
# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date (after {days} days): {formatted_future_date}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")

# Main function to run both parts
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

