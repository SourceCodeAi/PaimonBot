import discord
from discord.ext import commands
import csettings
from discord.utils import get




can_post = [636902078383521802, 691406006277898302]

class ad(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_message(self, message):
        content = message.content.lower()
        content = content.replace("`", "")
        content = content.replace("```", "")

        if message.author.id in can_post:
            return
        if message.guild is None:
            return
        if message.channel.id == 787339159295623178:
            return
        if "discord.gg/" in content:
            await message.delete()
            await message.channel.send(f"{message.author.mention} **|** Advertising is not allowed on this server!", delete_after = 5)
            return
        elif "discord.gg" in content:
            await message.delete()
            await message.channel.send(f"{message.author.mention} **|** Advertising is not allowed on this server!", delete_after = 5)
            return


    @commands.command()
    @commands.is_owner()
    async def name(self, ctx, member : discord.Member, *, new_name : str):
        await member.edit(nick = new_name)
        await ctx.send(f"Changed {member.mention}'s nickname to `{new_name}`!")
        

    
    @name.error
    async def ne(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send(f"{ctx.author.mention} **|** You're not Moon. You don't own me!")
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f"{ctx.author.mention} **|** I do not have permissions to do that!")

    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = get(self.client.guilds, id = 763087483499577415)
        t_role = get(guild.roles, id = 763089191399587880)

        if t_role in payload.member.roles:
            return
        if int(payload.message_id) != 791336567641866240:
            return

        if payload.member.bot == True:
            return
        

        member_id = int(payload.user_id)
        member = await self.client.fetch_user(member_id)
        embed = discord.Embed(
            title = "Success!",
            colour = csettings.embedcolour(),
            description = f"Hey Traveller! Thanks for verifying in {guild.name}! We hope you have a wonderful and fun time here! Remember to head over to <#768921752054923306> to get some cool roles and <#772873003477893141> to tell us a bit about yourself!"

        )
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/773312837623218247/796686361310396466/iu.png?width=718&height=676")
        try:
            await member.send(embed = embed)
        except:
            print("Unable to dm user.")
            pass




def setup(client):
    client.add_cog(ad(client))