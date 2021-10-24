#
# Participant:
# Jose Luis Hernandez Meza
#

import subprocess
import time
import argparse
import sys

# Start argparse
parser = argparse.ArgumentParser(
    description = "Cesar Encryption Tool"
    )

# We add the required arguments
parser.add_argument(
    "-r",
    nargs = "?",
    type = str, 
    help = "Type the path to the files")
parser.add_argument(
    "-m",
    nargs = "?",
    default = "1",
    type = str, 
    help = "Choose '1' to use the script in Bash or '2' to use the script in PowerShell")

args = parser.parse_args()

ruta = args.r
modo = args.m

print("=============================================")
print("----------------Starting tool----------------")
print("=============================================")
time.sleep(2)
print("\n\n")
print("Importing scripts...")
print("\n\n")
time.sleep(2)

print("WARNING\nIt is important that if you are going to use Bash you use it on a Linux system.")
time.sleep(2)

if modo == "1":
    print("Starting bash...")
    time.sleep(1)
    sh = input("Are you using Bash to use this script? (yes/no): ")
    if sh == "yes":
        codeSH = subprocess.call("./GeoIP.sh")
        print(codeSH)
        print("The script has been executed")
    elif sh == "no":
        print("You must use Bash to avoid errors")
        exit()
    else:
        print("No option selected")
        exit()
elif modo == "2":
    print("Starting PowerShell...")
    ps = subprocess.Popen(["powershell.exe", ruta], stdout = sys.stdout)
    ps.communicate()
    print("The script has been executed")
