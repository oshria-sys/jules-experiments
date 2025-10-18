def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    return a % b

if __name__ == "__main__":
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '^': power,
        '%': modulo
    }

    try:
        num1 = float(input("Enter the first number: "))
        op_symbol = input(f"Enter an operation ({', '.join(operations.keys())}): ")
        num2 = float(input("Enter the second number: "))

        if op_symbol in operations:
            operation_func = operations[op_symbol]
            result = operation_func(num1, num2)
            print(f'{num1} {op_symbol} {num2} = {result}')
        else:
            print(f"Invalid operation. Please use one of: {', '.join(operations.keys())}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
