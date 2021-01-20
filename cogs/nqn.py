import discord
from discord.ext import commands
import requests
from discord import Webhook, RequestsWebhookAdapter
from io import BytesIO
import nqnsend


class nqn(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def emoji(self, ctx, *, emoji : discord.Emoji):
        print(str(emoji))
        if emoji.animated == False:
            await ctx.send("This isn't an animated emoji. You can send it without nitro!", delete_after = 3)
            return
        channel = ctx.channel
        webhook_image = await discord.Asset.read(ctx.author.avatar_url)
        webhook = await channel.create_webhook(name = str(ctx.author.display_name), avatar = webhook_image, reason = f"Emoji Command Triggered by {ctx.author}/{ctx.author.id}")
        nqnsend.send(webhook.url, str(emoji))
        await ctx.message.delete()
        await webhook.delete(reason = "Emoji Action Finished")

    @emoji.error
    async def emoji_error(self, ctx, error):
        if isinstance(error, commands.EmojiNotFound):
            await ctx.send(f"Couldn't find that emoji!", delete_after = 3)
        





def setup(client):
    client.add_cog(nqn(client))