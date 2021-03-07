import requests
from colorama import Fore
from bs4 import BeautifulSoup

def print_error(a):
    print(f'{Fore.LIGHTWHITE_EX}[ {Fore.LIGHTRED_EX}ERRO {Fore.LIGHTWHITE_EX}] {Fore.RESET}{a}')

def print_sucess(a):
    print(f'{Fore.LIGHTWHITE_EX}[ {Fore.LIGHTGREEN_EX}INFO {Fore.LIGHTWHITE_EX}] {Fore.RESET}{a}')

def print_info(a):
    print(f'{Fore.LIGHTWHITE_EX}[ {Fore.LIGHTYELLOW_EX}INFO {Fore.LIGHTWHITE_EX}] {Fore.RESET}{a}')

def print_warning(a):
    print(f'{Fore.LIGHTWHITE_EX}[ {Fore.LIGHTYELLOW_EX}WARN {Fore.LIGHTWHITE_EX}] {Fore.RESET}{a}')

def cloudssp(target):
    if 'http' not in target:
        print_error('Please enter a valid website ( https://test.com )')
        return
    print_info('Starting module CloudSSP..')
    print_info(f'Set target : {target}')
    print_info(f'Testing target for vulnerable page')

    try:
        req = requests.get(f'{target}//mailman/listinfo/mailman')
    except:
        print_warning('Target seems to be offline')
        return
    if req.status_code == 200:
        try:
            soup = BeautifulSoup(req.text, 'html.parser')
            backend = soup.find_all('a')
            backend = requests.get(f'{backend[0].get("href")}', stream=True)
            backend = backend.raw._connection.sock.getpeername()[0]
            print_info(f'Target {Fore.LIGHTGREEN_EX}IS{Fore.WHITE} vulnerable')
            print_sucess(f'Backend IP : {Fore.MAGENTA}{backend}{Fore.WHITE}')
        except:
            print_error('Target isn\'t vulnerable')

def rcetest(target):
    print_info('Starting module CloudSSP..')
    print_info(f'Set Target : {target}')