def read_file_and_count(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)

            print(f"\nFile: {filepath}")
            print(f"Total Lines: {line_count}")
            print(f"Total Words: {word_count}")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example usage ---
file_path = input("Enter the path to your text file: ")
read_file_and_count(file_path)
