def count_numbers(num_list):
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for num in num_list:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    # Display results
    print("=== Count Results ===")
    print(f"Positive numbers: {positive_count}")
    print(f"Negative numbers: {negative_count}")
    print(f"Zeroes: {zero_count}")


if __name__ == "__main__":
    # Example list; you can also take input from user
    numbers = [3, -1, 0, 7, -5, 0, 2, -8, 4]
    count_numbers(numbers)
