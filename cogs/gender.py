import discord
from discord.ext import commands
from chart.gender import gender

channel_id = None
message = None
male = 0
female = 0 
lgbt = 0
gender_active_command = False

class Gender(commands.Cog):

    def __init__(self , bot):
        self.bot = bot

    @commands.hybrid_command()
    async def gender(self , ctx):
        global gender_active_command
        if gender_active_command:
            embed = discord.Embed(color=discord.Color.from_rgb(128,251,241),title="**Error**" , description=f"**You have already used this command. Please use ```/settings``` and press on the reload button to fix the issue**")
            await ctx.send(embed=embed)
            return
        gender_active_command = True
        global channel_id
        global message
        global male 
        global female
        global lgbt
        channel_id = ctx.channel.id
        urlGender = gender(male=male,female=female , lgbt=lgbt)
        embed = discord.Embed(color=discord.Color.from_rgb(128,251,241) , title="**Gender**" , description="**Participate in the Gender Challenge**").set_image(url=urlGender)
        message = await ctx.send(embed=embed)

        await message.add_reaction("♂️")
        await message.add_reaction("♀️")
        await message.add_reaction("⚧")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        global channel_id
        global message
        global male , female , lgbt
        if reaction.message.channel.id == channel_id and reaction.message.author == self.bot.user:
            emoji = reaction.emoji
            if emoji == "♂️":
                male += 1
            elif emoji == "♀️":
                female += 1
            elif emoji == "⚧":
                lgbt += 1
            urlGender = gender(male=male, female=female, lgbt=lgbt)
            embed = discord.Embed(color=discord.Color.from_rgb(128, 251, 241), title="**Gender**",
                                description="**Participate in the Gender Challenge**").set_image(url=urlGender)
            await message.edit(embed=embed)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        global channel_id
        global message
        global male , female , lgbt
        if reaction.message.channel.id == channel_id and reaction.message.author == self.bot.user:
            emoji = reaction.emoji
            if emoji == "♂️":
                male -= 1
            elif emoji == "♀️":
                female -= 1
            elif emoji == "⚧":
                lgbt -= 1
            urlGender = gender(male=male, female=female, lgbt=lgbt)
            embed = discord.Embed(color=discord.Color.from_rgb(128, 251, 241), title="**Gender**",
                                description="**Participate in the Gender Challenge**").set_image(url=urlGender)
            await message.edit(embed=embed)

async def setup(bot):
    await bot.add_cog(Gender(bot))