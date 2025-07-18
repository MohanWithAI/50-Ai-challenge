import time

def countdown_timer(start=10):
    print("=== Countdown Timer ===")
    for i in range(start, -1, -1):
        print(i)
        time.sleep(1)  # Wait for 1 second

    print("⏰ Time's up!")

if __name__ == "__main__":
    countdown_timer()
