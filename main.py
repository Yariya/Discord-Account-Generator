import discord
import keep_alive
import asyncio
import os

from discord.ext import commands


bot = commands.Bot(command_prefix="!")
bot.remove_command('help')

def get_total_accounts():
    with open('./minecraft.txt', 'r') as minecraft:
        minecraft_count_lines = len(minecraft.readlines())

    with open('./nordvpn.txt', 'r') as nordvpn:
        nordvpn_count_lines = len(nordvpn.readlines())

    with open('./spotify.txt', 'r') as spotify:
        spotify_count_lines = len(spotify.readlines())

    with open('./crunchyroll.txt', 'r') as origin:
        origin_count_lines = len(origin.readlines())


    with open('./hulu.txt', 'r') as hulu:
        hulu_count_lines = len(hulu.readlines())       



    return minecraft_count_lines + nordvpn_count_lines + spotify_count_lines + origin_count_lines + hulu_count_lines


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status, activity=discord.Activity(name=f'{get_total_accounts()} accounts.', type=discord.ActivityType.watching))
    bot.load_extension("commands")

    print(f'Successfully logged in as {bot.user.name}!')
    
keep_alive.keep_alive()
bot.run("token")
