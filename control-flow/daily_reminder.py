
#!/bin/bash

# daily_reminder.py

# Prompt the user for a task description, priority, and if it's time-bound
task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Provide a customized reminder based on the task priority and time sensitivity
match priority:
    case "high":
        reminder = f"Task: {task} is high priority."
    case "medium":
        reminder = f"Task: {task} is medium priority."
    case "low":
        reminder = f"Task: {task} is low priority."
    case _:
        reminder = "Invalid priority entered."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the final customized reminder
print(reminder)

