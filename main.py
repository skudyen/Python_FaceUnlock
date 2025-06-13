import subprocess
import os
import sys

PYTHON_CMD = os.path.join(sys.prefix, 'Scripts', 'python.exe')

menu = """
===== Face Unlock System =====
[1] Register
[2] Unlock
[3] Exit
==============================
[ Type Number to Select mode than Press Enter to run ]
"""

while True:
    os.system('clear' if os.name == 'posix' else 'cls')
    print(menu)
    choice = input("Choose (1-3): ").strip()

    if choice == '1':
        subprocess.run([PYTHON_CMD, 'register.py'])
        input("\n[Press Enter back to menu]")
    elif choice == '2':
        subprocess.run([PYTHON_CMD, 'unlock.py'])
        input("\n[Press Enter back to menu]")
    elif choice == '3':
        print("\n Exit \n")
        break
    else:
        input("\n[!] Please type 1  2 or 3 Only (Press Enter to continue)")
