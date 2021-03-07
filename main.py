import requests, json
from modules import test
from colorama import Fore

def print_error(a):
    print(f'{Fore.LIGHTWHITE_EX}[ {Fore.LIGHTRED_EX}ERRO {Fore.LIGHTWHITE_EX}] {Fore.RESET}{a}')

def print_sucess(a):
    print(f'{Fore.LIGHTWHITE_EX}[ {Fore.LIGHTGREEN_EX}INFO {Fore.LIGHTWHITE_EX}] {Fore.RESET}{a}')

def print_info(a):
    print(f'{Fore.LIGHTWHITE_EX}[ {Fore.LIGHTYELLOW_EX}INFO {Fore.LIGHTWHITE_EX}] {Fore.RESET}{a}')

def print_warning(a):
    print(f'{Fore.LIGHTWHITE_EX}[ {Fore.LIGHTYELLOW_EX}WARN {Fore.LIGHTWHITE_EX}] {Fore.RESET}{a}')

def logo():
    return f''' {Fore.WHITE}{Fore.LIGHTBLACK_EX}          {Fore.LIGHTWHITE_EX}0{Fore.LIGHTBLACK_EX}
{Fore.LIGHTBLACK_EX}        {Fore.LIGHTWHITE_EX}0{Fore.LIGHTBLACK_EX} __   __    _              
{Fore.MAGENTA}   _ _/|{Fore.LIGHTBLACK_EX}  \ \ / /  _| |_ _  ___ _ _ 
{Fore.MAGENTA}  \\ o.0/{Fore.LIGHTBLACK_EX}   \ V / || | | ' \/ -_) '_|
{Fore.MAGENTA}   ===== {Fore.LIGHTBLACK_EX}   \_/ \_,_|_|_||_\___|_|   {Fore.LIGHTGREEN_EX}0.1{Fore.WHITE}
'''

def main():
    print(logo())
    print(print_sucess('Starting Vulner...'))
    test('a')