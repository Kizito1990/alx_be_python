
#!/bin/bash
def perform_operation(num1: float, num2: float, operation: str):
    num1 = float(input("Enter first number: "))
    operation = input("Enter the operation 'add', 'subtract', 'divide', 'multiply': ")
    num2 = float(input("Enter second number:"))

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "DIVISION_BY_ZERO"
        return num1 / num2
    else:
        return "INVALID_OPERATION"

result = perform_operation()
print(f"results: {result}")


