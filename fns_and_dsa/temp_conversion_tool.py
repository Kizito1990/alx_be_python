# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR\s*=\s*9\/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def get_temperature_input():
    """Prompts the user to input temperature and checks for valid numeric input."""
    try:
        temp = float(input("Enter the temperature value: "))
        return temp
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    print("Temperature Conversion Tool")
    choice = input("Is the temperature in (C)elsius or (F)ahrenheit? ").strip().upper()

    try:
        if choice == 'C':
            celsius = get_temperature_input()
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        elif choice == 'F':
            fahrenheit = get_temperature_input()
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        else:
            print("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

