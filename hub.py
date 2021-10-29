import json
import os
from urllib.request import urlopen
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class Lab:
	def __init__(self, labName, gitURL, date):
		self.labName = labName
		self.gitURL = gitURL
		self.date = date

def addNewLab(labName, gitURL):
    labs = getLabList()
    newLab = Lab(labName, gitURL, 0)
    labs.append(newLab.__dict__)
    jsonStr = json.dumps(labs)
    os.remove("labs.json")
    text_file = open("labs.json", "w")
    text_file.write(jsonStr)
    text_file.close()

def getLabCount():
    from urllib.request import urlopen
    url = "https://raw.githubusercontent.com/Duhsten/cs2440-manager/main/labs.json"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    jsonString = html
    labList = json.loads(jsonString)
    return len(labList)

def getLabList():
    from urllib.request import urlopen
    url = "https://raw.githubusercontent.com/Duhsten/cs2440-manager/main/labs.json"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    jsonString = html
    labList = json.loads(jsonString)
    return labList

def cmd():
    cmd = input(f"{bcolors.BOLD}> {bcolors.ENDC}")
    if cmd == "help":
        print("Help:")
        print("pull <lab> - ")
        print("add <labName> <gitURL>")
    elif cmd.startswith("add"):
        subcmd = cmd.split(" ")
        addNewLab(subcmd[1], subcmd[2])
        print(f"{bcolors.ENDC}Adding New Lab {bcolors.HEADER}" + subcmd[1])
        print(f"{bcolors.ENDC} Would you like to pull from GitHub now? Y/n")
        result = input()
        if result == "yes" or result == "y":
            print()
        elif result == "no" or result == "n":
            print()



print(f"{bcolors.HEADER}Computer Science 2440 Lab Manager{bcolors.ENDC}")
print(f"{bcolors.HEADER} Labs Found: {bcolors.ENDC}" + str(getLabCount()))
for x in getLabList():
    print(f"{bcolors.OKCYAN}  " + x['labName'])

print(f"{bcolors.ENDC}")
cmd()



