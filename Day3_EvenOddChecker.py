def is_even(number):
    return number % 2 == 0

def check_single_number():
    num = int(input("Enter a number to check if it's even or odd: "))
    if is_even(num):
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

def check_list_of_numbers():
    numbers = input("Enter a list of numbers separated by spaces: ")
    num_list = [int(n) for n in numbers.split()]

    print("\nEven/Odd check for the list:")
    for num in num_list:
        status = "Even" if is_even(num) else "Odd"
        print(f"{num} is {status}")

if __name__ == "__main__":
    print("=== Even or Odd Checker ===")
    check_single_number()
    print("\n--- Now checking a list of numbers ---")
    check_list_of_numbers()
