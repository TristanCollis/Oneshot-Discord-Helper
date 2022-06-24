import asyncio
import discord
import discord.utils
from discord.ext import commands
from Cogs.Keeper import Keeper
from Cogs.RadioOperator import RadioOperator


bot = commands.Bot(command_prefix="`")


bot.add_cog(Keeper(bot, ["Keeper"], "tristan-pager"))
bot.add_cog(RadioOperator(bot, ["Keeper"], "Radio Operator", "tristan-pager", "tristan-receiver"))


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
