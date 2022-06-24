import asyncio
import discord
import discord.utils
from discord.ext import commands


bot = commands.Bot(command_prefix="`")


class KeeperCommands(commands.Cog):
    def __init__(self, bot, roles=["Keeper"]) -> None:
        super().__init__()
        self.bot = bot
        self.roles = roles

    def cog_check(self, ctx: commands.Context):
        return any([str(role) in self.roles for role in ctx.author.roles])  # type: ignore

    @commands.command()
    async def send(self, ctx: commands.Context, channelName: str, message: str):
        destinationChannel = [channel for channel in ctx.guild.channels if str(channel) == channelName][0]  # type: ignore
        await destinationChannel.send(message)


bot.add_cog(KeeperCommands(bot))


@bot.event
async def on_ready():
    with open("guild.txt", "r") as f:
        guildID = int(f.readline())
    if len(bot.guilds) > 1 or bot.guilds[0].id != guildID:
        raise RuntimeError(
            "This bot is not yet permitted to access any guilds other than my own."
        )
    print(f"Connected to {bot.guilds[-1]} as {bot.user}")


def main():
    with open("key.txt", "r") as f:
        key = f.readline()

    bot.run(key)


if __name__ == "__main__":
    main()
