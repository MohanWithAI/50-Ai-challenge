def simple_cipher(text):
    result = ""

    for char in text:
        if char.isalpha():
            # Shift lowercase letters
            if char.islower():
                shifted = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            # Shift uppercase letters
            elif char.isupper():
                shifted = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            result += shifted
        else:
            result += char  # Keep non-letters as is

    print(f"Ciphered Text: {result}")

if __name__ == "__main__":
    user_input = input("Enter a word or sentence: ")
    simple_cipher(user_input)
