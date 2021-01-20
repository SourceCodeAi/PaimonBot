import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs
import requests
import csettings

async def create_embed(ctx, name, description, tactic, img_url, bot_name, bot_img):
    embed = discord.Embed(
        colour = csettings.embedcolour(),
        title = name,
        description = description,
        timestamp = ctx.message.created_at

    )

    embed.add_field(name = "Tactic", value = tactic, inline = False)
    embed.set_image(url = img_url)
    embed.set_author(name = bot_name, icon_url = bot_img)
    embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = bot_img)
    await ctx.send(embed = embed)


class enemysearch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def enemy(self, ctx, *, name : str):
        description = "None Found"
        tactic = "None Found"
        img_url = None
        enemy_name = None
        # Geo Hypostasis 
        name = name.lower()
        name = name.replace(" ", "-")
        #await ctx.send(name)
        r = requests.get(f"https://www.gensh.in/database/enemies/{name}")
        soup = bs(r.content, "html.parser")
        cards = soup.findAll("div", class_ = "card")
        for i in cards:
            try:
                if i.find(class_ = "card-body").h3.get_text() == "Description":
                    description = i.find(class_ = "card-body").p.get_text()
            except:
                pass

        for i in cards:
            try:
                if i.find(class_ = "card-body").h3.get_text() == "Tactic":
                    tactic = i.find(class_ = "card-body").p.get_text()
            except:
                pass


        for i in cards:
            try:
                if i.find(class_ = "card-body").h2.get_text() == " Icon ":
                    img_url = "https://www.gensh.in" + i.find(class_ = "card-body").img["src"]
            except:
                pass


        for i in cards:
            try:
                current_name = name
                current_name = current_name.lower()
                current_name = current_name.replace("-", " ")
                card_name = i.find(class_ = "card-body").h2.get_text()
                if current_name in card_name.lower():
                    enemy_name = card_name

                
            except:
                pass


        await create_embed(ctx, enemy_name, description, tactic, img_url, self.client.user.name, self.client.user.avatar_url)

        


def setup(client):
    client.add_cog(enemysearch(client))