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

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        op = input("Enter an operation (+, -, *, /, ^): ")
        num2 = float(input("Enter the second number: "))

        if op == '+':
            result = add(num1, num2)
            print(f'{num1} + {num2} = {result}')
        elif op == '-':
            result = subtract(num1, num2)
            print(f'{num1} - {num2} = {result}')
        elif op == '*':
            result = multiply(num1, num2)
            print(f'{num1} * {num2} = {result}')
        elif op == '/':
            result = divide(num1, num2)
            print(f'{num1} / {num2} = {result}')
        elif op == '^':
            result = power(num1, num2)
            print(f'{num1} ^ {num2} = {result}')
        else:
            print("Invalid operation. Please use +, -, *, /, or ^.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
