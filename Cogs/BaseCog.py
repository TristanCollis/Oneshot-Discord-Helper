from discord.ext import commands
import discord.utils
import discord


class BaseCog(commands.Cog):
    def __init__(self, bot: commands.Bot, roles: list) -> None:
        super().__init__()

        self.bot = bot
        self.roles = roles

    
    def cog_check(self, ctx: commands.Context) -> bool:
        return any([str(role) in self.roles for role in ctx.author.roles])  # type: ignore