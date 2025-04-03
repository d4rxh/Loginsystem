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
# 2) Header Display (Box-Style + Glow Rainbow UI)
# ───────────────────────────────────────────
def display_header():
    """
    Clears the screen and prints a header with a rainbow DARSH credit, date/time,
    and a box for the 'MOD MENU | Version 7.2 Updated'.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time_now = now.strftime("%H:%M:%S")

    # Optionally use ASCII art for DARSH
    ascii_banner = pyfiglet.figlet_format("DARSH", font="slant")
    ascii_lines = ascii_banner.splitlines()
    colored_banner = "\n".join([rainbow_text(line) for line in ascii_lines])
    print(colored_banner)

    # Top box for the "MOD MENU | Version 7.2 Updated"
    print(rainbow_text("┌─────────────────────────────────────────┐"))
    print(rainbow_text("│         MOD MENU | Version 7.2         │"))
    print(rainbow_text("│               Updated                  │"))
    print(rainbow_text("└─────────────────────────────────────────┘"))

    # Additional info
    header_lines = [
        f" Date: {date} | Time: {time_now}",
        " Created by: @DARSH/FAITH",
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
# 7) Main Menu (Box-Style + Glow Rainbow UI)
# ───────────────────────────────────────────
def main():
    while True:
        display_header()

        # We’ll display menu options in a style resembling your screenshot.
        # Using ASCII lines and columns:
        print(rainbow_text("┌─────────────────────────────────────────────────────────┐"))
        print(rainbow_text("│                   CHOOSE AN OPTION                      │"))
        print(rainbow_text("├─────────────────────────┬─────────────────────────┬─────┤"))
        print(rainbow_text("│  1) MOD LOBBY           │  2) MOD CAR             │     │"))
        print(rainbow_text("│  3) MOD SKINS           │  4) ADD CREDIT          │     │"))
        print(rainbow_text("│  5) MOD GUN             │  6) FIX SIZE ISSUE GUN  │     │"))
        print(rainbow_text("│  7) FIX SIZE (CARS)     │  8) MOD HIT EFFECT (Pak)│     │"))
        print(rainbow_text("│  9) KILL MSG            │ 10) ENTRY EMOTE (X-SUIT)│     │"))
        print(rainbow_text("│ 11) SKIN TOOL           │ 12) REPAK OBB (Testing) │     │"))
        print(rainbow_text("├─────────────────────────┴─────────────────────────┴─────┤"))
        print(rainbow_text("│  0) EXIT                                             │"))
        print(rainbow_text("└─────────────────────────────────────────────────────────┘"))
        
        # Show an example "Enter choice babe (◕‿◕)" prompt:
        choice = input(rainbow_text("\nEnter choice babe (◕‿◕): ")).strip()

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

        # Pause before showing the menu again
        input(rainbow_text("\nPress Enter to continue..."))

# ───────────────────────────────────────────
# 8) Start Program
# ───────────────────────────────────────────
if __name__ == "__main__":
    main()