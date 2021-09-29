from discord import Permissions, guild
import discord
from discord.ext import commands

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    #Mute command
    @commands.command()
    async def mute(self, ctx, *,  member: discord.Member):
        ghostedRole = discord.utils.get(ctx.guild.roles, name="Ghost")

        if not ghostedRole: #Check if the Ghost role exist
            ghostedRole = await ctx.guild.create_role(name="Ghost") #Create the ghost role
            for channel in ctx.guild.channels:
                await channel.set_permissions(ghostedRole, send_messages=False, read_message_history=False, read_messages=False)    #Add the permissions to the role

        if ghostedRole in member.roles: #Mute or unmute the user
            await member.remove_roles(ghostedRole)
        else:
            await member.add_roles(ghostedRole)