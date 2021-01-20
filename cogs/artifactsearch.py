import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs
import requests
import csettings

class asearch(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def artifactset(self, ctx, *, set_name : str):
        set_description = "None Found"
        set_title = set_name.capitalize()
        set_icon = "https://media.discordapp.net/attachments/773312837623218247/790618263154982952/no_image.png"
        set_name = set_name.lower()
        set_name = set_name.replace(" ", "-")
        r = requests.get(f"https://www.gensh.in/database/artifact-set/{set_name}")
        soup = bs(r.content, "html.parser")
        cards = soup.findAll("div", class_ = "card")
        for i in cards:
            try:
                if i.find(class_ = "card-body").h3.get_text() == "Set Bonus":
                    targets = i.find(class_ = "card-body").ul.findAll("li")
                    #await ctx.send(targets)
                    for li in targets:
                        if targets.index(li) == 0:
                            set_description = f"• {li.get_text()}"
                        else:
                            set_description = set_description + "\n" + f"• {li.get_text()}"

            except:
                pass


        for i in cards:
            try:
                if "icon" in i.find(class_ = "card-body text-center").h2.get_text().lower():
                    img = "https://www.gensh.in" + str(i.find(class_ = "card-body text-center").img["src"])
                    #await ctx.send(str(img))
                    set_icon = str(img)


            except:
                pass


        for i in cards:
            try:
                if i.find(class_ = "card-body").h2.get_text().lower() == " " + set_name.replace("-", " ") + " ":
                    set_title = i.find(class_ = "card-body").h2.get_text()


            except:
                pass


        embed = discord.Embed(
            title = f"{set_title}Overview",
            colour = csettings.embedcolour(),
            timestamp = ctx.message.created_at
        )
        embed.add_field(name = "Set Bonus", value = set_description)
        embed.set_thumbnail(url = set_icon)
        embed.set_author(name = self.client.user.name, icon_url = self.client.user.avatar_url)
        embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = self.client.user.avatar_url)
        await ctx.send(embed = embed)
        



        


           
def setup(client):
    client.add_cog(asearch(client))