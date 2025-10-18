# a python function to add two numbers
def add_numbers(a, b):
    return a + b
# a python function to subtract two numbers
def subtract_numbers(a, b):
    return a - b
# a python function to multiply two numbers
def multiply_numbers(a, b):
    return a * b
# a python function to divide two numbers
def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b   
# a python function to calculate the power of a number
def power_numbers(a, b):
    return a ** b 
# a python function for modulo operation
def modulo_numbers(a, b):
    return a % b
# an interactive command line program to ask the user for two numbers and an operation
def calculator():
    print("Welcome to the calculator!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")

    while True:
        choice = input("Enter the number of the operation (1-6) or 'q' to quit: ")
        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print("Result:", add_numbers(num1, num2))
        elif choice == '2':
            print("Result:", subtract_numbers(num1, num2))
        elif choice == '3':
            print("Result:", multiply_numbers(num1, num2))
        elif choice == '4':
            print("Result:", divide_numbers(num1, num2))
        elif choice == '5':
            print("Result:", power_numbers(num1, num2))
        elif choice == '6':
            print("Result:", modulo_numbers(num1, num2))
# Uncomment the line below to run the calculator when this script is executed
# calculator()  