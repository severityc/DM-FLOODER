# Made by Severityc on Github | Licensed (MIT)
# This was made for educational purposes only
# Find the latest version at https://github.com/severityc/DM-FLOODER

import discord
import os
import asyncio
import pyfiglet
import shutil
import webbrowser
import datetime
from discord.ext import commands
from colorama import Fore, Style

async def start_bot(token, bot):
    @bot.event
    async def on_ready():
        print(f'{bot.user} is online!')
        await command_loop(bot)

    await bot.start(token)

async def command_loop(bot):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033]0;DM FLOODER - github.com/severityc - guns.lol/hooked\007", end="", flush=True)

        terminal_width = os.get_terminal_size().columns

        # title using ANSI Shadow ASCII | width = 100 | output = 14px
        choices = {'light_blue': '\033[94m', 'white': '\033[0m'}

        color = 'light_blue' 
        def print_outlined_title():
            if not color:
                background = choices['light_blue']
            else:
                background = choices[color]

            title = f"""
        {background}{'██████╗ ███╗   ███╗    ███████╗██╗      ██████╗  ██████╗ ██████╗ ███████╗██████╗ '}\033[0m
        {background}{'██╔══██╗████╗ ████║    ██╔════╝██║     ██╔═══██╗██╔═══██╗██╔══██╗██╔════╝██╔══██╗'}\033[0m
        {background}{'██║  ██║██╔████╔██║    █████╗  ██║     ██║   ██║██║   ██║██║  ██║█████╗  ██████╔╝'}\033[0m
        {background}{'██║  ██║██║╚██╔╝██║    ██╔══╝  ██║     ██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██╗'}\033[0m
        {background}{'██████╔╝██║ ╚═╝ ██║    ██║     ███████╗╚██████╔╝╚██████╔╝██████╔╝███████╗██║  ██║'}\033[0m
        {background}{'╚═════╝ ╚═╝     ╚═╝    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝'}\033[0m"""

            terminal_width = shutil.get_terminal_size().columns

            centered_title_lines = [line.center(terminal_width) for line in title.split('\n')]

            for line in centered_title_lines:
                print(line)

        print_outlined_title()


        with open('data/bot_tokens.txt', 'r') as file:
            lines = file.readlines()

        terminal_width = shutil.get_terminal_size().columns
        padding = (terminal_width - len("Bot Tokens") - len(str(len(lines)))) // 2

        print(" " * padding + f"Bot Tokens {Fore.LIGHTBLUE_EX}:{Fore.RESET}", len(lines))

        commands = [
            ("1", "DM"),   
            ("2", "Scrape Member IDs"),
            ("3", "Mass DM"),
            ("4", "Exit"),
            ("5", "Github")
        ]
        max_command_width = max(len(command) for _, command in commands)

        for number, command in commands:
            num_padding = (terminal_width - max_command_width - 6) // 2
            print(f"{num_padding * ' '}{Fore.LIGHTBLUE_EX}[{number}]{Fore.RESET} {command}")

        command = input(f"{Fore.LIGHTBLUE_EX}#{Style.RESET_ALL}>> ").lower()

        if not command:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if command == "5":
            webbrowser.open('https://www.guns.lol/hooked')
            webbrowser.open('https://github.com/severityc/DM-FLOODER')
            input("\nPress Enter to continue...")
            continue
        elif command == "4":
            await bot.close()
            break
        elif command == "1":
            user_id = input(f"{Fore.LIGHTBLUE_EX}{datetime.datetime.now().strftime('%H:%M:%S')}{Fore.RESET}{Style.RESET_ALL} Enter user ID: ")
            if not user_id:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            try:
                user_id = int(user_id)
            except ValueError:
                print("Invalid user ID. Please enter a valid user ID.")
                input("\nPress Enter to continue...")
                continue
            message = input(f"{Fore.LIGHTBLUE_EX}{datetime.datetime.now().strftime('%H:%M:%S')}{Fore.RESET}{Style.RESET_ALL} Enter message: ")
            if not message:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            user = bot.get_user(user_id)
            if user:
                await user.send(message)
                print(f"{Fore.LIGHTBLUE_EX}{datetime.datetime.now().strftime('%H:%M:%S')}{Fore.RESET} Message sent to {user}!")
                with open('data/logs.txt', 'a') as log_file:
                    log_file.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Message sent to {user}!\n")
            else:
                print("User not found.")
        elif command == "2":
            guild_id = input(f"{Fore.LIGHTBLUE_EX}{datetime.datetime.now().strftime('%H:%M:%S')}{Fore.RESET}{Style.RESET_ALL} Enter guild ID: ")
            if not guild_id:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            try:
                guild_id = int(guild_id)
            except ValueError:
                print("Invalid guild ID. Please enter a valid guild ID.")
                input("\nPress Enter to continue...")
                continue
            guild = bot.get_guild(guild_id)
            if not guild:
                print("Guild not found.")
                input("\nPress Enter to continue...")
                continue
            member_ids = [member.id for member in guild.members if not member.bot]
            with open('data/ids.txt', 'w') as file:
                for member_id in member_ids:
                    file.write(f"{member_id}\n")
                    print(f"{Fore.LIGHTBLUE_EX}{datetime.datetime.now().strftime('%H:%M:%S')}{Fore.RESET} Scraped user ID: {member_id}")
                    with open('data/logs.txt', 'a') as log_file:
                        log_file.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Scraped user ID: {member_id}\n")
            print("Member IDs have been saved to 'data/ids.txt'")
        elif command == "3":
            message = input(f"{Fore.LIGHTBLUE_EX}{datetime.datetime.now().strftime('%H:%M:%S')}{Fore.RESET}{Style.RESET_ALL} Enter message: ")
            if not message:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            guild_id = input(f"{Fore.LIGHTBLUE_EX}{datetime.datetime.now().strftime('%H:%M:%S')}{Fore.RESET}{Style.RESET_ALL} Enter guild ID: ")
            if not guild_id:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            try:
                guild_id = int(guild_id)
            except ValueError:
                print("Invalid guild ID. Please enter a valid guild ID.")
                input("\nPress Enter to continue...")
                continue
            try:
                with open('data/ids.txt', 'r') as file:
                    member_ids = [int(line.strip()) for line in file]
            except FileNotFoundError:
                print("data/ids.txt not found. Use the 'scrape' command first.")
                input("\nPress Enter to continue...")
                continue
            for member_id in member_ids:
                user = bot.get_user(member_id)
                if user:
                    await user.send(message)
                    await asyncio.sleep(1)
                    print(f"{Fore.LIGHTBLUE_EX}{datetime.datetime.now().strftime('%H:%M:%S')}{Fore.RESET} Message sent to {user}!")
                    with open('data/logs.txt', 'a') as log_file:
                        log_file.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} Message sent to {user}!\n")
                else:
                    print(f"User with ID {member_id} not found.")
            print("Messages sent!")

        input("\nPress Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

async def main():
    with open('data/bot_tokens.txt', 'r') as file:
        tokens = file.readlines()

    tokens = [token.strip() for token in tokens if token.strip()]

    await asyncio.gather(*(start_bot(token, commands.Bot(command_prefix='!', intents=discord.Intents.all())) for token in tokens))

if __name__ == "__main__":
    asyncio.run(main())
