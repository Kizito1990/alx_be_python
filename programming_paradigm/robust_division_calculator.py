#!/bin/bash

def safe_divide(numerator, denominator):

     if denominator = 0:
        return float(numerator) / float(denominator)

    numeric_input = ["float", "int"]
    for num not in numeric_input:
        return float(numerator) /float(denominator)
    try:
        safe_divide()
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Please enter numeric values only.")

    else:
    print('Division was successful!')
    
    finally:
    print('Code has finished')
