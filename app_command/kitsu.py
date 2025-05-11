import discord
from discord import ui
from discord.ext import commands
import requests

class Paginator(ui.View):
    def __init__(self, data_list, safe_value):
        super().__init__(timeout=None)
        self.data_list = data_list
        self.safe_value_func = safe_value
        self.index = 0

    async def get_current_embed(self):
        data = self.data_list[self.index]
        embed = discord.Embed(title=data["attributes"]["canonicalTitle"], color=discord.Colour.brand_green(), url="https://myanimelist.net/")
        embed.add_field(name="Synopsis", value=self.safe_value_func((data["attributes"]["synopsis"])), inline=False)
        embed.add_field(name="JP Name", value=data["attributes"]["titles"].get("ja_jp", "N/A"), inline=True)
        embed.add_field(name="Average Rating", value=f"**{data["attributes"]["averageRating"]}**", inline=False)
        embed.set_image(url=data["attributes"]["posterImage"]["original"])
        embed.set_footer(
            text=f"Page {self.index + 1}/{len(self.data_list)} | View more at MAL",
            icon_url="https://icons-for-free.com/iff/png/256/MyAnimeList-1329545826150253280.png",
        )
        return embed
    
    @discord.ui.button(label="⏮️", style=discord.ButtonStyle.grey)
    async def previous_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()  # Changed to defer()
        self.index = (self.index - 1) % len(self.data_list)
        embed = await self.get_current_embed()  # Await the coroutine
        await interaction.edit_original_response(embed=embed, view=self)  # Fixed method name
    
    @discord.ui.button(label="⏭️", style=discord.ButtonStyle.grey)
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()  # Changed to defer()
        self.index = (self.index + 1) % len(self.data_list)
        embed = await self.get_current_embed()  # Await the coroutine
        await interaction.edit_original_response(embed=embed, view=self)  # Fixed method name
    


class Kitsu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_path = "https://kitsu.io/api/edge"
    
    def safe_value(self, text: str) -> str:
         if not text:
             return "-"
         limit = 500
         if len(text) > limit:
             return text[:limit-3] + " ... See more at [MAL](https://myanimelist.net/)"
         else:
             return text
        
    @discord.app_commands.command(name="anime", description="Search for anime")
    @discord.app_commands.describe(anime="anime name")
    async def searchAnime(self, interaction: discord.Interaction, anime: str):
        try:
            result = (requests.get(f"{self.api_path}/anime?filter[text]={anime}")).json()
        except requests.exceptions.RequestException as e:
            error_embed = discord.Embed(
                title="API Error",
                description=f"Could not fetch data from the API: {e}",
                color=discord.Colour.red()
            )
            error_embed.add_field(title="Anda mencari", value=anime, inline=False)
            await interaction.response.send_message(embed=error_embed, ephemeral=True)
            return

        data_list = result["data"][:10]
        paginator_view = Paginator(data_list=data_list, safe_value=self.safe_value)
        initial = await paginator_view.get_current_embed()
        await interaction.response.send_message(embed=initial, ephemeral=False, view=paginator_view)


async def setup(bot):
    await bot.add_cog(Kitsu(bot=bot))