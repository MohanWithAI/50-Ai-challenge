from datetime import datetime

def write_log(activity, filename="daily_log.txt"):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, 'a') as file:
            file.write(f"[{timestamp}] {activity}\n")
        print("✅ Activity logged successfully.")
    except Exception as e:
        print(f"❌ Error writing to log file: {e}")

# --- Main Program ---
if __name__ == "__main__":
    print("📝 Simple Daily Activity Logger")
    print("Type 'exit' to stop logging.\n")

    while True:
        activity = input("Enter activity: ").strip()
        if activity.lower() == 'exit':
            print("🛑 Logging stopped.")
            break
        elif activity:
            write_log(activity)
