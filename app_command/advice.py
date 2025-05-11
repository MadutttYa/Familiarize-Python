import discord
import requests
from discord.ext import commands

class Advice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="advice", description="Use this if you need some random advice")
    async def getAdvice(self, interaction: discord.Interaction):
        try:
            response = requests.get("https://api.adviceslip.com/advice").json().get("slip", {}).get("advice", "there's no advice for now. Sorry.")
            await interaction.response.send_message(f"""> {response}""")
        except requests.RequestException as e:
            response = "There's no advice for today!"
            await interaction.response.send_message(response)
            print(e)

async def setup(bot):
    await bot.add_cog(Advice(bot=bot))