# Simple Calculator Program
# This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.
# It also maintains a history of all calculations performed during the session.

import sys

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# List to store calculation history
history = []

# Main function to run the calculator
def main():
    print("Welcome to the Simple Calculator!")
    print("Available operations: +, -, *, /")
    print("Type 'history' to view calculation history.")
    print("Type 'exit' to quit the program.")
    print()

    while True:
        # Get operation from user
        op = input("Enter operation (+, -, *, /, history, exit): ").strip().lower()

        if op == 'exit':
            print("Goodbye!")
            break

        if op == 'history':
            if history:
                print("Calculation History:")
                for i, calc in enumerate(history, 1):
                    print(f"{i}. {calc}")
            else:
                print("No calculations in history yet.")
            print()
            continue

        if op not in ['+', '-', '*', '/']:
            print("Invalid operation. Please choose +, -, *, /, history, or exit.")
            continue

        # Get numbers from user
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        # Perform calculation
        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)

        # Display result
        print(f"Result: {result}")

        # Add to history
        history.append(f"{a} {op} {b} = {result}")
        print()

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()