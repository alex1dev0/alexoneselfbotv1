from discord.ext import commands

class IPhoneGift(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def iphonegift(self, ctx):
        await ctx.message.delete()
        
        message = await ctx.send("# 🎉 **iPhone 16 Pro Max Giveaway!** 🎉\n\n`React with 🎁 to participate!`\n`Winner will be chosen in 30 seconds!`", delete_after=31)
        await message.add_reaction("🎁")

async def setup(bot):
    await bot.add_cog(IPhoneGift(bot))