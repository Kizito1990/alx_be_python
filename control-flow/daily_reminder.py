#!/bin/bash

def daily_reminder():
    # Prompt for task description
    task = input("Enter your task: ")

    # Prompt for task priority
    priority = input("Priority (high/medium/low): ").lower()

    # Prompt for whether the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match case to react based on the priority
    match priority:
        case 'high':
            reminder = f"'{task}' is a high priority task"
        case 'medium':
            reminder = f"'{task}' is a medium priority task"
        case 'low':
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = "Invalid priority. Please enter 'high', 'medium', or 'low'."
            print(reminder)
            return  # Exit if invalid priority is entered

    # Modify reminder if the task is time-bound
    if time_bound == 'yes':
        reminder += " that requires immediate attention today!"
    elif time_bound == 'no':
        reminder += " but does not require immediate attention."
    else:
        print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
        return  # Exit if invalid input is entered

    # Print the customized reminder
    print(f"Reminder: {reminder}")

# Call the function
daily_reminder()


