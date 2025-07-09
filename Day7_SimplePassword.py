def password_check():
    print("=== Simple Password Checker ===")

    # Define minimum password length
    min_length = 8

    # Get password input
    password = input("Enter your password: ")

    # Check password length
    if len(password) >= min_length:
        print("✅ Password is valid.")
    else:
        print(f"❌ Password is too short. Minimum length is {min_length} characters.")

if __name__ == "__main__":
    password_check()
