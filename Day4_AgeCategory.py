def age_category():
    try:
        age = int(input("Enter your age: "))
        
        if age < 0:
            print("Age can't be negative.")
        elif age <= 12:
            print("You are a Child.")
        elif 13 <= age <= 17:
            print("You are a Teenager.")
        elif 18 <= age <= 59:
            print("You are an Adult.")
        else:
            print("You are a Senior.")
    
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    age_category()
