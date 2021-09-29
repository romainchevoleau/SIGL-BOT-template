import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def ban(self, ctx, *, member: discord.Member, reason = None):
       # member = member or ctx.author
        await member.ban(reason = reason)
       # await ctx.send('{0.name}'.format(member))