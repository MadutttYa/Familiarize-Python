import discord
import random
from discord.ext import commands

class opinion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="opinion")
    async def getOpinion(self, ctx, *args):
        if await self.bot.is_owner(ctx.author):
            await ctx.send("Whatever you said king, yes it's true, your opinion is valid")
        else:
            await ctx.send("Okay....")

async def setup(bot):
    await bot.add_cog(opinion(bot=bot))