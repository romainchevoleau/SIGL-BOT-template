import discord
from discord.ext import commands

class Name(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def name(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        await ctx.send('{0.name}'.format(member))
            