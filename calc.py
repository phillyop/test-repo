import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero!"
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of a negative number!"
    else:
        return math.sqrt(x)

def logarithm(x, base):
    if x <= 0 or base <= 0:
        return "Error! Both arguments must be positive."
    else:
        return math.log(x, base)

def factorial(x):
    if x < 0:
        return "Error! Cannot compute factorial of a negative number!"
    else:
        return math.factorial(x)

print("Welcome to the Scientific Calculator!")
print("Enter 'exit' to quit.")

while True:
    operation_input = input("Enter operation (add/subtract/multiply/divide/power/sqrt/log/factorial): ")

    if operation_input.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break

    if operation_input.lower() in ('add', 'subtract', 'multiply', 'divide', 'power'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation_input.lower() == 'add':
            print("Result:", add(num1, num2))
        elif operation_input.lower() == 'subtract':
            print("Result:", subtract(num1, num2))
        elif operation_input.lower() == 'multiply':
            print("Result:", multiply(num1, num2))
        elif operation_input.lower() == 'divide':
            print("Result:", divide(num1, num2))
        elif operation_input.lower() == 'power':
            print("Result:", power(num1, num2))

    elif operation_input.lower() in ('sqrt', 'log', 'factorial'):
        num = float(input("Enter a number: "))

        if operation_input.lower() == 'sqrt':
            print("Result:", square_root(num))
        elif operation_input.lower() == 'log':
            base = float(input("Enter the base for logarithm: "))
            print("Result:", logarithm(num, base))
        elif operation_input.lower() == 'factorial':
            print("Result:", factorial(int(num)))

    else:
        print("Invalid operation.")
