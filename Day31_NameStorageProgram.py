def save_names_to_file(filename, names):
    try:
        with open(filename, 'w') as file:
            for name in names:
                file.write(name + '\n')
        print(f"\n✅ {len(names)} names saved to '{filename}' successfully.")
    except Exception as e:
        print(f"Error saving names: {e}")

def read_names_from_file(filename):
    try:
        with open(filename, 'r') as file:
            names = [line.strip() for line in file.readlines()]
            print(f"\n📄 Names in '{filename}':")
            for i, name in enumerate(names, 1):
                print(f"{i}. {name}")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

# --- Main Program ---
if __name__ == "__main__":
    filename = "names.txt"
    names = []

    print("Enter names (type 'done' to finish):")
    while True:
        name = input("Name: ").strip()
        if name.lower() == 'done':
            break
        if name:
            names.append(name)

    if names:
        save_names_to_file(filename, names)
        read_names_from_file(filename)
    else:
        print("No names entered.")
