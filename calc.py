#simple calculator done by Mohamad Hashem
# This function adds two numbers
def add(x, y):
    return x + y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y



while True:

        num1 = float(input("Enter first number: "))
        operator= input("Enter operater : ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operator == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operator == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operator == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
