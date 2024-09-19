#!/bin/bash

# daily_reminder.py

# Prompt the user for a task description
task = input("Enter a task description: ")

# Prompt the user for the task's priority level
priority = input("Enter the priority level (high, medium, low): ").lower()

# Prompt the user if the task is time-sensitive
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task based on priority using a match case statement
match priority:
    case 'high':
        reminder = f"The task '{task}' has a HIGH priority."
    case 'medium':
        reminder = f"The task '{task}' has a MEDIUM priority."
    case 'low':
        reminder = f"The task '{task}' has a LOW priority."
    case _:
        reminder = f"The task '{task}' has an UNDEFINED priority."

# Modify the reminder if the task is time-sensitive
if time_bound == 'yes':
    reminder += " It requires immediate attention today!"

# Print the customized reminder
print(reminder)


