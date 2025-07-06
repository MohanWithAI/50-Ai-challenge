def personal_greeting():
    # Ask user for their name, age, and favorite color
    name = input("What's your name? ")
    age = input("How old are you? ")
    color = input("What's your favorite color? ")

    # Create and display a personalized message
    message = (
        f"Hello, {name}! 👋\n"
        f"You're {age} years old and love the color {color}.\n"
        "That's awesome! Hope you have a colorful and amazing day! 🎨"
    )
    print("\n" + message)


# Run the function
if __name__ == "__main__":
    personal_greeting()
