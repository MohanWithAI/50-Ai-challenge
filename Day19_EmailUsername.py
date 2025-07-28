def extract_username(email):
    if "@" in email:
        username = email.split("@")[0]
        print(f"Username: {username}")
    else:
        print("Invalid email address. Please include '@' symbol.")

if __name__ == "__main__":
    user_input = input("Enter your email address: ")
    extract_username(user_input)
