def compare_numbers():
    print("=== Number Comparison ===")

    # Get two numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Compare numbers
        if num1 > num2:
            print(f"{num1} is greater than {num2}.")
        elif num1 < num2:
            print(f"{num1} is smaller than {num2}.")
        else:
            print(f"Both numbers are equal ({num1} = {num2}).")

    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    compare_numbers()
