def grade_average():
    print("=== Grade Average Calculator ===")

    scores = []

    # Step 1: Get 5 test scores from the user
    for i in range(1, 6):
        try:
            score = float(input(f"Enter score {i} (out of 100): "))
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Score must be between 0 and 100.")
                return
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

    # Step 2: Calculate average
    average = sum(scores) / len(scores)

    # Step 3: Determine pass/fail (threshold: 40)
    print(f"\nYour average score is: {average:.2f}")
    if average >= 40:
        print("✅ You Passed!")
    else:
        print("❌ You Failed.")

if __name__ == "__main__":
    grade_average()
