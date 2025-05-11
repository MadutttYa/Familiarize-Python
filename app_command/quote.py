import discord
import requests
from discord.ext import commands

class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="quotes", description="Use this if you need some random quote")
    async def getQuote(self, interaction: discord.Interaction):
        try:
            response = requests.get("https://www.quoterism.com/api/quotes/random").json()
            quotes = response.get("text", "No quotes available then")
            author = response.get("author", {}).get("name", "N/A")
            await interaction.response.send_message(f"""> *{quotes}*\n> By {author}""")
        except requests.RequestException as e:
            response = "There's no advice for today!"
            await interaction.response.send_message(response)
            print(e)

async def setup(bot):
    await bot.add_cog(Quote(bot=bot))