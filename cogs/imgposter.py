import discord
from discord.ext import commands, tasks
from bs4 import BeautifulSoup as bs
import requests
import random


class debugcls(commands.Cog):
    def __init__(self, client):
        self.client = client
        @tasks.loop(seconds = 30)
        async def send_img(self):
            channel = await self.client.fetch_channel(796863785075605535)
            try:
                page_num = random.randint(1, 99)
                url = f"https://www.zerochan.net/genshin+impact?p={page_num}"
                r = requests.get(url)
                r.raise_for_status()
                web_content = bs(r.content, "html.parser")
                parent_class = web_content.find(id = "thumbs2")
                sub_classes = parent_class.findAll("li")
                images_received = []
                for x in sub_classes:
                    img_url = x.img["src"]
                    images_received.append(img_url)
                
                chosen_image = random.choice(images_received)
                r = random.randint(1, 254)
                g = random.randint(1, 254)
                b = random.randint(1, 254)
                embed = discord.Embed(
                    colour = discord.Colour.from_rgb(r, g, b)
                )
                embed.set_image(url = chosen_image)
                await channel.send(embed = embed)
            except:
                try:
                    page_num = random.randint(1, 99)
                    url = f"https://www.zerochan.net/genshin+impact?p={page_num}"
                    r = requests.get(url)
                    r.raise_for_status()
                    web_content = bs(r.content, "html.parser")
                    parent_class = web_content.find(id = "thumbs2")
                    sub_classes = parent_class.findAll("li")
                    images_received = []
                    for x in sub_classes:
                        img_url = x.img["src"]
                        images_received.append(img_url)
                    
                    chosen_image = random.choice(images_received)
                    r = random.randint(1, 254)
                    g = random.randint(1, 254)
                    b = random.randint(1, 254)
                    embed = discord.Embed(
                        colour = discord.Colour.from_rgb(r, g, b)
                    )
                    embed.set_image(url = chosen_image)
                    await channel.send(embed = embed)
                except:
                    print("Error occured while getting image!")
                    pass
        send_img.start(self)

    
    



    @commands.command(aliases = ["img"])
    async def image(self, ctx):
        if ctx.channel.id != 796863785075605535:
            await ctx.send(f"{ctx.author.mention} **|** Head over to <#796863785075605535> to use this command!")
            return
            
        try:
            page_num = random.randint(1, 99)
            url = f"https://www.zerochan.net/genshin+impact?p={page_num}"
            r = requests.get(url)
            r.raise_for_status()
            web_content = bs(r.content, "html.parser")
            parent_class = web_content.find(id = "thumbs2")
            sub_classes = parent_class.findAll("li")
            images_received = []
            for x in sub_classes:
                img_url = x.img["src"]
                images_received.append(img_url)
            
            chosen_image = random.choice(images_received)
            r = random.randint(1, 254)
            g = random.randint(1, 254)
            b = random.randint(1, 254)
            embed = discord.Embed(
                colour = discord.Colour.from_rgb(r, g, b)
            )
            embed.set_image(url = chosen_image)
            await ctx.send(embed = embed)
        except:
            page_num = random.randint(1, 99)
            url = f"https://www.zerochan.net/genshin+impact?p={page_num}"
            r = requests.get(url)
            r.raise_for_status()
            web_content = bs(r.content, "html.parser")
            parent_class = web_content.find(id = "thumbs2")
            sub_classes = parent_class.findAll("li")
            images_received = []
            for x in sub_classes:
                img_url = x.img["src"]
                images_received.append(img_url)
            
            chosen_image = random.choice(images_received)
            r = random.randint(1, 254)
            g = random.randint(1, 254)
            b = random.randint(1, 254)
            embed = discord.Embed(
                colour = discord.Colour.from_rgb(r, g, b)
            )
            embed.set_image(url = chosen_image)
            await ctx.send(embed = embed)




def setup(client):
    client.add_cog(debugcls(client))