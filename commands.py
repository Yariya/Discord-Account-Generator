import discord
import asyncio
import random


from discord.ext import commands
from datetime import datetime


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command('help')
    async def premiumhelp_command(self, ctx):
        embed = discord.Embed(title='AccGenerator', description=''
        + '\n'
        + '\n**AccGenerator**'
        + '\n`!minecraft` - Generates an minecraft account'
        + '\n`!nordvpn` - Generates an nordvpn account'
        + '\n`!spotify` - Generates an spotify account'
        + '\n`!crunchyroll` - Generates crunchyroll account'
        + '\n`!hulu` - Generates an  hulu account'
        + '\n`-` - PurgeAlts'
        + '\n`'
        + '\n**Stocks**'
        + '\n`!stock` - shows the stock of the accounts'
        + '\n'
        + '\n', color=0x4a0101)
        embed.set_footer(text=f'AccGenerator Help - Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

   
    @commands.guild_only()
    @commands.cooldown(1, (2.5 * 60), commands.BucketType.user)
    @commands.command('nordvpn', ignore_extra=False)
    async def nordvpn_command(self, ctx):
        with open('./nordvpn.txt', 'r') as file:
            file_lines = file.readlines()
            count_lines = len(file_lines)

        random_alt = random.randint(0, count_lines)
        print(f'Currently there are {count_lines} accounts loaded.')

        if file is not None:
            embed = discord.Embed(title=':white_check_mark: NordVPN Account generated!', description='Take a look in your direct messages, I sent you a NordVPN account!', color=0x00ff00)
            embed.set_footer(text=f'Requested by {ctx.author} on the {datetime.now().strftime("%m.%d.%Y")} at {datetime.now().strftime("%H:%M:%S")}.', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

            embed = discord.Embed(title=':white_check_mark: NordVPN Account generated!', description=f'Account: `{file_lines[random_alt]}`', color=0x00ff00)
            await ctx.author.send(embed=embed)
        else:
            print('It seems like the NordVPN alt file isnt there.')

    @commands.guild_only()
    @commands.cooldown(1, (2.5 * 60), commands.BucketType.user)
    @commands.command('spotify', ignore_extra=False)
    async def spotify_command(self, ctx):
        with open('./spotify.txt', 'r') as file:
            file_lines = file.readlines()
            count_lines = len(file_lines)

        random_alt = random.randint(0, count_lines)
        print(f'Currently there are {count_lines} accounts loaded.')

        if file is not None:
            embed = discord.Embed(title=':white_check_mark: spotify Account generated!', description='Take a look in your direct messages, I sent you a spotify account!', color=0x00ff00)
            embed.set_footer(text=f'Requested by {ctx.author} on the {datetime.now().strftime("%m.%d.%Y")} at {datetime.now().strftime("%H:%M:%S")}.', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

            embed = discord.Embed(title=':white_check_mark: spotify Account generated!', description=f'Account: `{file_lines[random_alt]}`', color=0x00ff00)
            await ctx.author.send(embed=embed)
        else:
            print('It seems like the spotify alt file isnt there.')


    @commands.guild_only()
    @commands.cooldown(1, (2.5 * 60), commands.BucketType.user)
    @commands.command('crunchyroll', ignore_extra=False)
    async def crunchyroll_command(self, ctx):
        with open('./crunchyroll.txt', 'r') as file:
            file_lines = file.readlines()
            count_lines = len(file_lines)

        random_alt = random.randint(0, count_lines)
        print(f'Currently there are {count_lines} accounts loaded.')

        if file is not None:
            embed = discord.Embed(title=':white_check_mark: crunchyroll Account generated!', description='Take a look in your direct messages, I sent you a crunchyroll account!', color=0x00ff00)
            embed.set_footer(text=f'Requested by {ctx.author} on the {datetime.now().strftime("%m.%d.%Y")} at {datetime.now().strftime("%H:%M:%S")}.', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

            embed = discord.Embed(title=':white_check_mark: crunchyroll Account generated! | AccGenerator by Yariya#0001', description=f'Account: `{file_lines[random_alt]}`', color=0x00ff00)
            await ctx.author.send(embed=embed)
        else:
            print('It seems like the crunchyroll alt file isnt there.')


    @commands.guild_only()
    @commands.cooldown(1, (2.5 * 60), commands.BucketType.user)
    @commands.command('hulu', ignore_extra=False)
    async def hulu_command(self, ctx):
        with open('./hulu.txt', 'r') as file:
            file_lines = file.readlines()
            count_lines = len(file_lines)

        random_alt = random.randint(0, count_lines)
        print(f'Currently there are {count_lines} accounts loaded.')

        if file is not None:
            embed = discord.Embed(title=':white_check_mark: hulu Account generated! | AccGenerator by Yariya#0001', description='Take a look in your direct messages, I sent you a hulu account!', color=0x00ff00)
            embed.set_footer(text=f'Requested by {ctx.author} on the {datetime.now().strftime("%m.%d.%Y")} at {datetime.now().strftime("%H:%M:%S")}.', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

            embed = discord.Embed(title=':white_check_mark: hulu Account generated!', description=f'Account: `{file_lines[random_alt]}`', color=0x00ff00)
            await ctx.author.send(embed=embed)
        else:
            print('It seems like the hulu alt file isnt there.')


    @commands.guild_only()
    @commands.cooldown(1, (1 * 60), commands.BucketType.user)
    @commands.command('minecraft', ignore_extra=False)
    async def minecraft_command(self, ctx): 
    
        with open('./minecraft.txt', 'r') as file:
            file_lines = file.readlines()
            count_lines = len(file_lines)
        
        random_alt = random.randint(0, count_lines)
        print(f'Currently there are {count_lines} accounts loaded.')

        if file is not None:
            if count_lines != 0:
                embed = discord.Embed(title=':white_check_mark: Minecraft Account generated! | AccGenerator by Yariya#0001', description='Take a look in your direct messages, I sent u a minecraft account!', color=0x00ff00)
                embed.set_footer(text=f'Requested by {ctx.author} on the {datetime.now().strftime("%m.%d.%Y")} at {datetime.now().strftime("%H:%M:%S")}.', icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)

                embed = discord.Embed(title=':white_check_mark: Minecraft Account generated!', description=f'Account: `{file_lines[random_alt]}`', color=0x00ff00)
                
                embed.set_thumbnail(url="https://gamepedia.cursecdn.com/minecraft_de_gamepedia/7/7c/Grasblock.png")
                await ctx.author.send(embed=embed)

                file_lines.pop(random_alt)

                with open('./minecraft.txt', 'w') as file:
                    file.writelines(file_lines)
            else: #ANTICHECK - wenn es 0 is message
                error_embed = discord.Embed(title=f':no_entry: Error: No Accounts in Database | AccGenerator by Yariya#0001',
                                            description='It looks like the Database is out of stock. ', color=0xFF0000) # Own Message
                error_embed.set_footer(text=f'{self.bot.user.name} - Requested by {ctx.author}.', icon_url=ctx.author.avatar_url)
                await ctx.channel.send(embed=error_embed)
        else:
            print('It seems like the minecraft alt file isnt there.')


    @commands.guild_only()
    @commands.command('stock', ignore_extra=False)
    async def stock_command(self, ctx):
        with open('./minecraft.txt', 'r') as minecraft:
            minecraft_count_lines = len(minecraft.readlines())

        with open('./spotify.txt', 'r') as spotify:
            spotify_count_lines = len(spotify.readlines())

        with open('./nordvpn.txt', 'r') as nordvpn:
            nordvpn_count_lines = len(nordvpn.readlines())

        with open('./crunchyroll.txt', 'r') as crunchyroll:
            crunchyroll_count_lines = len(crunchyroll.readlines()) 

        with open('./hulu.txt', 'r') as hulu:
            hulu_count_lines = len(hulu.readlines())       
            
  

        embed = discord.Embed(title='STOCK', description=''
        + f'\nMinecraft - {minecraft_count_lines}'
        + f'\nNordVPN - {nordvpn_count_lines}'
        + f'\nHulu - {hulu_count_lines}'
        + f'\nCrunchyroll - {crunchyroll_count_lines}'
        + f'\nSpotify - {spotify_count_lines}', color=0x00ff00)

        embed.set_footer(text=f'Requested by {ctx.author} on the {datetime.now().strftime("%m.%d.%Y")} at {datetime.now().strftime("%H:%M:%S")}.', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)






def setup(bot):
    bot.add_cog(Commands(bot))
