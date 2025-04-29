import weatherapi
from weatherapi.rest import ApiException
import discord
from discord.ext import commands
import dotenv
from pathlib import Path
import os

dotenv.load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.configuration = weatherapi.Configuration()
        self.configuration.api_key['key'] = API_KEY
        self.api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration=self.configuration))
    
    @discord.app_commands.command(name="weather", description="Memberikan weather sesuai lokasi yang diinginkan")
    @discord.app_commands.describe(tempat="Lokasi")
    async def getWeather(self, interaction: discord.Interaction, tempat: str):
        try:
            api_response = self.api_instance.realtime_weather(tempat)
            last_updated = api_response["current"]["last_updated"]
            weather = api_response["current"]["condition"]["text"]
            weather_icon = api_response["current"]["condition"]["icon"]
            feels_like_celcius = api_response["current"]["feelslike_c"]
            heat_celcius = api_response["current"]["heatindex_c"]

            embed = discord.Embed(
                title = f"Cuaca di {tempat}",
                description=f"{weather}",
                color = discord.Color.blue()
            )

            embed.set_thumbnail(url=f"http:{weather_icon}")
            embed.add_field(name="Terakhir update", value=last_updated, inline=False)
            embed.add_field(name="Suhu terasa", value=f"{feels_like_celcius} Celcius", inline=True)
            embed.add_field(name="Index panas", value=f"{heat_celcius} Celcius", inline=True)
            embed.set_author(name="weatherapi.com", url="https://www.weatherapi.com/")

            await interaction.response.send_message(
                embed=embed
            )
        except ApiException as e:
            print("Exception when calling APIsApi->realtime_weather: %s\n" % e)

async def setup(bot):
    await bot.add_cog(Weather(bot=bot))
