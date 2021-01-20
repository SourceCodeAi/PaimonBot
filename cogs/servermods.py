import discord
from discord.ext import commands
from discord.utils import get
import json

roles = {
    "moderator" : 763090036873756682,
    "administrator" : 763089929093251114
}

async def checkadmin(member):
    for i in member.roles:
        if i.id == roles["administrator"]:
            return True

    return False

    


async def checkmods(member):
    for i in member.roles:
        if i.id == roles["administrator"]:
            return True
        elif i.id == roles["moderator"]:
            return True


    return False
    

    







class servermoderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason : str = "No Reason Given"):
        has_perms = await checkadmin(ctx.author)

        if ctx.author.id == member.id:
            await ctx.send("You can't kick yourself")
            return

        
        print(has_perms)
        if has_perms == True:
            """embed = discord.Embed(
                title = "Member Kicked",
                description = f"`{member} ({member.id})` has been kicked from `{ctx.guild.name} ({ctx.guild.id})` for reason: `{reason}` by Administrator: `{ctx.author} ({ctx.author.id})`"
            )"""
            embed = discord.Embed(
                title = "Member Kicked",
                timestamp = ctx.message.created_at,
                colour = discord.Colour.from_rgb(47, 49, 54)
            )
            embed.add_field(name = "Rule Breaker", value = f"{member} `({member.id})`", inline = False)
            embed.add_field(name = "Administrator", value = f"{ctx.author} `({ctx.author.id})`", inline = False)
            embed.add_field(name = "Reason", value = reason, inline = False)
            embed.add_field(name = "Guild", value = f"{ctx.guild.name} `({ctx.guild.id})`", inline = False)
            try:
                await member.send(embed = embed)
            except:
                await ctx.send("Failed to DM rulebreaker, kicking without DM notice!")
                pass
            await ctx.send(embed = embed)
            await member.kick(reason = f"{reason} | {ctx.author} ({ctx.author.id})")
            logs = get(ctx.guild.text_channels, name = "server-logs")
            await logs.send(embed = embed)
            #await ctx.guild.owner.send(embed = embed)


    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason : str = "No Reason Given"):
        has_perms = await checkadmin(ctx.author)

        if ctx.author.id == member.id:
            await ctx.send("You can't ban yourself")
            return
        print(has_perms)
        if has_perms == True:
            """embed = discord.Embed(
                title = "Member Kicked",
                description = f"`{member} ({member.id})` has been kicked from `{ctx.guild.name} ({ctx.guild.id})` for reason: `{reason}` by Administrator: `{ctx.author} ({ctx.author.id})`"
            )"""
            embed = discord.Embed(
                title = "Member Banned",
                timestamp = ctx.message.created_at,
                colour = discord.Colour.from_rgb(47, 49, 54)
            )
            embed.add_field(name = "Rule Breaker", value = f"{member} `({member.id})`", inline = False)
            embed.add_field(name = "Administrator", value = f"{ctx.author} `({ctx.author.id})`", inline = False)
            embed.add_field(name = "Reason", value = reason, inline = False)
            embed.add_field(name = "Guild", value = f"{ctx.guild.name} `({ctx.guild.id})`", inline = False)
            try:
                await member.send(embed = embed)
            except:
                await ctx.send("Failed to DM rulebreaker, kicking without DM notice!")
                pass
            await ctx.send(embed = embed)
            await member.ban(reason = f"{reason} | {ctx.author} ({ctx.author.id})")
            logs = get(ctx.guild.text_channels, name = "server-logs")
            await logs.send(embed = embed)
            #await ctx.guild.owner.send(embed = embed)

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for entry in banned_users:
            user = entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title = "Member Unbanned",
                    colour = discord.Colour.from_rgb(47, 49, 54)
                )
                embed.add_field(name = "Rule Breaker", value = f"{user} `({user.id})`", inline = False)
                embed.add_field(name = "Administrator", value = ctx.author, inline = False)
                embed.add_field(name = "Reason", value = "Staff Member unbanned user!", inline = False)
                embed.add_field(name = "Guild", value = f"{ctx.guild.name} `({ctx.guild.id})`", inline = False)
                try:
                    await user.send(embed = embed)
                except:
                    await ctx.send("Failed to DM user, Unbanning without DM notice!")
                    
                await ctx.send(embed = embed)
                logs = get(ctx.guild.text_channels, name = "server-logs")
                await logs.send(embed = embed)



def setup(client):
    client.add_cog(servermoderation(client))