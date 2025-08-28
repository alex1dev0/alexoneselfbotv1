from discord.ext import commands
import requests

class IP(commands.Cog):
      def __init__(self, bot):
          self.bot = bot

      @commands.command()
      async def ipinfo(self, ctx, ip):
          try:
              response = requests.get(f"http://ip-api.com/json/{ip}")
              data = response.json()

              if data["status"] == "success":
                  message = f"## 🌐 IP INFO {ip}\n\n"
                  message += f"> 🏳️ **Country:** `{data['country']}`\n"
                  message += f"> 🗺️ **Region:** `{data['regionName']}`\n"
                  message += f"> 🏙️ **City:** `{data['city']}`\n"
                  message += f"> 📮 **ZIP:** `{data['zip']}`\n"
                  message += f"> 📍 **Latitude:** `{data['lat']}`\n"
                  message += f"> 📍 **Longitude:** `{data['lon']}`\n"
                  message += f"> 🔌 **ISP:** `{data['isp']}`\n"
                  message += f"> 🏢 **Organization:** `{data['org']}`\n"
                  message += f"> 🌐 **AS:** `{data['as']}`\n"
                  message += f"> ⏰ **Timezone:** `{data['timezone']}`"

                  await ctx.send(message)
              else:
                  await ctx.send("`❌ Could not find information for that IP address.`", delete_after=5)

          except Exception as e:
              await ctx.send(f"`⚠️ An error occurred: {str(e)}`", delete_after=5)

async def setup(bot):
    await bot.add_cog(IP(bot))