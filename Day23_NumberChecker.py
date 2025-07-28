def is_positive(n):
    return n > 0

def is_even(n):
    return n % 2 == 0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))

        print("\n--- Number Check Results ---")
        print(f"Positive : {'Yes' if is_positive(num) else 'No'}")
        print(f"Even     : {'Yes' if is_even(num) else 'No'}")
        print(f"Prime    : {'Yes' if is_prime(num) else 'No'}")

    except ValueError:
        print("❌ Invalid input. Please enter a valid integer.")
