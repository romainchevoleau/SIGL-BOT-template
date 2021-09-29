from discord import Permissions, guild
import discord
from discord.ext import commands

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def mute(self, ctx, *,  member: discord.Member):
        ghostedRole = discord.utils.get(ctx.guild.roles, name="Ghost")

        if not ghostedRole:
            ghostedRole = await ctx.guild.create_role(name="Ghost")
            for channel in ctx.guild.channels:
                await channel.set_permissions(ghostedRole, send_messages=False, read_message_history=False, read_messages=False)
        if ghostedRole in member.roles:
            await member.remove_roles(ghostedRole)
        else:
            await member.add_roles(ghostedRole)