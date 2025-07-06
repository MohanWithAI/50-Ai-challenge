def basic_calculator():
    print("Welcome to the Basic Calculator!")
    
    # Get user input
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    
    # Perform the chosen operation
    if operator == '+':
        result = num1 + num2
        operation = "Addition"
    elif operator == '-':
        result = num1 - num2
        operation = "Subtraction"
    elif operator == '*':
        result = num1 * num2
        operation = "Multiplication"
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operation = "Division"
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return
    
    # Print result
    print(f"\n{operation} Result: {num1} {operator} {num2} = {result}")


# Run the calculator
if __name__ == "__main__":
    basic_calculator()
