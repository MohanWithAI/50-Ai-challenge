def capitalize_string(text):
    return text.capitalize()

def reverse_string(text):
    return text[::-1]

def count_characters(text):
    return len(text)

if __name__ == "__main__":
    user_input = input("Enter a string: ")

    print("\n--- String Helper Results ---")
    print(f"Capitalized : {capitalize_string(user_input)}")
    print(f"Reversed    : {reverse_string(user_input)}")
    print(f"Characters  : {count_characters(user_input)}")
