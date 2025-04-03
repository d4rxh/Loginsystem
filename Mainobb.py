import os
import time
import requests
import subprocess
from datetime import datetime
from termcolor import colored
import pyfiglet  # for generating ASCII art

# ───────────────────────────────────────────
# 1) Rainbow Text Function
# ───────────────────────────────────────────
def rainbow_text(text):
    """
    Returns a string with each character in a different color to simulate a rainbow effect.
    """
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    rainbow = ""
    for i, char in enumerate(text):
        rainbow += colored(char, colors[i % len(colors)], attrs=["bold"])
    return rainbow

# ───────────────────────────────────────────
# 2) Header Display (Glow Rainbow UI)
# ───────────────────────────────────────────
def display_header():
    """
    Clears the screen and prints an enhanced header with a rainbow DARSH credit and date/time.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time_now = now.strftime("%H:%M:%S")

    # Create ASCII art for "DARSH" and apply rainbow effect
    ascii_banner = pyfiglet.figlet_format("DARSH", font="slant")
    ascii_lines = ascii_banner.splitlines()
    colored_banner = "\n".join([rainbow_text(line) for line in ascii_lines])
    print(colored_banner)

    # Additional header text with rainbow glow
    header_lines = [
        "╔════════════════════════════════════════════════════╗",
        "║            MOD MENU TOOL  |  CHOOSE AN OPTION       ║",
        "╚════════════════════════════════════════════════════╝",
        f"🔹 Date: {date} | Time: {time_now}",
        "🔹 Created by: @DARSH/FAITH",
        ""
    ]
    for line in header_lines:
        print(rainbow_text(line))

# ───────────────────────────────────────────
# 3) Progress Bar (Enhanced Rainbow)
# ───────────────────────────────────────────
def show_progress_bar():
    """
    Displays an enhanced rainbow progress bar for user feedback.
    """
    progress_colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    print(rainbow_text("Processing"), end=" ", flush=True)
    for i in range(15):
        time.sleep(0.1)
        color = progress_colors[i % len(progress_colors)]
        print(colored("➤", color, attrs=['bold']), end="", flush=True)
    print(rainbow_text(" Done!"))

# ───────────────────────────────────────────
# 4) GitHub Raw Base URL
# ───────────────────────────────────────────
GITHUB_RAW_URL = "https://raw.githubusercontent.com/d4rxh/MYTOOL/main/"

# ───────────────────────────────────────────
# 5) Script List
# ───────────────────────────────────────────
SCRIPT_FILES = {
    "1": ("MOD_LOBBY.py", "python"),
    "2": ("MOD_CAR.py", "python"),
    "3": ("MOD_SKIN.py", "python"),
    "4": ("ADD_CREDIT.py", "python"),
    "5": ("GOATED.py", "python"),
    "6": ("SIZE_ISSUE_FIX.py", "python"),
    "7": ("SIZE_ISSUE_ICON_FIX.py", "python"),
    "8": ("hit.py", "python"),
    "9": ("killmsg.py", "python"),
    "10": ("entry.py", "python"),
    "11": ("bot.py", "python"),
    "12": ("rep.sh", "bash")
}

# ───────────────────────────────────────────
# 6) Fetch & Run Scripts in RAM
# ───────────────────────────────────────────
def fetch_and_run_script(script_name, script_type):
    """
    Fetches the script from GitHub and runs it in memory.
    """
    script_url = f"{GITHUB_RAW_URL}{script_name}"
    try:
        response = requests.get(script_url)
        if response.status_code == 200:
            script_content = response.text

            if script_type == "python":
                # Execute Python script in RAM
                exec(script_content, globals())
            elif script_type == "bash":
                # Execute Bash script in RAM (no temp file)
                subprocess.run(["bash"], input=script_content, text=True)
            else:
                print(rainbow_text("⚠ Unknown script type."))
        else:
            print(rainbow_text(f"⚠ Failed to fetch script. Status: {response.status_code}"))
    except Exception as e:
        print(rainbow_text(f"⚠ Error: {e}"))

# ───────────────────────────────────────────
# 7) Custom Menu Display (Matching the Screenshot)
# ───────────────────────────────────────────
def display_custom_menu():
    """
    Prints a menu styled similarly to the provided screenshot (Version 3.7 UPDATE).
    """
    print(rainbow_text("┌─────────────────────────────────────────────────────────┐"))
    print(rainbow_text("│                Version 3.7 UPDATE - Main Menu          │"))
    print(rainbow_text("└─────────────────────────────────────────────────────────┘"))
    print()

    # Each option in its own 'box' to mimic screenshot
    # Feel free to adjust spacing and alignment to match more precisely
    menu_layout = [
        "[1. MOD LOBBY]      [2. MOD CAR]        [3. MOD SKIN]",
        "[4. ADD CREDIT]     [5. MOD GUN]        [6. HIT EFFECT (PAK)]",
        "[7. GUN SIZE FIX]   [8. REPAK (OBB)]    [9. KILL MESSAGE (PAK)]",
        "[10. SKIN SIZE FIX] [X. ABOUT TOOL]"
    ]
    for line in menu_layout:
        print(rainbow_text(line))
    print()

    # Return the user's choice
    choice = input(rainbow_text("Enter choice babe (▶): ")).strip()
    return choice

# ───────────────────────────────────────────
# 8) Main Program Loop
# ───────────────────────────────────────────
def main():
    while True:
        # Clear and show fancy ASCII "DARSH" header
        display_header()
        # Then show our custom menu
        choice = display_custom_menu()

        # Special check if user typed 'x' or 'X' for "ABOUT TOOL"
        if choice.lower() == "x":
            # You could fetch and run some "about" script here if you want
            print(rainbow_text("\nABOUT TOOL:\nThis tool is made by DARSH/FAITH, etc.\n"))
            show_progress_bar()
            input(rainbow_text("\nPress Enter to continue..."))
            continue

        # Check if choice is in your known scripts
        if choice in SCRIPT_FILES:
            os.system('cls' if os.name == 'nt' else 'clear')
            script_name, script_type = SCRIPT_FILES[choice]
            fetch_and_run_script(script_name, script_type)
            show_progress_bar()
        elif choice == "0":
            print(rainbow_text("\n👋 Goodbye! Stay Legendary!"))
            break
        else:
            print(rainbow_text("⚠ Invalid choice. Try again."))
        
        input(rainbow_text("\nPress Enter to continue..."))

# ───────────────────────────────────────────
# 9) Start Program
# ───────────────────────────────────────────
if __name__ == "__main__":
    main()