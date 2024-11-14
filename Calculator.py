# DSC510
# Programming Assignment Week 5
# Sarah Theriot
# 7/2/2024

# Calculator

# Define functions

def performCalculation(operation):
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        if operation == "+":
            if number1 == 0:
                print("Error: Addition with zero not allowed.")
                return
            if number2 == 0:
                print("Error: Addition with zero not allowed.")
                return
            result = number1 + number2
        if operation == "-":
            if number1 == 0:
                print("Error: Subtraction with zero not allowed.")
                return
            if number2 == 0:
                print("Error: Subtraction with zero not allowed.")
                return
            result = number1 - number2
        if operation == "*":
            if number1 == 0:
                print("Error: Multiplication by zero not allowed.")
                return
            if number2 == 0:
                print("Error: Multiplication by zero not allowed.")
                return
            result = number1 * number2
        if operation == "/":
            if number1 == 0:
                print("Error: Division by zero not allowed.")
                return
            if number2 == 0:
                print("Error: Division by zero not allowed.")
                return
            result = number1 / number2
        else:
            print("Error: Please enter a valid operation (+, -, *, /).")
            return

        print(f"The result of {number1} {operation} {number2} = {result}")
    except ValueError:
        print("Error: Please enter a valid number.")


def calculateAverage():
    try:
        totalNumbers = int(input("Enter the total number of numbers you want to input: "))

        if totalNumbers <= 0:
            print("Error: Number must be greater than 0.")
            return

        total = 0
        for i in range(totalNumbers):
            number = float(input(f"Enter the number: {i + 1}: "))
            total += number

        average = total / totalNumbers
        print(f"The average of the {totalNumbers} numbers is: {average}")

    except ValueError:
        print("Error: No numbers entered, please enter valid numbers.")


def main():
    while True:
        print("Welcome to Calculator Buddy!")
        print("Please select an action to be performed:")
        print("1. Perform Calculation (+, -, *, /)")
        print("2. Calculate Average")
        print("3. Exit")

        choice = input("Enter your choice: (1, 2, or 3) ")

        if choice == "1":
            operation = input("Enter the operation: (+, -, *, /)")
            performCalculation(operation)
        elif choice == "2":
            calculateAverage()
        elif choice == "3":
            print("Exiting Calculator Buddy!")
            break
        else:
            print("Error: Please enter a valid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
