import discord
from discord.ext import commands
import csettings


class aboutcmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def about(self, ctx):
        bots = 0
        for i in ctx.guild.members:
            if i.bot == True:
                bots = bots + 1
        #print(len(self.client.all_members))
        dev = await self.client.fetch_user(691406006277898302)
        bot_name = self.client.user.name
        embed = discord.Embed(
            description = f"Please keep in mind that {bot_name} bot is not at all affiliated with Mihoyo. We are simply a fan made discord bot. If anyone from Mihoyo wants me to take {bot_name} bot down, please DM me via my username: `{dev}`.",
            colour = csettings.embedcolour(),
            timestamp = ctx.message.created_at
        )
        embed.set_author(name = f"About {self.client.user.name} Bot", icon_url = self.client.user.avatar_url)
        embed.set_footer(text = f"Requested by: {ctx.author}", icon_url = self.client.user.avatar_url)
        #embed.add_field(name = "Useful Links", value = f"[Bot Invite Link](https://discord.com/api/oauth2/authorize?client_id=789975395238674463&permissions=8&scope=bot)\n[Bot Upvote Link](https://discord.ly/gencord)",)
        embed.add_field(name = "Server Info", value = f"{len(ctx.guild.members)} members\n{bots} bots")
        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(aboutcmd(client))