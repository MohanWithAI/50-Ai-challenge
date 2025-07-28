def format_phone_number(phone):
    # Remove any non-digit characters
    digits = ''.join(filter(str.isdigit, phone))

    # Check if it has exactly 10 digits
    if len(digits) == 10:
        formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
        print(f"Formatted Phone Number: {formatted}")
    else:
        print("❌ Invalid input. Please enter exactly 10 digits.")

if __name__ == "__main__":
    user_input = input("Enter a 10-digit phone number: ")
    format_phone_number(user_input)
