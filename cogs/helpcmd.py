import discord
from discord.ext import commands
import csettings
import random


staff_commands = ["mute [member] [duration] [reason]", "ban [member] [reason]", "unban [member]"]
g_commands = ["character [character name]", "artifactset [set name]", "previewchar [character name]", "lore", "enemy [enemy name]", "fanart"]

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, *, command_name : str = None):
        bot_prefix = self.client.command_prefix
        s_commands = ""
        genshin_commands = ""
        for i in staff_commands:
            s_commands = s_commands + "\n" + f"- {bot_prefix}{i}"
        
        for i in g_commands:
            genshin_commands = genshin_commands + "\n" + f"- {bot_prefix}{i}"
        server_name = ctx.guild.name
        if command_name == None:
            embed = discord.Embed(
                title = "Paimon Help Panel",
                description = f"Command Prefix: `{bot_prefix}`\nUse the `{bot_prefix}emoji [emoji name]` command to send animated emojis without discord nitro!",
                colour = csettings.embedcolour(),
                timestamp = ctx.message.created_at
            )
            embed.add_field(name = "ModMail", value = f"If you would like to contact {server_name}'s Staff Team for any reason what so ever, please do so by direct messaging {self.client.user.mention}. Please type exactly what your issue is and you will then be asked to confirm your request to contact our Staff Team. Once you do, {self.client.user.mention} will act as a middle man, direct messaging you and the Staff Team. You will understand once you use ModMail for the first time!", inline = False)
            embed.add_field(name = "Staff Commands", value = f"```{s_commands}```", inline = False)
            embed.add_field(name = "Genshin Impact", value = f"```{genshin_commands}```", inline = False)
            images = ["https://media.discordapp.net/attachments/773312837623218247/793562335071043615/iu.png?width=1202&height=676", "https://media.discordapp.net/attachments/773312837623218247/793563238670925856/54780f18-31a0-4931-b1ad-951cc73902ed-ebq-ukjxyaawyhz.png"]
            embed.set_image(url = random.choice(images))
            embed.set_footer(icon_url = self.client.user.avatar_url)
            await ctx.send(embed = embed)


def setup(client):
    client.add_cog(help(client))