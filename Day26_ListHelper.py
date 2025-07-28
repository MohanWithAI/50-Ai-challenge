def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return find_sum(numbers) / len(numbers)

if __name__ == "__main__":
    try:
        input_str = input("Enter numbers separated by spaces: ")
        num_list = [float(x) for x in input_str.split()]

        print("\n--- List Statistics ---")
        print(f"Maximum : {find_max(num_list)}")
        print(f"Minimum : {find_min(num_list)}")
        print(f"Sum     : {find_sum(num_list)}")
        print(f"Average : {find_average(num_list):.2f}")

    except ValueError:
        print("❌ Please enter only numeric values.")
