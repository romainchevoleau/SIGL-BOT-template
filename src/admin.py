from discord import Permissions
import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def admin(self, ctx, *, member: discord.Member):
       # member = member or ctx.author
       adminRole = discord.utils.get(ctx.guild.roles, name="Admin")
       if not adminRole :
           adminRole = await ctx.guild.create_role(name="Admin", mentionable=True, permissions= Permissions.all())

       await member.add_roles(adminRole)

    #await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")