import discord
from discord.ext import commands
from Cogs.BaseCog import BaseCog
from Cogs.Keeper import Keeper


class RadioOperator(BaseCog):
    def __init__(
        self,
        bot: commands.Bot,
        roles: list,
        activeOperatorRole: str,
        origin: str,
        destination: str,
    ) -> None:
        super().__init__(bot, roles)
        self.activeOperatorRole = activeOperatorRole
        self.origin = origin
        self.destination = destination

    def cog_check(self, ctx: commands.Context) -> bool:
        return super().cog_check(ctx) and str(ctx.channel) == self.origin

    @commands.command()
    async def send(self, ctx: commands.Context, message: str) -> None:
        destination: discord.TextChannel = discord.utils.get(ctx.guild.text_channels, name=self.destination)  # type: ignore
        await destination.send(message)
