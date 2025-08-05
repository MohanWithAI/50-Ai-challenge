import json
import os

SCORE_FILE = "high_scores.json"

def load_high_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_high_scores(high_scores):
    with open(SCORE_FILE, 'w') as file:
        json.dump(high_scores, file, indent=4)

def update_score(player, score):
    high_scores = load_high_scores()
    current_score = high_scores.get(player, 0)
    if score > current_score:
        high_scores[player] = score
        print(f"✅ New high score for {player}: {score}")
    else:
        print(f"ℹ️ No update. Current high score for {player} is {current_score}")
    save_high_scores(high_scores)

def display_scores():
    high_scores = load_high_scores()
    if high_scores:
        print("\n🏆 High Scores:")
        for player, score in sorted(high_scores.items(), key=lambda x: x[1], reverse=True):
            print(f"{player}: {score}")
    else:
        print("❌ No high scores found.")

# --- Main Program ---
if __name__ == "__main__":
    print("🎮 Game High Score Tracker")
    while True:
        choice = input("\nChoose an option (1: Add/Update, 2: View, 3: Exit): ")

        if choice == '1':
            name = input("Enter player name: ").strip()
            try:
                score = int(input("Enter new score: "))
                update_score(name, score)
            except ValueError:
                print("⚠️ Invalid score input.")
        elif choice == '2':
            display_scores()
        elif choice == '3':
            print("👋 Exiting High Score Tracker.")
            break
        else:
            print("❌ Invalid option. Try again.")
