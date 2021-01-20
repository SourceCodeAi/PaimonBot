import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs
import requests


blacklist = {
    "Beidou" : "Baidou",
    "Bennett" : "Benett"
}

def returnlink(name):
    if name in blacklist:
        name = blacklist[name]
    return f"https://www.gensh.in/fileadmin/Database/Characters/{name}/Character_{name}_XL.png"