import json

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




print(f"{bcolors.HEADER}Computer Science 2440 Lab Manager{bcolors.ENDC}")
print(f"{bcolors.HEADER} Labs Found: {bcolors.ENDC}" + str(getLabCount()))
for x in getLabList():
    print(f"{bcolors.OKCYAN}  " + x['labName'])

print(f"{bcolors.ENDC}")
cmd()



