def name_list():
    print("=== Name List ===")

    # Step 1: Create an empty list
    names = []

    # Step 2: Get 5 names from the user
    for i in range(1, 6):
        name = input(f"Enter name {i}: ")
        names.append(name)

    # Step 3: Print each name and its length
    print("\n--- Names and Their Lengths ---")
    for name in names:
        print(f"{name} ({len(name)} characters)")

# Run the function
if __name__ == "__main__":
    name_list()
