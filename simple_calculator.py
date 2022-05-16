print("This is a calculator for you. Please enter the appropriate parameters, thanks")
print("This calculator can only perform operations between 2 numbers please.")
print("")
print("")

def add(a, b):
    print(f"{a} + {b} is {a + b}")

def subtract(a, b):
    print(f"{a} - {b} is {a - b}")

def divide(a, b):
    print(f"{a} / {b} is {a / b}")

def multiply(a, b):
    print(f"{a} * {b} is {a * b}")

def calculate(operation, a, b):
    if operation == "add":
        add(a, b)
    elif operation == "subtract":
        subtract(a, b)
    elif operation == "divide":
        divide(a, b)
    elif operation == "multiply":
        multiply(a, b)
    else:
        print("Please enter a valid operation.")


calculate(
    input("Please enter the operation you would like to perform: add, subtract, divide, multiply"),
    int(input("Please enter the first number: ")),
    int(input("Please enter the second number: "))
)