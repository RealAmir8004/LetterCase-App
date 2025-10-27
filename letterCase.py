import os
import msvcrt
import subprocess

# Get the current directory where the script is run from
INPUT_PATH = "input.txt"

def read_file(path):
    if not os.path.exists(path):
        print("Error: File does not exist.")
        msvcrt.getch()

        getattr()
        return None
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def convert_text(text, option):
    if not text.strip():
        return "file is empty"
    if option == '1':
        return text.title()
    elif option == '2':
        return text.lower()
    elif option == '3':
        return text.upper()
    else:
        return None

def write_output_file(directory, content):
    output_path = os.path.join(directory, 'output.txt')
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)
    return output_path

def clear_input_file(path):
    with open(path, 'w', encoding='utf-8') as file:
        pass  # Write nothing = clear file

def main():
    content = read_file(INPUT_PATH)
    if content is None:
        return
    
    print("1 - Convert every word to Capitalized (first letter uppercase)\n")
    print("2 - Convert all text to lowercase\n")
    print("3 - Convert all text to UPPERCASE\n")

    while True:
        key = msvcrt.getch().decode('utf-8')
        if key in ['1', '2', '3']:
            break
        else:
            print("Invalid key. Please press 1, 2, or 3.")

    converted = convert_text(content, key)
    if converted is None:
        print("Conversion failed.")
        return

    directory = os.path.dirname(INPUT_PATH)
    output_file = write_output_file(directory, converted)
    # clear_input_file(INPUT_PATH)

    print(f"\nConversion done. Output saved to: {output_file}")
    print("Opening output file...")

    subprocess.Popen(['notepad', output_file])  # Opens in Notepad

if __name__ == "__main__":
    main()
