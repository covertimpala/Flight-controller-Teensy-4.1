import subprocess
import sys
import colorama
from colorama import Fore

print("User Current Version:-", sys.version)
print(Fore.RESET)


name = 'pyautogui'
print("--==--")
try:
    subprocess.check_call([sys.executable, "-m", "pip", "show", name])
    print(Fore.GREEN + "All requirements satisfied")

except:
    print("Packages need to be installed before Tess can be used")
    print("installing packages")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except:
        print(Fore.RED + "Installation failed")

print(Fore.RESET)
