import discord
from discord.ext import commands

class Colek(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.app_commands.command(name="colek", description="Mencolek....")
    async def colek(self, interaction: discord.Interaction, user: discord.Member):
        if (user == interaction.user):
            await interaction.response.send_message(f"Anda kenapa mencolek diri sendiri? {interaction.user.mention}")
        elif (user == self.bot.user):
            await interaction.response.send_message(f"Pls gak usah colek sy... {interaction.user.mention}")
        else:
            await interaction.response.send_message(f"{interaction.user.mention} mencolek {user.mention}")

async def setup(bot):
    await bot.add_cog(Colek(bot=bot))