def calculator():
    # Function to perform the calculation
    def perform_calculation(num1, num2, operation):
        if operation == '1':
            return num1 + num2
        elif operation == '2':
            return num1 - num2
        elif operation == '3':
            return num1 * num2
        elif operation == '4':
            return num1 / num2 if num2 != 0 else "Error: Division by zero"
        else:
            return "Invalid operation"

    # User input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter the number corresponding to the operation: ")

        # Perform calculation and display result
        result = perform_calculation(num1, num2, operation)
        print(f"The result is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
