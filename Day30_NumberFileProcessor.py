def read_numbers_and_calculate(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = []

            for line in file:
                # Split line into individual parts (support space/comma separated)
                parts = line.replace(',', ' ').split()
                for item in parts:
                    if item.strip().isdigit() or (item.strip().lstrip('-').replace('.', '', 1).isdigit()):
                        numbers.append(float(item.strip()))

            if numbers:
                total = sum(numbers)
                average = total / len(numbers)
                print(f"\nFile: {file_path}")
                print(f"Total Numbers: {len(numbers)}")
                print(f"Sum: {total}")
                print(f"Average: {average:.2f}")
            else:
                print("No valid numbers found in the file.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example usage ---
file_path = input("Enter the path to your number file: ")
read_numbers_and_calculate(file_path)
