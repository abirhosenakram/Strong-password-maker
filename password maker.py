import random
import string
import os
from datetime import datetime

# ---------- Color Setup ----------
class Color:
    RESET = "\033[0m"
    GREEN = "\033[92m"      # Strings/Input
    RED = "\033[91m"        # Error
    CYAN = "\033[96m"       # Password/output
    BLUE = "\033[94m"       # Title
    WHITE = "\033[97m"      # Normal text
    YELLOW = "\033[93m"     # Warnings

# ---------- Display Tool Name ----------
# ---------- Display Tool Name ----------
def display_tool_name():
    print(f"""{Color.CYAN}
╔══════════════════════════════╗
║        Password Maker        ║
╚══════════════════════════════╝
{Color.WHITE}Github: abirhosenakram
""")

# ---------- Generate Password ----------
def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += random.choices(characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

# ---------- Save Password ----------
def save_password(password, note):
    try:
        folder_path = '/data/data/com.termux/files/home/PasswordStorage'
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, 'strong_passwords.txt')

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Note: {note if note.strip() else '(No note provided)'}\n")
            file.write(f"Password: {password}\n")
            file.write("="*40 + "\n")

        print(f"{Color.GREEN}Password saved to: {file_path}{Color.RESET}")

    except PermissionError:
        print(f"{Color.RED}Permission Denied: Cannot save file.{Color.RESET}")
        print(f"{Color.YELLOW}Fix: You need to give storage permission to Termux first.{Color.RESET}")
        print(f"{Color.CYAN}Run this command:\n{Color.WHITE}termux-setup-storage")
        print(f"{Color.GREEN}Then allow permission and run the tool again.{Color.RESET}")
    except Exception as e:
        print(f"{Color.RED}An unexpected error occurred:{Color.RESET} {e}")

# ---------- Main ----------
def main():
    while True:
        display_tool_name()
        
        length_input = input(f"{Color.GREEN}Enter password length (default 16): {Color.RESET}").strip()
        if length_input == "":
            length = 16
        else:
            try:
                length = int(length_input)
                if length < 8:
                    print(f"{Color.RED}Length must be at least 8!{Color.RESET}")
                    continue
            except ValueError:
                print(f"{Color.RED}Invalid number. Please enter digits only.{Color.RESET}")
                continue

        password = generate_strong_password(length)
        print(f"{Color.CYAN}Generated Password: {Color.WHITE}{password}{Color.RESET}")

        save_choice = input(f"{Color.GREEN}Do you want to save this password? (y/n): {Color.RESET}").strip().lower()
        if save_choice == 'y':
            note = input(f"{Color.GREEN}Enter a note to recognize this password (optional): {Color.RESET}")
            save_password(password, note)

        again = input(f"\n{Color.GREEN}Generate another password? (y/n): {Color.RESET}").strip().lower()
        if again != 'y':
            print(f"\n{Color.CYAN}Thanks for using Password Maker Tool.\nBe secure,stay secure{Color.RESET}")
            break

if __name__ == "__main__":
    main()