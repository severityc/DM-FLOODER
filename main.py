# Made by Severityc on Github | Licensed (MIT)
# This was made for educational purposes only
# Find the latest version at https://github.com/severityc/DM-FLOODER

import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()


async def start_bot(token):
    bot = commands.Bot(command_prefix='!', intents=intents)

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
            
            try:
                response = await bot.wait_for('message', check=check, timeout=30)
                message_count = int(response.content)
                
                for _ in range(message_count):
                    await user.send(message)
                    
                await ctx.send(f'Successfully sent {message_count} message(s) to {user}!')
                
            except asyncio.TimeoutError:
                await ctx.send("You didn't respond in time. Command cancelled.")
            
        else:
            await ctx.send("User not found.")

    await bot.start(token)

async def main():
    with open('tokens.txt', 'r') as file:
        tokens = file.readlines()

    tokens = [token.strip() for token in tokens if token.strip()]

    await asyncio.gather(*(start_bot(token) for token in tokens))

if __name__ == "__main__":
    asyncio.run(main())
