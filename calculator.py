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

    operations = {
        '1': ('Add', add_numbers),
        '2': ('Subtract', subtract_numbers),
        '3': ('Multiply', multiply_numbers),
        '4': ('Divide', divide_numbers),
        '5': ('Power', power_numbers),
        '6': ('Modulo', modulo_numbers)
    }

    print("Select an operation:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    while True:
        choice = input(f"Enter the number of the operation (1-{len(operations)}) or 'q' to quit: ")
        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in operations:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                _, operation_func = operations[choice]
                result = operation_func(num1, num2)
                print("Result:", result)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
        else:
            print("Invalid choice. Please try again.")

# Uncomment the line below to run the calculator when this script is executed
# calculator()