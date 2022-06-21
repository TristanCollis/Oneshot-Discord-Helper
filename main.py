import asyncio
import discord
import discord.utils
from discord.ext import commands


bot = commands.Bot(command_prefix="`")


@bot.event
async def on_ready():
    print(f"Connected as {bot.user}")


@bot.command()
async def test(ctx: commands.Context):
    await ctx.send("Tested")


@bot.command()
@commands.has_role("Keeper")
async def keeper(ctx: commands.Context):
    await ctx.send("You're a Keeper!")


def main():
    bot.run("")


if __name__ == "__main__":
    main()
