def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    while b == 0:
        print("Cannot divide by zero!")
        b = float(input("Enter a non-zero second number: "))

    return a / b


while True:
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you for using Calculator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = add(num1, num2)

    elif choice == "2":
        result = subtract(num1, num2)

    elif choice == "3":
        result = multiply(num1, num2)

    elif choice == "4":
        result = divide(num1, num2)

    print("Result:", result)