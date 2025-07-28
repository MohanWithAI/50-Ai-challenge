import re

def text_statistics(text):
    # Count characters (excluding spaces if desired)
    character_count = len(text)

    # Count words (split by whitespace)
    word_count = len(text.split())

    # Count sentences (basic split by ., !, or ?)
    sentence_count = len(re.findall(r'[.!?]', text))

    print("\n--- Text Statistics ---")
    print(f"Characters: {character_count}")
    print(f"Words     : {word_count}")
    print(f"Sentences : {sentence_count}")

if __name__ == "__main__":
    user_input = input("Enter a paragraph:\n")
    text_statistics(user_input)
