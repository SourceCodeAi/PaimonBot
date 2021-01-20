import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs
import requests
import csettings


async def create_embed(ctx, description, character_name, unlock_details, character_element, character_star, img_url, bot_name, bot_img, weapon_type):
    character_name = character_name.capitalize()
    embed = discord.Embed(
        title = f"{character_name} Overview",
        colour = csettings.embedcolour(),
        description = description,
        timestamp = ctx.message.created_at
    )
    embed.set_author(name = bot_name, icon_url = bot_img)
    embed.add_field(name = "How to Unlock", value = unlock_details, inline = False)
    embed.add_field(name = "Character Element", value = character_element, inline = False)
    embed.add_field(name = "Weapon Type", value = weapon_type, inline = False)
    embed.add_field(name = "Character Star", value = character_star, inline = False)
    embed.set_image(url = img_url)
    embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = bot_img)
    await ctx.send(embed = embed)

class charactersearch(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def character(self, ctx, * , name : str):
        #Vision / Element:
        print("received")
        description = "No Description Found"
        weapon_type = "None Found"
        unlock_details = "None Found"
        character_element = "None Found"
        character_star = "None Found"
        img_url = "https://media.discordapp.net/attachments/773312837623218247/790207753905897502/iu.png"
        name = name.lower()
        url = f"https://www.gensh.in/characters/{name}"
        r = requests.get(url)
        soup = bs(r.content, "html.parser")
        cards = soup.findAll(class_ = "card")
        for i in cards:
            try:
                if i.find(class_ = "card-header").h3.get_text() == "Description":
                    description = str(i.find(class_ = "card-body").p.get_text())
            except:
                pass

        for i in cards:
            try:
                if i.find(class_ = "card-header").h3.get_text() == "How To Unlock":
                    unlock_details = str(i.find(class_ = "card-body").p.get_text())
            except:
                pass

        for i in cards:
            try:
                if i.find(class_ = "card-header").h3.get_text() == "Character":
                    element_class = soup.findAll("a", href="/genshin-impact/elements")
                    character_element = element_class[1].get_text()
                    
            except:
                pass

       
        for i in cards:
            try:
                if i.find(class_ = "card-header").h3.get_text() == "Character":
                    related_class = i.find(class_ = "card-body")
                    li_list = related_class.findAll("li")
                    for x in li_list:
                        if x.strong.get_text() == "Star Rank:":
                            info = x.get_text()
                            info = str(info)
                            info = info.replace("Star Rank:", "")
                            character_star = info
            except:
                pass



        for i in cards:
            try:
                if i.find(class_ = "card-header").h3.get_text() == "Character":
                    related_class = i.find(class_ = "card-body")
                    li_list = related_class.findAll("li")
                    for x in li_list:
                        if x.strong.get_text() == "Weapon:":
                            info = x.get_text()
                            info = str(info)
                            info = info.replace("Weapon:", "")
                            weapon_type = info
            except:
                pass

        
                    
                    
            

        for i in cards:
            try:
                image_class = i.find(class_ = "card-body character-image")
                img_url = "https://www.gensh.in" + str(image_class.img["src"])
                    
                    
            except:
                pass

        await create_embed(ctx, description, name, unlock_details, character_element, character_star, img_url, self.client.user.name, self.client.user.avatar_url, weapon_type)


def setup(client):
    client.add_cog(charactersearch(client))