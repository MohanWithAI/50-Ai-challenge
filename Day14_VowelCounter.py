def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0

    for char in word:
        if char in vowels:
            count += 1

    print(f"The number of vowels in '{word}' is: {count}")


if __name__ == "__main__":
    user_input = input("Enter a word or phrase: ")
    count_vowels(user_input)
