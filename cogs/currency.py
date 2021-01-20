import discord
from discord.ext import commands
import dbcursor
import random
from discord.ext.commands.cooldowns import BucketType
import csettings

class currency(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.cooldown(1, 86400, BucketType.user)
    async def daily(self, ctx):
        new_mora = 7500
        new_primos = 320
        userid = int(ctx.author.id)
        current_data = dbcursor.get_user_bal(userid)
        if current_data == None:
            await ctx.send(f"{ctx.author.mention} **|** Please create a Gencord Account by running the `{self.client.command_prefix}register` command!")
            return
        new_p = int(current_data["primogems"]) + new_primos
        new_m = int(current_data["mora"]) + new_mora
        dbcursor.update_bal_p(userid, new_p)
        dbcursor.update_bal_m(userid, new_m)
        await ctx.send(f"{ctx.author.mention} **|** Gave you **{new_mora}** Mora and **{new_primos}** Primogems!")


    @commands.command()
    @commands.cooldown(1, 3600, BucketType.user)
    async def quest(self, ctx):
        userid = int(ctx.author.id)
        new_mora = random.randint(7500, 10000)
        new_primos = random.randint(60, 500)
        current_data = dbcursor.get_user_bal(userid)
        if current_data == None:
            await ctx.send(f"{ctx.author.mention} **|** Please create a Gencord Account by running the `{self.client.command_prefix}register` command!")
            return
        new_p = int(current_data["primogems"]) + new_primos
        new_m = int(current_data["mora"]) + new_mora
        dbcursor.update_bal_p(userid, new_p)
        dbcursor.update_bal_m(userid, new_m)
        await ctx.send(f"{ctx.author.mention} **|** Gave you **{new_mora}** Mora and {new_primos} Primogems!")

    @quest.error
    async def quest_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} **|** You can only go on a quest once every hour!")

    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} **|** Your daily rewards are still on a cooldown!")


    @commands.command()
    async def giftprimos(self, ctx, receiver : discord.Member, amount : int):
        r_id = int(receiver.id)
        gifted = dbcursor.gift_primos(int(ctx.author.id), r_id, amount)
        
        if gifted == None:
            await ctx.send(f"{ctx.author.mention} **|** Either you or the receiver doesn't have a registered Gencord Account. Please make one with the `{self.client.command_prefix}register` command!")
            return
        elif gifted == False:
            await ctx.send(f"{ctx.author.mention} **|** Your balance is too low! You are trying to gift more than you have!")
            return
        elif gifted == True:
            await ctx.send(f"{ctx.author.mention} **|** Successfully gifted **{amount}** Primogems to {receiver.mention}!")
            return

        




def setup(client):
    client.add_cog(currency(client))