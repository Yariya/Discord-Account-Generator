import discord

import asyncio
import os

from discord.ext import commands
from configuration import config

__name__ = 'botname'
__version__ = 0.1

bot = commands.Bot(command_prefix=config.__prefix__)
bot.remove_command('help')

def get_total_accounts():
    with open('./accounts/minecraft.txt', 'r') as minecraft:
        minecraft_count_lines = len(minecraft.readlines())

    with open('./accounts/nordvpn.txt', 'r') as nordvpn:
        nordvpn_count_lines = len(nordvpn.readlines())

    with open('./accounts/spotify.txt', 'r') as spotify:
        spotify_count_lines = len(spotify.readlines())

    with open('./accounts/origin.txt', 'r') as origin:
        origin_count_lines = len(origin.readlines())


    with open('./accounts/hulu.txt', 'r') as hulu:
        hulu_count_lines = len(hulu.readlines())       



    return minecraft_count_lines + nordvpn_count_lines + spotify_count_lines + origin_count_lines + hulu_count_lines

async def auto_reload():
    await bot.wait_until_ready()
    while not bot.is_closed():
        await bot.change_presence(status=discord.Status, activity=discord.Activity(name=f'{get_total_accounts()} accounts. | Yariya#0001', type=discord.ActivityType.watching))
        await asyncio.sleep(10 * 60)

@bot.event
async def on_ready():
    for filename in os.listdir('./extensions'):
        if filename.endswith('.py'):
            bot.load_extension(f'extensions.{filename[:-3]}')

    print(f'Successfully logged in as {bot.user.name}!')

bot.loop.create_task(auto_reload())
bot.run(config.__token__)
