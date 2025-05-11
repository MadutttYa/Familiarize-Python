import discord
import requests
from discord.ext import commands

class Affirmation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="affirmation", description="Use this if you need some random affirmation")
    async def getAffirmation(self, interaction: discord.Interaction):
        try:
            response = requests.get("https://www.affirmations.dev").json().get("affirmation", "No affirmation today. Sorry")
            await interaction.response.send_message(f"""> {response}""")
        except requests.RequestException as e:
            response = "There's no affirmation for today!"
            await interaction.response.send_message(response)
            print(e)

async def setup(bot):
    await bot.add_cog(Affirmation(bot=bot))