import discord
from discord.ext import commands
from discord.utils import get

roles = {
    "moderator" : 763090036873756682,
    "administrator" : 763089929093251114
}

current_mails = {}


async def checkmods(member):
    for i in member.roles:
        if i.id == roles["administrator"]:
            return True
        elif i.id == roles["moderator"]:
            return True


    return False

class modmail(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        #print(message.content)
        ll = get(self.client.guilds, id = 763087483499577415)

        if message.content == f"<@!{self.client.user.id}>":
            await message.channel.send(f"Hey Traveller! I'm Paimon! My Command Prefix is `{self.client.command_prefix}` | You can DM me to contact a staff member or you can run my `{self.client.command_prefix}help` command to see what I can do!")
            return

  
        
            
        if message.author.bot:
            return
            
        if message.guild:
            if message.channel.topic == "Paimon ModMail Channel":
                if f"{self.client.command_prefix}close" in message.content.lower():
                    return
                user = list(current_mails.values()).index(message.channel.id)
                user = list(current_mails.keys())[user]
                user = await self.client.fetch_user(user)
                embed = discord.Embed(
                    colour = discord.Colour.from_rgb(47, 49, 54),
                    title = "Message Received",
                    description = message.content,
                    timestamp = message.created_at
                )
                embed.set_footer(text = f"{message.author} ({message.author.id})", icon_url = message.author.avatar_url)
                await user.send(embed = embed)
                await message.add_reaction("✅")
                return

        if message.author.id in current_mails:
            if message.guild != None:
                return
            user_channel = get(ll.text_channels, id = current_mails.get(message.author.id))
            embed = discord.Embed(
                colour = discord.Colour.from_rgb(47, 49, 54),
                title = "Message Received",
                description = message.content,
                timestamp = message.created_at
            )
            embed.set_footer(text = f"{message.author} ({message.author.id})", icon_url = message.author.avatar_url)
            await user_channel.send(embed = embed)
            await message.add_reaction("✅")
            return
        reactions = ["✅", "❌"]
        
        if message.guild == None:
            embed = discord.Embed(
                colour = discord.Colour.from_rgb(47, 49, 54),
                title = "Confirm ModMail Request",
                description = f"Confirm that you want to contact the Server Staff of {ll.name} by reacting with :white_check_mark: - React with :x: to cancel this request"
            )
            c_request = await message.channel.send(embed = embed)

            for i in reactions:
                await c_request.add_reaction(i)

            def check(reaction, user):
                if user.bot == False:
                    return True


            reaction, user = await self.client.wait_for("reaction_add", check = check, timeout = 30.0)
            if str(reaction.emoji) == "❌":
                new_embed = discord.Embed(
                    description = "Request Cancelled",
                    colour = discord.Colour.from_rgb(47, 49, 54)
                )
                await c_request.edit(embed = new_embed)
                return

            if str(reaction.emoji) == "✅":
                e_embed = discord.Embed(
                    colour = discord.Colour.from_rgb(47, 49, 54),
                    title = "Request Created",
                    description = "Please remember to be kind to our staff members!\nRequest created with initial message set as: `{}`".format(message.content)
                )
                #await c_request.clear_reactions()
                await c_request.edit(embed = e_embed)
                category = await self.client.fetch_channel(793127179511791656)
                channel_name = f"{message.author.name}-{message.author.discriminator}"
                adminrole = get(ll.roles, id = roles["administrator"])
                modrole = get(ll.roles, id = roles["moderator"])
                overwrites = {
                    ll.default_role : discord.PermissionOverwrite(
                        read_messages = False,
                        send_messages = False
                    ),
                    adminrole : discord.PermissionOverwrite(
                        read_messages = True,
                        send_messages = True
                    ),
                    modrole : discord.PermissionOverwrite(
                        read_messages = True,
                        send_messages = True
                    )
                }
                user_help_channel = await ll.create_text_channel(channel_name, category = category)
                await user_help_channel.edit(overwrites = overwrites)
                await user_help_channel.edit(topic = "Paimon ModMail Channel")
                current_mails.update({message.author.id : user_help_channel.id})
                embed = discord.Embed(
                    title = "Message Received",
                    description = message.content,
                    timestamp = message.created_at,
                    colour = discord.Colour.from_rgb(47, 49, 54)
                )
                embed.set_footer(text = f"{message.author} ({message.author.id})", icon_url = message.author.avatar_url)
                await user_help_channel.send(embed = embed)
                await user_help_channel.send(f"Staff Members: {adminrole.mention} | {modrole.mention}")
                await message.add_reaction("✅")


    @commands.command()
    @commands.guild_only()
    async def close(self, ctx, *, reason : str = "No Reason Given"):

        if ctx.guild == None:
            return

        perms = await checkmods(ctx.author)
        if perms != True:
            return
        
        if ctx.channel.topic != "Paimon ModMail Channel":
            return

        user = list(current_mails.values()).index(ctx.channel.id)
        user = list(current_mails.keys())[user]
        user = await self.client.fetch_user(user)
        embed = discord.Embed(
            title = "ModMail Ticket Closed",
            description = "Reason: {}".format(reason),
            colour = discord.Colour.from_rgb(47, 49, 54)
        )
        ll = get(self.client.guilds, id = 763087483499577415)
        embed.set_footer(text = "Replying will create a new ticket!", icon_url = ll.icon_url)
        await user.send(embed = embed)
        await ctx.channel.delete()
        del current_mails[user.id]
        


            
            



def setup(client):
    client.add_cog(modmail(client))