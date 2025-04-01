import os
import time
import requests
import subprocess
from datetime import datetime
from termcolor import colored

# ───────────────────────────────────────────
# 1) Header Display
# ───────────────────────────────────────────
def display_header():
    """
    Clears the screen and prints a header with date & time.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time_now = now.strftime("%H:%M:%S")

    print(colored("╔════════════════════════════════════════════════════╗", "light_grey"))
    print(colored("║     MOD MENU TOOL  |  CHOOSE AN OPTION      ║", "yellow"))
    print(colored("╚════════════════════════════════════════════════════╝", "light_grey"))
    print(colored(f"🔹 Date: {date} | Time: {time_now}", "light_grey", attrs=["bold"]))
    print(colored("🔹 Created by: @D4RXH_FAITH", "light_grey", attrs=["bold"]))
    print("")

# ───────────────────────────────────────────
# 2) Progress Bar
# ───────────────────────────────────────────
def show_progress_bar():
    """
    Displays a simple progress bar for user feedback.
    """
    print(colored("Processing", "light_grey"), end=" ", flush=True)
    for _ in range(15):
        time.sleep(0.1)
        print(colored("➤", "yellow", attrs=['bold']), end="", flush=True)
    print(colored(" Done!", "green"))

# ───────────────────────────────────────────
# 3) GitHub Raw Base URL
#    Make sure these filenames exist in your repo.
# ───────────────────────────────────────────
GITHUB_RAW_URL = "https://raw.githubusercontent.com/d4rxh/MYTOOL/main/"

# ───────────────────────────────────────────
# 4) Script List
#    (Option: (filename, script_type))
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
    "9": ("gay", "python"),
    "10": ("rep.sh", "bash")
}

# ───────────────────────────────────────────
# 5) Fetch & Run Scripts in RAM
#    Python => exec()
#    Bash   => subprocess.run(input=..., shell=False)
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
                print(colored("⚠ Unknown script type.", "red", attrs=['bold']))
        else:
            print(colored(f"⚠ Failed to fetch script. Status: {response.status_code}", "red", attrs=['bold']))
    except Exception as e:
        print(colored(f"⚠ Error: {e}", "red", attrs=['bold']))

# ───────────────────────────────────────────
# 6) Main Menu
# ───────────────────────────────────────────
def main():
    while True:
        display_header()

        print(colored("1] MOD LOBBY", "yellow"))
        print(colored("2] MOD CAR", "yellow"))
        print(colored("3] MOD SKINS (Cars,Outfits)", "yellow"))
        print(colored("4] ADD CREDIT", "yellow"))
        print(colored("5] MOD GUN", "yellow"))
        print(colored("6] FIX SIZE ISSUE GUN", "yellow"))
        print(colored("7] FIX SIZE ISSUE CARS AND OUTFITS", "yellow"))
        print(colored("8] MOD HIT EFFECT (Pak)", "yellow"))
        print(colored("9] DONT USE", "yellow"))
        print(colored("10] REPAK OBB (Testing)", "yellow"))
        print(colored("0] EXIT", "red"))

        choice = input(colored("\n🔹 Enter your choice: ", "yellow", attrs=['bold'])).strip()

        if choice in SCRIPT_FILES:
            os.system('cls' if os.name == 'nt' else 'clear')
            script_name, script_type = SCRIPT_FILES[choice]
            fetch_and_run_script(script_name, script_type)
            show_progress_bar()
        elif choice == "0":
            print(colored("\n👋 Goodbye! Stay Legendary!", "cyan"))
            break
        else:
            print(colored("⚠ Invalid choice. Try again.", "red", attrs=['bold']))

# ───────────────────────────────────────────
# 7) Start Program
# ───────────────────────────────────────────
if __name__ == "__main__":
    main()
