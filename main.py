import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from dotenv import load_dotenv
import os
import subprocess


#presences
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.reactions = True



def token():
    load_dotenv()
    token = os.getenv("CLIENT_SECRET")
    return str(token)


client = commands.Bot(command_prefix = "p!", case_insensitive = True, intents = intents)

client.remove_command("help")




@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="DM reports!"))
    print("ready")

for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded {filename}")


@client.command()
async def printcmds(ctx):
    for i in client.commands:
        print(i.name)





@client.command()
@commands.cooldown(1, 1800, BucketType.guild)
async def dedchat(ctx):
    role = discord.utils.get(ctx.guild.roles, id = 800401894937198598)
    await ctx.send(f"**{ctx.author.display_name}** thought that the chat was dead! **[ {role.mention} ]**")


@dedchat.error
async def ded_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        if ctx.author.id == ctx.guild.owner.id:
            role = discord.utils.get(ctx.guild.roles, id = 800401894937198598)
            await ctx.send(f"**{ctx.author.display_name}** thought that the chat was dead! **[ {role.mention} ]**")
            


    


@client.command()
async def reload(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.reload_extension(f"cogs.{filename[:-3]}")
            print(f"Reloaded {filename}")

    await ctx.send("Reloaded Bot's Cogs")


client.run(token())