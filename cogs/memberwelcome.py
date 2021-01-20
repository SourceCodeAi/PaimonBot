import discord
from discord.ext import commands
from discord.utils import get

class welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 763087483499577415:
            embed = discord.Embed(
                title = f"Welcome to {member.guild.name}!",
                description = f"Welcome {member.mention}! Hop over to <#768921752054923306> to grab some roles and <#772873003477893141> to tell us a bit about yourself!\n\nEnjoy your stay!",
                colour = discord.Colour.from_rgb(47, 49, 54)
            )
            embed.set_image(url = "https://media.discordapp.net/attachments/773312837623218247/801172307439386634/UVU00AAAAASUVORK5CYII.png")
            embed.set_footer(text = "Member #" + str(len(member.guild.members)), icon_url = member.guild.icon_url)
            chat = await self.client.fetch_channel(763087483969208324)
            await chat.send(embed = embed)
                



def setup(client):
    client.add_cog(welcome(client))