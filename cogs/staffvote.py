import discord
from discord.ext import commands
from discord.utils import get
from disputils import BotConfirmation

current_votes = {}
voted = []

async def get_online_mods(ctx, mod_id):
    counter = 0
    mod = get(ctx.guild.roles, id = 763090036873756682)
    guild = ctx.guild
    for i in guild.members:
        if i.id == mod_id:
            continue
        for role in i.roles:
            if role.id == 763090036873756682:
                if i.raw_status == "online":
                    counter = counter + 1
                elif i.raw_status == "dnd":
                    counter = counter + 1
    
    return counter
            

    #print(current_vote)
#not command
async def add_vote(ctx, mod_id):
    modrole = get(ctx.guild.roles, id = 763090036873756682)
    
    voted.append(ctx.author.id)
    online_mods = await get_online_mods(ctx, mod_id)
    if online_mods == 0:
        raise ValueError("online mods cannot equal 0")

    if mod_id in current_votes:
        current_votes[mod_id] = current_votes[mod_id] + 1
    else:
        current_votes.update({mod_id : 1})

    print(current_votes)

    if current_votes[mod_id] == online_mods:
        mod = get(ctx.guild.members, id = mod_id)
        await mod.remove_roles(modrole)
    elif current_votes[mod_id] == online_mods - 1:
        mod = get(ctx.guild.members, id = mod_id)
        await mod.remove_roles(modrole)
        voted.clear()
        current_votes.clear()
       





        

class staffvote(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def voteoff(self, ctx, member : discord.Member):
        if ctx.author.id in voted:
            await ctx.send("You have already voted!")
            return
        if ctx.author.id == member.id:
            await ctx.send("You can't vote yourself off!")
            return
        
        confirmation = BotConfirmation(ctx)
        await confirmation.confirm("Submit Vote?")

        if confirmation.confirmed:
            await confirmation.update("Confirmed", color=0x55ff55)
            await add_vote(ctx, member.id)
        else:
            await confirmation.update("Not confirmed", hide_author=True, color=0xff5555)


def setup(client):
    client.add_cog(staffvote(client))