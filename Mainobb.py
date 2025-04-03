import os
import time
import requests
import subprocess
from datetime import datetime

# ───────────────────────────────────────────
# 1) Simple Color Function (Optional)
#    (If you don't want colors, remove or comment out)
# ───────────────────────────────────────────
def color_text(text, color_code="32"):
    """
    Returns a string with ANSI color codes.
    Default color_code="32" (green).
    You can change color_code for different colors:
      - 31: red
      - 32: green
      - 33: yellow
      - 34: blue
      - 35: magenta
      - 36: cyan
      - 37: white
    """
    return f"\033[{color_code}m{text}\033[0m"

# ───────────────────────────────────────────
# 2) Header Display (Match Screenshot Style)
# ───────────────────────────────────────────
def display_header():
    """
    Clears the screen and prints a header similar to the screenshot:
    MOD MENU (Version 2 Update B)
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(color_text("╔════════════════════════════════════════════════════╗", "33"))
    print(color_text("║      MOD MENU   (Version 2 Update B)              ║", "33"))
    print(color_text("╚════════════════════════════════════════════════════╝", "33"))

    # Show date/time if you want
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time_now = now.strftime("%H:%M:%S")
    print(f"  Date: {date} | Time: {time_now}")
    print(f"  Created by: @DARSH/FAITH\n")

# ───────────────────────────────────────────
# 3) Progress Bar (You can keep it or style it differently)
# ───────────────────────────────────────────
def show_progress_bar():
    """
    Displays a simple progress bar (or any loading effect).
    """
    print("Processing...", end=" ", flush=True)
    for _ in range(15):
        time.sleep(0.05)
        print(color_text("▓", "32"), end="", flush=True)
    print(" Done!\n")

# ───────────────────────────────────────────
# 4) GitHub Raw Base URL
# ───────────────────────────────────────────
GITHUB_RAW_URL = "https://raw.githubusercontent.com/d4rxh/MYTOOL/main/"

# ───────────────────────────────────────────
# 5) Script List (same commands, no changes)
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
# 6) Fetch & Run Scripts in RAM (unchanged)
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
                exec(script_content, globals())
            elif script_type == "bash":
                subprocess.run(["bash"], input=script_content, text=True)
            else:
                print(color_text("⚠ Unknown script type.", "31"))
        else:
            print(color_text(f"⚠ Failed to fetch script. Status: {response.status_code}", "31"))
    except Exception as e:
        print(color_text(f"⚠ Error: {e}", "31"))

# ───────────────────────────────────────────
# 7) Main Menu (Styled to match your screenshot)
# ───────────────────────────────────────────
def main():
    while True:
        # Show top header
        display_header()

        # Print the menu options in the style from the screenshot
        print(color_text("  1. # MOD LOBBY", "36"))
        print(color_text("  2. # MOD CAR", "36"))
        print(color_text("  3. # MOD SKINS (Cars,Outfits)", "36"))
        print(color_text("  4. # ADD CREDIT", "36"))
        print(color_text("  5. # MOD GUN", "36"))
        print(color_text("  6. # FIX SIZE ISSUE GUN", "36"))
        print(color_text("  7. # FIX SIZE ISSUE CARS AND OUTFITS", "36"))
        print(color_text("  8. # MOD HIT EFFECT (Pak)", "36"))
        print(color_text("  9. # KILL MSG", "36"))
        print(color_text(" 10. # ENTRY EMOTE (X-SUIT ONLY)", "36"))
        print(color_text(" 11. # SKIN TOOL", "36"))
        print(color_text(" 12. # REPAK OBB (Testing)", "36"))
        print(color_text("  0. # EXIT\n", "36"))

        # Prompt (like in screenshot: "Enter choice babe ...")
        choice = input(color_text("Enter choice babe (⛧) → ", "35")).strip()

        if choice in SCRIPT_FILES:
            os.system('cls' if os.name == 'nt' else 'clear')
            script_name, script_type = SCRIPT_FILES[choice]
            fetch_and_run_script(script_name, script_type)
            show_progress_bar()
        elif choice == "0":
            print(color_text("\n👋 Goodbye! Stay Legendary!\n", "32"))
            break
        else:
            print(color_text("⚠ Invalid choice. Try again.", "31"))

        # Pause before returning to menu
        input(color_text("Press Enter to continue...", "33"))

# ───────────────────────────────────────────
# 8) Start Program
# ───────────────────────────────────────────
if __name__ == "__main__":
    main()