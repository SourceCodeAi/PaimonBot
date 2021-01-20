import discord
from discord.ext import commands


async def pass_error(ctx, error_msg : str):
    embed = discord.Embed(
        colour = discord.Colour.red(),
        description = error_msg
    )
    await ctx.send(embed = embed)