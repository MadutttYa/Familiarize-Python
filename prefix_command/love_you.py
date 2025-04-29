import discord
import asyncio
from discord.ext import commands

class LoveYou(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="loveyou", aliases=["ily"])
    async def love_you(self, ctx):
        channel = ctx.channel
        await ctx.send(f"Love you tooo {ctx.author.mention}, are you fr tho??")

        def check(m):
            return m.channel == channel and m.author == ctx.author
        
        try:
            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            if (msg.content.lower() not in ["no", "nah", "in another life"]):
                await ctx.send(f"okay.")
            else:
                await ctx.send(f"So rude @Neuvillete")
        except asyncio.TimeoutError:
            await ctx.send(f"1 minutes has passed, i guess this is fake as fuck {ctx.author.mention}")
        

async def setup(bot):
    await bot.add_cog(LoveYou(bot=bot))