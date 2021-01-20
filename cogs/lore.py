import discord
from discord.ext import commands
import csettings

class lore(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lore(self, ctx):
        embed = discord.Embed(
            colour = csettings.embedcolour(),
            title = "Teyvat Lore Collection",
            description = "Click [here](https://docs.google.com/document/d/1LwX5siXL9rZ02k-hfViSda_AiBWdO4tdUnN9fvw0ZWY/) to access the ultimate Teyvat Lore Collection!"
        )
        embed.set_image(url = "https://media.discordapp.net/attachments/773312837623218247/793498889583460422/B1F5QVGCqtTQA2HquTUHETPG46zHe-0q0bWHkM_x9byHEbNp2rik5BqEowI8tdq-LhzLiAQmKu0xLBu5y3EshqCtBVA9ix5vmKnz.png?width=1269&height=676")
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(lore(client))