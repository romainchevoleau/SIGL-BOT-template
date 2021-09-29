import discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def poll(self, ctx, question, *argv):
        if (len(argv) < 2) :
            message = await ctx.send(f"@here{question}")
            await message.add_reaction('👍')
            await message.add_reaction('👎')
        else :
            message = await ctx.send(f"@here{question}")
            for arg in argv :
                await message.add_reaction(arg)
