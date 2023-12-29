import discord
from discord.ext import commands
import Paginator

class HelpCommand(commands.Cog):

    def __init__(self , bot):
        self.bot = bot

    @commands.hybrid_command()
    async def help(self , ctx):
        """
        A brochure for understandign bot's feature
        """
        if ctx.author.guild_permissions.administrator:
            embeds = [
                discord.Embed(color=discord.Color.from_rgb(128,251,241), title="**Brochure**",description="**Pepperoni-X is a versatile Discord bot designed to enhance your server experience. With a variety of features and commands, Pepperoni-X offers a seamless way to engage with your community, streamline activities, and foster meaningful interactions. Whether you're interested in staying updated on voice channel activity, Pepperoni-X has you covered. Explore the commands below to discover how Pepperoni-X can add value to your server!**").set_image(url="https://images.pexels.com/photos/4109111/pexels-photo-4109111.jpeg?auto=compress&cs=tinysrgb&w=600"),
                # discord.Embed(color=discord.Color.from_rgb(185,139,212), title="**Pepperoni-X Cogs**",description="** ```/gender``` The command allows you to express your gender identity and see how many members in the server identify as male, female, or transgender. Upon using the command, a visually appealing embedded message will be displayed containing a chart with three interactive emoji buttons: male, female, and transgender flags. When you react to any of these emoji buttons, the chart dynamically updates to reflect the choice you made. The chart consists of three sections: male, female, and transgender, each showing the number of members who have selected that identity. By participating in this interactive chart, you contribute to a better understanding of the gender distribution within the community.**"),
                discord.Embed(color=discord.Color.from_rgb(200,3,218), title="**Pepperoni-X Cogs**",description="** ```/voice``` Command:Description: Monitor Voice ActivityUsage: /voice: This command displays an embed with a real-time chart that monitors voice activity in your server. It shows the number of online members and the number of members in voice channels. The chart updates when members join or leave voice channels. Any time you use this command if you use it before it will delete your previous chart.**"),
                                discord.Embed(color=discord.Color.from_rgb(200,3,218), title="**Pepperoni-X Cogs**",description="** ```<ask```Pepperoni-X is more than just a regular Discord bot—it harnesses the immense power of strong AI to provide you with a unique and enlightening experience. With the simple command **<ask**,you unlock a world of knowledge at your fingertips. Our cutting-edge AI is here to answer any question you have, from trivia to deep inquiries. Just ask, and Pepperoni-X will deliver accurate and insightful responses.Explore the limitless possibilities of knowledge and curiosity with Pepperoni-X's AI capabilities. Whether you're seeking information, pondering a complex problem, or simply engaging in conversation, our AI is ready to assist you. Join us in unlocking the potential of AI-driven interactions today! **")]
                                      
            await Paginator.Simple(timeout=None).start(ctx, pages=embeds)
                   
        
async def setup(bot):
    await bot.add_cog(HelpCommand(bot))