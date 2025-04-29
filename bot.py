import discord
from discord.ext import commands
import dotenv
from pathlib import Path
import os


dotenv.load_dotenv(Path("./.env"))
API_KEY = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

async def load_commands():
    for filename in os.listdir("./app_command"):
        if (filename.endswith(".py")) and (filename != "__init__.py"):
            await bot.load_extension(f"app_command.{filename[:-3]}")
        
    for filename in os.listdir("./prefix_command"):
        if (filename.endswith(".py")) and (filename != "__init__.py"):
            await bot.load_extension(f"prefix_command.{filename[:-3]}")
            print(f"Loaded prefix {filename[:-3]}")

@bot.event
async def on_ready():
    await load_commands()
    try:
        synced = await bot.tree.sync()
        for i in range(len(synced)):
            print(f"Synced {synced[i]} command")
    except Exception as e:
        print(f"Failed to sync command(s): {e}")

    print(f"[LOGGED IN] {bot.user}")

bot.run(API_KEY)
