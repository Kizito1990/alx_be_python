#!/bin/bash

# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR  # Access global variable
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR  # Access global variable
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Function to handle user input and conversion
def get_temperature_input():
    try:
        temp = input("Enter the temperature: ")

        # Validate that the input is numeric
        if not temp.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temp = float(temp)  # Convert input to float
        scale = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if scale == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is equivalent to {converted_temp:.2f}°F")
        elif scale == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is equivalent to {converted_temp:.2f}°C")
        else:
            raise ValueError("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"Error: {e}")

# Main program loop
if __name__ == "__main__":
    get_temperature_input()

