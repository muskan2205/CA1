writing a python code a simple calculator
def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    match choice:
        case '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        case '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        case '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        case '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Cannot divide by zero.")
        case _:
            print("Invalid input.")

calculator()

