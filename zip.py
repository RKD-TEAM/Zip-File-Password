import os #for Clear
import sys#for Animation
import time#for Time
import zipfile
import shutil

os.system("clear")

#Type With Animation
print("\n\n\n\n\n")
ab="                 \033[36m System Loading..........."

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)#Animation with Time
print("\n\n\n\n\n")

time.sleep(2)
os.system("clear")

ab="                   \033[1;32m Loading Completed"

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)#Animation with Time

# Name Input
while True:
    Name=input("     \n\n\n            \033[1;36m Enter Your Name: ").strip()
    if Name:
        break
    else:
        print("\033[91m      Name can't be empty. Please enter your name.\033[0m")
  
ab="\033[1;32m             Hey "+ Name +", Be Ethical....\033[0m"

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
print("\n\n\n")
time.sleep(2)
os.system("clear")

# Terminal width
columns = shutil.get_terminal_size().columns

# RKD logo
logo_lines = [
    ":::::::::  :::    ::: ::::::::: ",
    ":+:    :+: :+:   :+:  :+:    :+:",
    "+:+    +:+ +:+  +:+   +:+    +:+",
    "+#++:++#:  +#++:++    +#+    +:+",
    "+#+    +#+ +#+  +#+   +#+    +#+",
    "#+#    #+# #+#   #+#  #+#    #+#",
    "###    ### ###    ### #########"
]

print("\033[1;91m")
for line in logo_lines:
    print(line.center(columns))
print("\033[0m")

print("\033[32m" + "=" * columns + "\033[1;96m")
print(" Owner     : Mr.Rakibul Islam")
print(" Github    : https://github.com/RKD-TEAM")
print(" Facebook  : Alex Rk Khan")
print(" Tool Name : zipfile password Crack (By Brute force)")
print("\033[31m!!!   This tool is for educational purposes only   !!!!!!   So don't use it for any illegal activities   !!!")
print("\033[32m" + "=" * columns + "\033[0m")

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def main():
    while True:
        try:
            z = input(CYAN + "Enter Your zip file Path: " + RESET).strip()
            zip = zipfile.ZipFile(z)
            break
        except FileNotFoundError:
            print(RED + "❌ ZIP file not found! Please check the path." + RESET)
        except zipfile.BadZipFile:
            print(RED + "❌ This is not a valid ZIP file." + RESET)
        except Exception as e:
            print(RED + f"❌ Unexpected error opening ZIP file: {e}" + RESET)

    while True:
        try:
            pw_path = input(CYAN + "Enter Your Password File Path: " + RESET).strip()
            with open(pw_path, "r") as file:
                passwords = [line.strip() for line in file if line.strip()]
            break
        except FileNotFoundError:
            print(RED + "❌ Password file not found! Please check the path." + RESET)
        except Exception as e:
            print(RED + f"❌ Unexpected error opening password file: {e}" + RESET)

    print(YELLOW + f"🔍 Trying {len(passwords)} passwords..." + RESET)

    for count, password in enumerate(passwords, start=1):
        try:
            zip.extractall(pwd=bytes(password, "utf-8"))
            print(GREEN + f"✅ Password found: {password}" + RESET)
            break
        except RuntimeError:
            print(RED + f"❌ Wrong password #{count}: {password}" + RESET)
        except Exception as e:
            print(RED + f"❌ Error during extraction: {e}" + RESET)
            sys.exit(1)
    else:
        print(RED + "❌ Password not found in the provided list." + RESET)

if __name__ == "__main__":
    main()
    print(GREEN + "\nThank you for using the tool!" + RESET)
    input("\033[1;35mPress Enter to exit...")