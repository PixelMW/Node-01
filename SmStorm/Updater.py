import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import threading
import requests
import urllib.request
import json
import asyncio
import sqlite3
import time
import sched
token = "NzUyNDM0NjczNTYwMzIyMDQ5.X1XlZQ.mxwfYB8UbHZxaaOYLVXIq5695x0"

client = commands.Bot(command_prefix=';')
client.remove_command('help')


@client.event
async def on_ready():
    activity = discord.Game(name=";help | by maste#3801", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("SMStorm wlaczony, wykonany przez maste.")


@client.command()
@commands.has_role('SMStorm')

async def new(ctx):
    def prox():
        while 1:
            os.system('rm proxies.txt')
            os.system('rm socks4.txt')
            os.system('rm http.txt')
            os.system('wget https://api.openproxylist.xyz/socks4.txt -O proxies.txt')
            os.system('rm socks4.txt')
            os.system('wget https://api.openproxylist.xyz/socks4.txt')
            os.system('rm http.txt')
            os.system('wget https://api.openproxylist.xyz/http.txt')
            time.sleep(1200)
    while 1:
        t1 = threading.Thread(target=prox)
        t1.start()
        embed = discord.Embed(title='The proxy has been updated, the next update will be in 20 minutes',color=discord.Colour.red())
        await ctx.send(embed=embed)
        time.sleep(1200)


client.run(token)
