import discord
from discord.ext import commands


class disboard(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        author = msg.author
        if author.id != 649604306596528138:
            return
        
        if msg.channel != 773972307470450699:
            return

        embeds = msg.embeds
        embed = embeds[0]
        role = discord.utils.get(msg.guild.roles, id = 801412407884906506)
        if "!d bump" in embed.description.text:
            await msg.channel.send(f"{role.mention} **|** Disboard is off cooldown!")


def setup(client):
    client.add_cog(disboard(client))