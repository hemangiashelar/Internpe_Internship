import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return x ** y

def logarithm(x, base):
    return math.log(x, base)

print("Welcome to the Simple Scientific Calculator!")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Logarithm")
    print("8. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

    if choice == '8':
        print("Thank you for using the calculator!")
        break

    if choice in ('1', '2', '3', '4', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '6':
            print("Result:", power(num1, num2))
        elif choice == '7':
            base = float(input("Enter the base for logarithm: "))
            print("Result:", logarithm(num1, base))
    elif choice == '5':
        num = float(input("Enter a number: "))
        print("Result:", square_root(num))
    else:
        print("Invalid input. Please enter a valid choice.")