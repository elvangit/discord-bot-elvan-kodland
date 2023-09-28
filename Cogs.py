from discord.ext import commands,tasks
from datetime import datetime
class MyCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    # like event
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content == "Hey":
            await msg.channel.send("Hi there!")
    # like function
    @commands.command()
    async def black(self,ctx):
        await ctx.channel.send("White is the opposite of black")
    # set alarm
    @tasks.loop(seconds = 10)
    async def alarm(self,ctx,hour,minute):
        now = datetime.now().time()
        if now.hour == hour and now.minute == minute:
            await ctx.author.create_dm()
            await ctx.author.dm_channel.send("It's time now")
            self.alarm.stop()
    @commands.command()
    async def setalarm(self,ctx,date):
        hour,minute = date.split(":")
        hour = int(hour)
        minute = int(minute)
        self.alarm.start(ctx,hour,minute)
async def setup(bot):
    await bot.add_cog(MyCog(bot))
