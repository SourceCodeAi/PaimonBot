import discord
from discord.ext import commands
import dbcursor

class genshindata(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def addprofile(self, ctx):
        mention = ctx.author.mention
        author_id = int(ctx.author.id)
        def check(msg):
            if msg.author.id == ctx.author.id:
                return True
        await ctx.send(f"{mention} **|** What is your Genshin Impact UID?")
        g_id = await self.client.wait_for("message", check = check, timeout = 30.0)
        await ctx.send(f"{mention} **|** What is your Genshin Impact World Level?")
        wl = await self.client.wait_for("message", check = check, timeout = 30.0)
        await ctx.send(f"{mention} **|** What is your Genshin Impact Username?")
        g_name = await self.client.wait_for("message", check = check, timeout = 30.0)
        await ctx.send(f"{mention} **|** What is your Genshin Impact Adventure Rank?")
        g_rank = await self.client.wait_for("message", check = check, timeout = 30.0)
        dbcursor.genshindata.add_user(author_id, g_id.content, wl.content, g_name.content, g_rank.content)



def setup(client):
    client.add_cog(genshindata(client))