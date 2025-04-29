import discord
from discord.ext import commands
import requests
import asyncio

class randomJoke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.app_commands.command(name="joke", description="Get some jokes?")
    async def getJoke(self, interaction: discord.Interaction):
        headers = {
            "Accept": "application/json",
            "User-Agent": "Learn to use API (https://github.com/MadutttYa/Familiarize-Python/tree/main)"
        }

        response = requests.get("https://icanhazdadjoke.com/", headers=headers)
        result = response.json()

        if (result["status"] == 200):
            await interaction.response.send_message(f"{result['joke']}")
            await interaction.followup.send("Lucu gak?")

            def check(msg):
                return msg.author == interaction.user and msg.channel == interaction.channel

            msg = await self.bot.wait_for("message", check=check, timeout = 30.0)
            try:
                if msg.content.lower() not in ["gak", "no", "tidak", "g"]:
                    await interaction.followup.send("Makasih")
                else:
                    await interaction.followup.send("Kok gitu :(")
            except asyncio.TimeoutError:
                await interaction.followup.send("Ghosting aja terus bro, 30 detik gak balas...")
                
        else:
            await interaction.response.defer(thinking=True)
            await asyncio.sleep(2)
            await interaction.followup.send("Maaf, tidak ada lelucon untuk saat ini HAHAHAH")

async def setup(bot):
    await bot.add_cog(randomJoke(bot=bot))