import discord
from discord.ext import commands


class client_events(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error): # -> Error Handler
        if isinstance(error, TimeoutError):
            embed = discord.Embed(
                colour = discord.Colour.red(),
                description = "Command Timout has occurred. Please re-run the command!"
            )
            embed.set_author(name = "Error", icon_url = self.client.user.avatar_url)

            await ctx.send(embed = embed)
        elif isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                colour = discord.Colour.red(),
                description = str(error)
            )
        else:
            embed = discord.Embed(
                colour = discord.Colour.red(),
                description = "An Unknown Error Has Occurred! Error has been reported to developers!"
            )

            dev_embed = discord.Embed(
                colour = discord.Colour.red(),
                description = f"```{error}```"
            )
            dev_embed.set_author(name = "Error Report", icon_url = self.client.user.avatar_url)
            logs_channel = await self.client.fetch_channel(794332756267499621)
            await logs_channel.send(embed = dev_embed)
            await ctx.send(embed = embed)




    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == f"<@!{self.client.user.id}>":
            await message.channel.send(f"Hey! My Command Prefix is `{self.client.command_prefix}`")

        
    @commands.Cog.listener()
    async def on_guild_join(self, ctx, guild):
        channel = guild.text_channels[0]#
        owner = guild.owner
        embed = discord.Embed(
            description = f"Hey **{owner}**! Thanks for adding me to your server!\nMy command prefix is `{self.client.command_prefix}`\nYou can see what I can do by running my `{self.client.command_prefix}help`",
            colour = csettings.embedcolour()
        )
        embed.add_field(name = "Hey There!", icon_url = self.client.user.avatar_url)
        await channel.send(embed = embed)


def setup(client):
    client.add_cog(client_events(client))