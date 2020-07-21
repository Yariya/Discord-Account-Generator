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
    with open('./minecraft.txt', 'r') as minecraft:
        minecraft_count_lines = len(minecraft.readlines())

    with open('./nordvpn.txt', 'r') as nordvpn:
        nordvpn_count_lines = len(nordvpn.readlines())

    with open('./spotify.txt', 'r') as spotify:
        spotify_count_lines = len(spotify.readlines())

    with open('./crunchyroll.txt', 'r') as origin:
        crunchyroll_count_lines = len(crunchyroll.readlines())


    with open('./hulu.txt', 'r') as hulu:
        hulu_count_lines = len(hulu.readlines())       



    return minecraft_count_lines + nordvpn_count_lines + spotify_count_lines + crunchyroll_count_lines + hulu_count_lines

async def auto_reload():
    await bot.wait_until_ready()
    while not bot.is_closed():
        await bot.change_presence(status=discord.Status, activity=discord.Activity(name=f'{get_total_accounts()} accounts.', type=discord.ActivityType.watching))
        await asyncio.sleep(10 * 60)

@bot.event
async def on_ready():
    for filename in os.listdir('./extensions'):
        if filename.endswith('.py'):
            bot.load_extension(f'extensions.{filename[:-3]}')

    print(f'Successfully logged in as {bot.user.name}!')

bot.loop.create_task(auto_reload())
bot.run(config.__token__)
