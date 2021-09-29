import os
from re import A
from discord.ext import commands
from dotenv import load_dotenv
from name import *
from mute import *
from ban import *
from admin import *
from poll import *

load_dotenv() #Charge the token

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 148122837889056768  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

bot.add_cog(Name(bot))  #Add the name command

bot.add_cog(Mute(bot))  #Add the mute command

bot.add_cog(Ban(bot))   #Add the Ban command

bot.add_cog(Admin(bot)) #Add the Admin command

bot.add_cog(Poll(bot))

token = os.getenv("DISCORD_TOKEN")
bot.run(token)  # Starts the bot