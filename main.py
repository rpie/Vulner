import requests, json, os
from modules import *
from colorama import Fore

def logo():
    return f''' {Fore.WHITE}{Fore.LIGHTBLACK_EX}          {Fore.LIGHTWHITE_EX}0{Fore.LIGHTBLACK_EX}
{Fore.LIGHTBLACK_EX}        {Fore.LIGHTWHITE_EX}0{Fore.LIGHTBLACK_EX} __   __    _              
{Fore.MAGENTA}   _ _/|{Fore.LIGHTBLACK_EX}  \ \ / /  _| |_ _  ___ _ _ 
{Fore.MAGENTA}  \\ o.0/{Fore.LIGHTBLACK_EX}   \ V / || | | ' \/ -_) '_|
{Fore.MAGENTA}   ===== {Fore.LIGHTBLACK_EX}   \_/ \_,_|_|_||_\___|_|   {Fore.LIGHTGREEN_EX}0.1{Fore.WHITE}
'''

def clear():
    os.system('cls')

def main():
    clear()
    print(logo())
    while True:
        cmd = input(f'{Fore.WHITE}[{Fore.MAGENTA} INPU{Fore.WHITE} ] {Fore.GREEN}~>{Fore.WHITE} ')

        if 'cloudssp' in cmd.lower():
            target = cmd.split(' ')[1]
            cloudssp(target)

        if 'remotedown' in cmd.lower():
            target = cmd.split(' ')[1]
            remotedown(target)

        if 'help' in cmd.lower() or 'modules' in cmd.lower():
            helper()

        if cmd.lower() == 'clear' or cmd.lower() == 'cls':
            main()

        if cmd.lower() == 'exit':
            exit('Have a good day :)')
main()