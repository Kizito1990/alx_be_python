#!/bin/bash

def safe_divide(numerator, denominator):

     if denominator = 0:
        return numerator / denominator

    numeric_input = ["float", "int"]
    for num not in numeric_input:
        return numerator / denominator
    try:
        safe_divide()
    
    except ZeroDivisionError:
        print('Cannot divide by zero')

    except ValueError:
        print('Cannot divide str value')

    else:
    print('Division was successful!')
    
    finally:
    print('Code has finished')
