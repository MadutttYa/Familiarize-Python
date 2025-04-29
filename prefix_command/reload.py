import discord
from discord.ext import commands
import os

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="reload", aliases=["rld"])
    @commands.is_owner()
    async def reload_commands(self, ctx):
        await ctx.send("Reloading commands...", ephemeral=True)

        for folder in ["app_command", "prefix_command"]:
            for filename in os.listdir(f"./{folder}"):
                if (filename.endswith(".py") and (filename != "__init__.py")):
                    try:
                        await self.bot.unload_extension(f"{folder}.{filename[:-3]}")
                    except Exception as e:
                        pass

        for folder in ["app_command", "prefix_command"]:
            for filename in os.listdir(f"./{folder}"):
                if (filename.endswith(".py") and (filename != "__init__.py")):
                    try:
                        await self.bot.load_extension(f"{folder}.{filename[:-3]}")
                        print(f"Reloaded {folder}.{filename[:-3]}!")
                    except Exception as e:
                        print(f"Failed to reload {folder}.{filename[:-3]}: {e}")
        
        await ctx.send("Selesai menreload semua command!", ephemeral=True)

        try:
            synced = await self.bot.tree.sync()
            await ctx.send(f"synced {len(synced)} command(s)")
            # print(f"synced {len(synced)} command(s)")
        except Exception as e:
            print(f"Error, failed to sync : {e}")


async def setup(bot):
    await bot.add_cog(Reload(bot=bot))
