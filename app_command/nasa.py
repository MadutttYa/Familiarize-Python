import discord
import requests
import dotenv
import os
from discord.ext import commands

dotenv.load_dotenv()
API_KEY = os.getenv("NASA_API_DEMO_KEY")

class Nasa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = API_KEY
    
    def safe_value(text: str) -> str:
        if (not text):
            return
        else:
            limit = 500

    
    @discord.app_commands.command(name="napod", description="Giving the nasa astronomic picture of the day!")
    async def getApod(self, interaction: discord.Interaction):
        params = {
            "api_key": API_KEY
        }

        response = requests.get("https://api.nasa.gov/planetary/apod", params=params).json()
        embed = discord.Embed(title=f"{response.get("title", "N/A")}", color=discord.Colour.blurple())
        embed.set_author(name=f"author : {response.get("copyright", "N/A")}")
        embed.add_field(name="Date", value=f"{response.get("date", "N/A")}", inline=False)
        embed.add_field(name="Description", value=f"{response.get("explanation", "N/A")}")
        if response.get("media_type") == "image":
            embed.set_image(url=response.get("url"))
        else:
            embed.add_field(name="Media Link", value=response.get("url", "Unavailable"), inline=False)

        await interaction.response.send_message(embed=embed)
        print("Media type:", response.get("media_type"))
        print("URL:", response.get("url"))

async def setup(bot):
    await bot.add_cog(Nasa(bot=bot))
