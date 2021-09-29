import os
from discord.ext import commands
from dotenv import load_dotenv
from name import *

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

client = discord.Client()

load_dotenv()
bot.author_id = 148122837889056768  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

bot.add_cog(Name(bot))

token = os.getenv("DISCORD_TOKEN")
bot.run(token)  # Starts the bot