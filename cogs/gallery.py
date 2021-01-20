import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs
import requests
import random
import characterimages
import csettings



class gallerypy(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def fanart(self, ctx):
        r = requests.get("https://www.gensh.in/gallery/wallpaper")
        soup = bs(r.content, "html.parser")
        imgs = soup.findAll("a", class_ = "col-sm-12 col-md-6 col-lg-4 col-xl-3")
        embed = discord.Embed(
            colour = csettings.embedcolour(),
            timestamp = ctx.message.created_at
        )

        chosen = random.choice(imgs)
        url = "https://www.gensh.in" + chosen["href"]
        embed.set_image(url = url)
        embed.set_author(name = "Genshin Impact Fan Art", icon_url = self.client.user.avatar_url)
        embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = self.client.user.avatar_url)
        await ctx.send(embed = embed)


    @commands.command(aliases = ["pc"])
    async def previewchar(self, ctx, *, c_name):
        embed = discord.Embed(
            colour = csettings.embedcolour()
        )
        embed.set_image(url = characterimages.returnlink(c_name.capitalize()))
        await ctx.send(embed = embed)



def setup(client):
    client.add_cog(gallerypy(client))