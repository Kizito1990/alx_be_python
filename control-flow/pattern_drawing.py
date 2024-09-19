#!/bin/bash

# pattern_drawing.py

# Prompt the user to enter a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# Use a while loop to iterate through each row of the pattern
while row < size:
    # Use a for loop to print asterisks for each row
    for col in range(size):
        print("*", end="")
    
    # Print a newline after each row to move to the next line
    print()
    
    # Increment the row counter
    row += 1



