import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
import csettings
db_pass = os.getenv("TICKETS_PASS")

cluster = pymongo.MongoClient(f"mongodb+srv://paimon:{db_pass}@cluster0.xg3cq.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["tickets"]
tickets_collection = db["tickets"]



async def custom_role(self, ctx):
    def check(m):
        return m.author.id == ctx.author.id
    custom_role_count = 0
    for role in ctx.author.roles:
        if "(custom)" in role.name.lower():
            custom_role_count += 1

    if custom_role_count == 3:
        await ctx.send("You already have the max amount of custom_roles that you can buy!")
        return
    else:
        await ctx.send(f"{ctx.author.mention} **|** What would you like the colour of your custom role to be! Please pass in an RGB value. Example: 255, 255, 255")
        role_color = await self.client.wait_for("message", check = check, timeout = 30.0)
        await ctx.send(f"{ctx.author.mention} **|** What should the name be for your custom role?")
        role_name = await self.client.wait_for("message", check = check, timeout = 30.0)
        role_name = str(role_name.content)
        role_color = role_color.content
        role_color = role_color.replace(" ", "")
        role_color = role_color.replace("(", "")
        role_color = role_color.replace(")", "")
        role_colors = role_color.split(",")
        r = int(role_colors[0])
        g = int(role_colors[1])
        b = int(role_colors[2])
        guild = ctx.guild
        await guild.create_role(name = role_name, mentionable = False, colour = discord.Colour(r, g, b))
        await ctx.send(f"{ctx.author.mention} **|** Created your custom role!")



    





msg_threshold = 100
bully_cost = 5 # (tickets)

class bt(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.ticket = "<:booliticket:795406971083030549>"
        

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild is None:
            return
        if message.channel.id == 782668803011248169:
            return
        if message.author.bot == True:
            return
        userid = int(message.author.id)
        if tickets_collection.find({"_id" : userid}).count() > 0:
            user_data = tickets_collection.find({"_id" : userid})
            user_data = user_data[0]
            current_messages = user_data["messages"]
            current_messages = current_messages + 1
            current_tickets = user_data["tickets"]
            tickets_collection.update({"_id" : userid}, {"$set" : {"messages" : current_messages}})
            if current_messages >= msg_threshold:
                tickets_collection.update({"_id" : userid}, {"$set" : {"messages" : 0}})
                new_tickets = current_tickets + 1
                tickets_collection.update({"_id" : userid}, {"$set" : {"tickets" : new_tickets}})
                await message.channel.send(f"{message.author.mention} **|** Gave you **1** {self.ticket}!")

        else:
            post = {"_id" : userid, "messages" : 1, "tickets" : 0}
            tickets_collection.insert_one(post)



    @commands.command()
    async def tickets(self, ctx):
        userid = int(ctx.author.id)
        if tickets_collection.find({"_id" : userid}).count() > 0:
            user_data = tickets_collection.find({"_id" : userid})
            user_data = user_data[0]
            tickets = user_data["tickets"]
            await ctx.send(f"{ctx.author.mention} **|** You have **{tickets}** {self.ticket}")

    

    @commands.command()
    async def bully(self, ctx, *, dare : str = ""):
        if dare == "":
            await ctx.send("Cool, thx, you ain't bullying me :smiling_face_with_tear:")
            return

        userid = int(ctx.author.id)
        if tickets_collection.find({"_id" : userid}).count() > 0:
            user_data = tickets_collection.find({"_id" : userid})
            user_data = user_data[0]
            tickets = user_data["tickets"]
            if tickets < bully_cost:
                await ctx.send(f"{ctx.author.mention} **|** Nope, you ain't bullying me today! You need **{bully_cost}** {self.ticket} to bully me!")
                return
            else:
                new_tickets = tickets - bully_cost
                tickets_collection.update({"_id" : userid}, {"$set" : {"tickets" : new_tickets}})
                embed = discord.Embed(
                    title = "New Bully Request!",
                    description = dare,
                    colour = csettings.embedcolour(),
                    timestamp = ctx.message.created_at
                )
                embed.set_footer(text = f"{ctx.author} {ctx.author.id}", icon_url = ctx.author.avatar_url)

                moon = await self.client.fetch_user(691406006277898302)

                await moon.send(embed = embed)
                await ctx.send(f"{ctx.author.mention} **|** Sent bully request to {moon.mention} and deducted **{bully_cost}** {self.ticket} from your bully account!")


    
    @commands.command()
    async def messages(self, ctx):
        userid = int(ctx.author.id)
        if tickets_collection.find({"_id" : userid}).count() > 0:
            user_data = tickets_collection.find({"_id" : userid})
            user_data = user_data[0]
            messages = user_data["messages"]
            until = msg_threshold - int(messages)
            await ctx.send(f"{ctx.author.mention} **|** You are **{until}** messages away from your next ticket!")
            return
        else:
            await ctx.end(f"{ctx.author.mention} **|** You have no logged messages! Talk in chat!")


    



    



            
            
        
        




def setup(client):
    client.add_cog(bt(client))

