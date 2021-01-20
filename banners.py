import discord
from discord.ext import commands
from disputils import BotEmbedPaginator
import csettings

def standard_banner(prefix, name, icon):
    banner_code = "sb"
    embed = discord.Embed(
        colour = csettings.embedcolour()
    )
    embed.set_image(url = "https://media.discordapp.net/attachments/773312837623218247/784179472835280896/unknown.png")
    embed.set_footer(text = f"Banner Code: {banner_code}", icon_url=icon)
    embed.set_author(name = name, icon_url=icon)
    return embed


def event_char_banner(prefix, name, icon):
    banner_code = "ab"
    embed = discord.Embed(
        colour = csettings.embedcolour()
    )
    embed.set_image(url = "https://media.discordapp.net/attachments/773312837623218247/791284370501402644/unknown.png")
    embed.set_footer(text = f"Banner Code: {banner_code}", icon_url = icon)
    embed.set_author(name = name, icon_url = icon)
    return embed