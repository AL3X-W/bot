import asyncio

import discord

import random

import time


#:lsupa4lf?

from discord.ext import commands




bot = commands.Bot(command_prefix='-')


whitelist = ['-cheaters', '-invites', '-invite', '-top']

@bot.listen()
async def on_message(message):
    role = discord.utils.get(message.guild.roles, name='Member')
    if message.author == bot.user:
        print (message.content)
        return
    if role not in message.author.roles:
        print (message.content)
        return
    contents = message.content.split()
    if not any(word in whitelist for word in contents):
        print (message.content)
        await message.delete()




bot.run(os.environ['TOKEN'])
