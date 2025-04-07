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
# BMI Calculator
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))


bmi = weight / (height ** 2)


print(f"Your BMI is: {bmi:.2f}")


if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")

