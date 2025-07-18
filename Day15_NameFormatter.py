def format_name(full_name):
    # Split the name into parts (assuming First and Last)
    parts = full_name.strip().split()

    if len(parts) < 2:
        print("Please enter both first and last name.")
        return

    first = parts[0]
    last = parts[-1]  # Handles middle names too

    # Print various formats
    print("\n--- Name Formats ---")
    print(f"First Last       : {first} {last}")
    print(f"Last, First      : {last}, {first}")
    print(f"Initials         : {first[0].upper()}.{last[0].upper()}.")
    print(f"UPPERCASE        : {full_name.upper()}")
    print(f"lowercase        : {full_name.lower()}")


if __name__ == "__main__":
    user_input = input("Enter your full name (First Last): ")
    format_name(user_input)
