import asyncio
import discord
from discord.ext import commands
from Cogs.BaseCog import BaseCog


class Keeper(BaseCog):
    def __init__(self, bot: commands.Bot, roles: list, commandChannel: str) -> None:
        super().__init__(bot, roles)
        self.commandChannel = commandChannel

    @commands.command()
    async def ksend(
        self, ctx: commands.Context, channelName: str, message: str
    ) -> None:
        destination: discord.TextChannel = discord.utils.get(ctx.guild.text_channels, name=channelName) # type: ignore
        await destination.send(message)