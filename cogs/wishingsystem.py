import discord
from discord.ext import commands
import dbcursor
import random
from disputils import BotEmbedPaginator
import banners
import banneritems

single_rate = 160
ten_rate = 1600
import asyncio
import characterimages
import csettings



four_star_gif = "https://media.discordapp.net/attachments/773312837623218247/784479456051462244/4starwish.gif"
five_star_gif = "https://media.discordapp.net/attachments/773312837623218247/784498449240293446/5starwish.gif"


def check_amount(amount):
    amount = int(amount)
    if amount == 1:
        return True
    elif amount == 10:
        return True
    else:
        return False

def choose_star(amount):
    chances = [5, 4, 4, 4, 4]
    amount = int(amount)
    if amount == 1:
        selected_star = random.choice(chances)
        return selected_star
    elif amount == 10:
        for x in range(1, 4):
            chosen_star = random.choice(chances)
            if chosen_star == 5:
                return 5
            else:
                continue
        
        return 4


class wishingsys(commands.Cog):
    def __init__(self, client):
        self.client = client

 

    @commands.command()
    async def register(self, ctx):
        userid = int(ctx.author.id)
        connection = dbcursor.add_user(userid)
        if connection == "noerr":
            await ctx.send(f"{ctx.author.mention} **|** Successfully registered a Gencord account for you!")
        elif connection == "exists":
            await ctx.send(f"{ctx.author.mention} **|** You already have a Gencord Account!")

    @commands.command(aliases = ["bal"])
    async def balance(self, ctx):
        prefix = str(self.client.command_prefix)
        userid = int(ctx.author.id)
        data = dbcursor.get_user_bal(userid)
        if data == None:
            await ctx.send(f"{ctx.author.mention} **|** Please run the `{prefix}register` command!")
            return
        p = data["primogems"]
        m = data["mora"]
        print(p)
        print(m)
        embed = discord.Embed(
            colour = csettings.embedcolour(),
            description = f"Primogems: {p}\nMora: {m}"
        )
        embed.set_author(name = f"{ctx.author.name}'s Balance", icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)


    @commands.command()
    async def wish(self, ctx, banner : str = "", amount : int = 0):
        wish_banners ={
            "sb" : banners.standard_banner(self.client.command_prefix, self.client.user.name, self.client.user.avatar_url),
            "ab" : banners.event_char_banner(self.client.command_prefix, self.client.user.name, self.client.user.avatar_url)
        }
        userid = int(ctx.author.id)
        if check_amount(amount) == False:
            embeds = [banners.standard_banner(self.client.command_prefix, self.client.user.name, self.client.user.avatar_url), banners.event_char_banner(self.client.command_prefix, self.client.user.name, self.client.user.avatar_url)]
            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()
            return
        elif banner == "":
            embeds = [banners.standard_banner(self.client.command_prefix, self.client.user.name, self.client.user.avatar_url), banners.event_char_banner(self.client.command_prefix, self.client.user.name, self.client.user.avatar_url)]
            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()
            return
        elif amount == 0:
            embeds = [banners.standard_banner(self.client.command_prefix, self.client.user.name, self.client.user.avatar_url), banners.event_char_banner(self.client.command_prefix, self.client.user.name, self.client.user.avatar_url)]
            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()
            return


        if not banner.lower() in wish_banners:
            await ctx.send(f"{ctx.author.mention} **|** That is not a valid banner code!")
            return

        user_data = dbcursor.get_user_bal(userid)
        if user_data == None:
            await ctx.send(f"{ctx.author.mention} **|** Please run the `{self.client.command_prefix}register` command!")
            return
        elif user_data["primogems"] < amount * single_rate:
            await ctx.send(f"{ctx.author.mention} **|** You do not have enough for {amount} wishes!")
            return

        wish_star = choose_star(amount)
        chosen_character = None
        if banner.lower() == "sb":
            chosen_character = banneritems.standard_banner(wish_star)
        elif banner.lower() == "ab":
            chosen_character = banneritems.event_char_banner(wish_star)

        
        gif_embed = discord.Embed(
            colour = csettings.embedcolour()
        )
        if wish_star == 4:
            gif_embed.set_image(url = four_star_gif)
        elif wish_star == 5:
            gif_embed.set_image(url = five_star_gif)

        msg = await ctx.send(embed = gif_embed)
        await asyncio.sleep(6)
        await msg.delete()
        result_embed = discord.Embed(
            colour = csettings.embedcolour()
        )
        result_embed.set_footer(text = f"Summoned By: {ctx.author}", icon_url=ctx.author.avatar_url)
        result_embed.set_author(name = f"{chosen_character}", icon_url = self.client.user.avatar_url)
        result_embed.set_image(url = characterimages.returnlink(chosen_character))
        await ctx.send(embed = result_embed)
        current_user_data = dbcursor.get_user_bal(userid)
        u_ps = current_user_data["primogems"]
        u_ps = int(u_ps)
        u_ps = u_ps - int(amount * single_rate)
        dbcursor.update_bal_p(userid, u_ps)
        dbcursor.add_character(userid, chosen_character)


    @commands.command(aliases = ["viewchars"])
    async def viewcharacters(self, ctx):
        userid = int(ctx.author.id)
        user_chars = dbcursor.get_characters(userid)
        all_chars = "Character Name | Constellation Level\n-------------------------------------"
        if user_chars == None:
            await ctx.send(f"{ctx.author.mention} **|** You have no characters!")
            return

        if str(user_chars) == r"{}":
            await ctx.send(f"{ctx.author.mention} **|** You have no characters!")
            return

        counter = 0
        for char in user_chars:
            c_name = char
            c_level = user_chars[char]
            all_chars = all_chars + "\n" + f"{c_name} | {c_level}"
            counter = counter + 1

        embed = discord.Embed(
            colour = csettings.embedcolour(),
            description = f"```{all_chars}```"
        )

        embed.set_author(name = f"{ctx.author.name}'s Characters", icon_url = ctx.author.avatar_url)
        embed.set_footer(text = self.client.user.name, icon_url = self.client.user.avatar_url)
        await ctx.send(embed = embed)
        


        
            
        





def setup(client):
    client.add_cog(wishingsys(client))