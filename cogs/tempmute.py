import discord
from discord.ext import commands
import asyncio
from discord.utils import get



roles = {
    "moderator" : 763090036873756682,
    "administrator" : 763089929093251114
}

time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}

def convert_time_to_seconds(time):
    try:
        return int(time[:-1]) * time_convert[time[-1]]
    except:
        return time


async def checkmods(member):
    for i in member.roles:
        if i.id == roles["administrator"]:
            return True
        elif i.id == roles["moderator"]:
            return True


    return False

class tempmute(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def mute(self, ctx, member : discord.Member, duration, *, reason : str = "No Reason Provided"):
        perms = await checkmods(ctx.author)
        if perms != True:
            return
        duration = str(duration).lower()
        time = convert_time_to_seconds(duration)
        if str(type(time)) == "<class 'float'>":
            time = round(time)
        for role in ctx.author.roles:
            if role.name == "Muted":
                await ctx.send("This person is already muted!")
                return
        muted_role = get(ctx.guild.roles, name = "Muted")
        await member.add_roles(muted_role)
        embed = discord.Embed(
            title = "Member Muted",
            colour = discord.Colour.from_rgb(47, 49, 54),
            timestamp = ctx.message.created_at
        )
        embed.add_field(name = "Rule Breaker", value = f"{member} `({member.id})`", inline = False)
        embed.add_field(name = "Administrator", value = f"{ctx.author} `({ctx.author.id})`", inline = False)
        embed.add_field(name = "Reason", value = reason, inline = False)
        embed.add_field(name = "Guild", value = f"{ctx.guild.name} `({ctx.guild.id})`", inline = False)
        try:
            await member.send(embed = embed)
        except: 
            await ctx.send("Failed to DM user, muting without DM notice!")
            pass
        await ctx.send(embed = embed)
        logs = get(ctx.guild.text_channels, name = "server-logs")
        await logs.send(embed = embed)
        await asyncio.sleep(time)
        await member.remove_roles(muted_role)
        embed = discord.Embed(
            title = "Member Unmuted",
            colour = discord.Colour.from_rgb(47, 49, 54),
            timestamp = ctx.message.created_at
        )
        embed.add_field(name = "Rule Breaker", value = f"{member} `({member.id})`", inline = False)
        embed.add_field(name = "Administrator", value = f"{ctx.author} `({ctx.author.id})`", inline = False)
        embed.add_field(name = "Reason", value = "Mute Expired", inline = False)
        embed.add_field(name = "Guild", value = f"{ctx.guild.name} `({ctx.guild.id})`", inline = False)
        try:
            await member.send(embed = embed)
        except:
            pass
        await logs.send(embed = embed)


    @commands.command()
    async def unmute(self, ctx, member : discord.Member, *, reason : str = "Staff Member has Unmute You"):
        perms = await checkmods(ctx.author)
        if perms != True:
            return
        muted_role = get(ctx.guild.roles, name = "Muted")
        if not muted_role in member.roles:
            await ctx.send("This member isn't muted!")
            return
        await member.remove_roles(muted_role)
        embed = discord.Embed(
            title = "Member Unmuted",
            colour = discord.Colour.from_rgb(47, 49, 54),
            timestamp = ctx.message.created_at
        )
        embed.add_field(name = "Rule Breaker", value = f"{member} `({member.id})`", inline = False)
        embed.add_field(name = "Administrator", value = f"{ctx.author} `({ctx.author.id})`", inline = False)
        embed.add_field(name = "Reason", value = "Mute Expired", inline = False)
        embed.add_field(name = "Guild", value = f"{ctx.guild.name} `({ctx.guild.id})`", inline = False)
        try:
            await member.send(embed = embed)
        except:
            await ctx.send("Failed do DM Rule Breaker! Unmuting without DM notice!")
            pass
        await ctx.send(embed = embed)
        logs = get(ctx.guild.text_channels, name = "server-logs")
        await logs.send(embed = embed)


        

        
        




def setup(client):
    client.add_cog(tempmute(client))