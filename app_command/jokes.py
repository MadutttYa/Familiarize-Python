import discord
from discord.ext import commands
import requests

class randomJoke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.app_commands.command(name="joke", description="Get some jokes?")
    async def getJoke(interaction: discord.Interaction):
        headers = {
            "Accept": "application/json",
            "User-Agent": "Learning To Use API"
        }

async def setup(bot):
    await bot.add_cog(randomJoke(bot=bot))