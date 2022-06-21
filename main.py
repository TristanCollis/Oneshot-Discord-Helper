import asyncio
import discord
import discord.utils
from discord.ext import commands


bot = commands.Bot(command_prefix="`")


class KeeperCommands(commands.Cog):
    def __init__(self, bot, role="Keeper") -> None:
        super().__init__()
        self.bot = bot
        self.role = role

    
    def cog_check(self, ctx):
        if self.role not in map(str, ctx.author.roles):
            return False
            
        return True
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send("You're a Keeper!")

bot.add_cog(KeeperCommands(bot))

@bot.event
async def on_ready():
    print(f"Connected as {bot.user}")


def main():
    with open('key.txt', 'r') as f:
        key = f.readline()

    bot.run(key)


if __name__ == "__main__":
    main()
