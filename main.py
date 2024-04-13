# Made by Severityc on Github | Licensed (MIT)
# This was made for educational purposes only
# Find the latest version at https://github.com/severityc/DM-FLOODER

import discord
from discord.ext import commands
import asyncio

async def start_bot(token, bot):
    @bot.event
    async def on_ready():
        print(f'{bot.user} is online!')

    @bot.command()
    async def dm(ctx, user_id: int, *, message):
        user = bot.get_user(user_id)
        if user:
            await ctx.send(f"How many times do you want to send the message to {user}?")

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

            while True:
                try:
                    response = await bot.wait_for('message', check=check, timeout=30)
                    message_count = int(response.content)
                    break 
                except ValueError:
                    await ctx.send("Invalid input. Please enter a number.")

            for _ in range(message_count):
                await user.send(message)
                await asyncio.sleep(1)  # Prevent rate-limiting

            await ctx.send(f'Successfully sent {message_count} message(s) to {user}!')

        else:
            await ctx.send("User not found.")

    @bot.command()
    async def scrape(ctx):
        if not ctx.author.guild_permissions.manage_guild:
            await ctx.send("You don't have the 'Manage Server' permission to use this command.")
            return

        guild = ctx.guild
        member_ids = [member.id for member in guild.members if not member.bot]  # Filter out bots

        with open('data/ids.txt', 'w') as file:
            for member_id in member_ids:
                file.write(f"{member_id}\n")

        await ctx.send("Member IDs have been saved to 'data/ids.txt'")

    @bot.command()
    async def mass_dm(ctx, *, message):
        if not ctx.author.guild_permissions.manage_guild:
            await ctx.send("You don't have the 'Manage Server' permission to use this command.")
            return

        try:
            with open('data/ids.txt', 'r') as file:
                member_ids = [int(line.strip()) for line in file]
        except FileNotFoundError:
            await ctx.send("data/ids.txt not found. Use the !scrape command first.")
            return

        await ctx.send(f"How many times do you want to send the message?")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

        while True:
            try:
                response = await bot.wait_for('message', check=check, timeout=30)
                message_count = int(response.content)
                break
            except ValueError:
                await ctx.send("Invalid input. Please enter a number.")

        for member_id in member_ids:
            user = bot.get_user(member_id)
            if user:
                for _ in range(message_count):
                    await user.send(message)
                    await asyncio.sleep(1) 
            else:
                await ctx.send(f"User with ID {member_id} not found.")

        await ctx.send("Messages sent!")

    await bot.start(token)

async def main():
    with open('data/bot_tokens.txt', 'r') as file:
        tokens = file.readlines()

    tokens = [token.strip() for token in tokens if token.strip()]

    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    await asyncio.gather(*(start_bot(token, bot) for token in tokens))

if __name__ == "__main__":
    asyncio.run(main())
