def sum_calculator():
    print("=== Sum Calculator ===")

    try:
        n = int(input("Enter a positive integer (n): "))
        
        if n < 1:
            print("Please enter a number greater than or equal to 1.")
            return

        total_sum = 0
        for i in range(1, n + 1):
            total_sum += i

        print(f"The sum of numbers from 1 to {n} is: {total_sum}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    sum_calculator()
