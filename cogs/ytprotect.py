import discord
from discord.ext import commands
import requests
#hi


class ytprotect(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild is None:
            return


        yt_role = discord.utils.get(message.guild.roles, id = 797574179674521610)
        content = message.content
        content = content.replace(",", "")
        words = content.split(" ")
        for word in words:
            if "youtube" in word.lower():
                try:
                    r = requests.get(word)
                    if yt_role in message.author.roles:
                        return
                    
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} You need the **{yt_role.name}** role to post YouTube Links!")
                except:
                    pass


        


def setup(client):
    client.add_cog(ytprotect(client))