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



principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)



num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

sum_result = num1 + num2

print(f"The sum of {num1} and {num2} is {sum_result}")



num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

