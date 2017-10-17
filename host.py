import os
import time
import sys
import fileinput


"TODO: make it so it works on linux too"
"paths to host file on windows and linux"
WINPATH = os.environ['WINDIR'] + "\System32" + "\drivers" + "\etc"
LINPATH = "/etc/hosts"


def flushDNS():
    print("Flushing DNS.")
    time.sleep(5)
    os.system("ipconfig /flushdns")

"checking if the path exists, if it does, switch to it"
def checkOS():
    if os.path.exists(WINPATH):
        print("Windows system detected, changing to " + WINPATH)
        os.chdir(WINPATH)
    elif os.path.isfile(LINPATH):
        print("Linux system detected, changing to " + LINPATH)
        os.chdir(LINPATH)
    else:
        print("hosts file not found.")


"Opens host file and adds an entry to it, flushing the DNS to make sure the setting is applied"
def addHost():
    while True:
        with open("hosts", "a") as op:
            add = input("Add line to host file: ")
            op.write("\n127.0.0.1	        " + add)
            if add == "":
                break
            """"pressing enter after done adding names still adds the 127.0.0.1 address on a new
            line with no website next to it"""
            "has to do with the way i'm writing it to the file"
    flushDNS()

""
def deleteHost():
    while True:
        remove = input("Which host would you like to delete?: ")
        for line in fileinput.input('hosts', inplace=1):
            line = line.strip()
            if not remove in line:
                print(line)
        if remove == "exit":
            break
    flushDNS()

"command line arguments, add later"
if len(sys.argv)<2:
    print("Usage: hosts.py [--add] OR [--del]")
    exit()
elif sys.argv[1] == "--add":
    checkOS()
    addHost()
elif sys.argv[1] == "--del":
    checkOS()
    deleteHost()


