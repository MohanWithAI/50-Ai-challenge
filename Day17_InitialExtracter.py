def extract_initials(full_name):
    # Split the full name into individual words
    name_parts = full_name.strip().split()

    # Extract the first letter from each part, capitalize it, and add a dot
    initials = '.'.join([part[0].upper() for part in name_parts]) + '.'

    print(f"Initials: {initials}")

if __name__ == "__main__":
    user_input = input("Enter your full name: ")
    extract_initials(user_input)
