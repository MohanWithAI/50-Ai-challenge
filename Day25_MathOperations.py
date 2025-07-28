import math

# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    return math.factorial(n)

# Function to calculate power
def power(base, exponent):
    return base ** exponent

# Function to calculate square root
def square_root(n):
    if n < 0:
        return "Square root not defined for negative numbers"
    return math.sqrt(n)

if __name__ == "__main__":
    print("Choose an operation:")
    print("1. Factorial")
    print("2. Power")
    print("3. Square Root")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        n = int(input("Enter a number for factorial: "))
        print(f"Factorial of {n} = {factorial(n)}")

    elif choice == "2":
        base = float(input("Enter the base: "))
        exp = float(input("Enter the exponent: "))
        print(f"{base} raised to the power {exp} = {power(base, exp)}")

    elif choice == "3":
        n = float(input("Enter a number for square root: "))
        print(f"Square root of {n} = {square_root(n)}")

    else:
        print("❌ Invalid choice. Please select 1, 2, or 3.")
