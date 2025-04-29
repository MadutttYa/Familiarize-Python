import discord
from discord.ext import commands

class Kurang(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.app_commands.command(name="kurangi", description="tes aja")
    @discord.app_commands.describe(a="angka pertama", b="angka kedua")
    async def colek(self, interaction: discord.Interaction, a: int, b: int):
        result = a - b
        await interaction.response.send_message(f"Hasil pengurangan = {result}")

async def setup(bot):
    await bot.add_cog(Kurang(bot=bot))