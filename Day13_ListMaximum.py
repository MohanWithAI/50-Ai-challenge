def find_maximum(num_list):
    if not num_list:
        print("The list is empty.")
        return None

    # Assume the first element is the largest
    largest = num_list[0]

    # Compare with each element
    for num in num_list[1:]:
        if num > largest:
            largest = num

    print(f"The largest number in the list is: {largest}")
    return largest


if __name__ == "__main__":
    # Example list; you can also use input if needed
    numbers = [42, 17, 68, 99, 23, 11]
    find_maximum(numbers)
