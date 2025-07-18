def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    print(f"Reversed words: {reversed_sentence}")


if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    reverse_words(user_input)
