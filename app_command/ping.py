import discord
import time
import asyncio
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.app_commands.command(name="ping", description="Memberikan ping bot saat ini")
    async def ping(self, interaction: discord.Interaction):
        start_time = time.perf_counter()
        await interaction.response.defer(thinking=True)
        await asyncio.sleep(4)
        end_time = time.perf_counter()

        response_time = (end_time - start_time) * 1000
    
        await interaction.followup.send(f"Pong! Latency Furina : {self.bot.latency:.2f} ms; response time Furina: {response_time:.2f} ms")

async def setup(bot):
    await bot.add_cog(Ping(bot=bot))