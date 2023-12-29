from discord.ext import commands
import discord
from peewee import *
from database import Server
import settings

db = SqliteDatabase('database.db')
db.connect()



class SimpleView(discord.ui.View):
    
    foo : bool = None
    
    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)
    
    async def on_timeout(self) -> None:
        await self.message.channel.send("Timedout")
        await self.disable_all_items()
    
    @discord.ui.button(label="Hello", 
                       style=discord.ButtonStyle.success)
    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel.name
        await interaction.response.send_message(f"The notification has been activated at {channel}")
        self.foo = True
        self.stop()
        
    @discord.ui.button(label="Cancel", 
                       style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Cancelling")
        self.foo = False
        self.stop()




class FavouriteGameSelect(discord.ui.Select):
    def __init__(self):
        options = [ 
                   discord.SelectOption(label="Cs", value="cs"),
                   discord.SelectOption(label="Minecraft", value="mc"),
                   discord.SelectOption(label="Fortnite", value="f"),
        ]
        super().__init__(options=options, placeholder="What do you like to play?", max_values=2)

    async def callback(self, interaction:discord.Interaction):
        await self.view.respond_to_answer2(interaction, self.values)
class SurveyView(discord.ui.View):
    answer1 = None 
    answer2 = None 
    
    @discord.ui.select(
        placeholder="What background color do you want ?",
        options=[
            discord.SelectOption(label="blue", value="blue"),
            discord.SelectOption(label="purple", value="purple"),
            discord.SelectOption(label="pink", value="pink"),
            discord.SelectOption(label="yellow", value="yellow")

        ]        
    )
    async def select_age(self, interaction:discord.Interaction, select_item : discord.ui.Select):
        self.answer1 = select_item.values
        self.children[0].disabled= True
        await interaction.message.edit(view=self)
        await interaction.response.defer()
        self.stop()


class ColorSettings(commands.Cog):

    def __init__(self , bot):
        self.bot = bot
        self.bod = False

    @commands.hybrid_group()
    async def settings(self, ctx):
        """
        Settings group command.
        """
        if ctx.invoked_subcommand is None:
            await ctx.send("Use one of the subcommands: theme, notification, diactive_notification")

    @settings.command()
    async def theme(self , ctx):
        """
        Change the background color
        """
        query = Server.select()
        server_guild = ctx.guild.id

        for item in query:
            if str(item.serverGuild) == str(server_guild):
                self.bod = True
                print("here")
                view = ViewMetadata()
                await view.wait()

                results = {
                    'a1':view.anwser1,
                }
                
    @settings.command()
    async def notification(self , ctx , goal : int):
        """
        Set an achievement for active voices
        """
        server =  ctx.guild.id
        channel = ctx.channel
        try:
            Server.get(Server.serverGuild == server)
            await ctx.send(f"The notification has been activated at {channel.name} with {goal} voice active goal. Let's do it")
            Server.update(notification=True , channelNotification=channel.id , numberNotification=goal).where(Server.serverGuild == server).execute()
        except:
            await ctx.send("voice monitoring message is not active. For unlock use this command '/voice'")


    @settings.command()
    async def deactive_notification(self , ctx):
        """
        deactive nonification option
        """
        server =  ctx.guild.id
        try:
            Server.get(Server.serverGuild == server)
            await ctx.send(f"The notification has been deactivated")
            Server.update(notification=False).where(Server.serverGuild == server).execute()
        except:
            await ctx.send("voice monitoring message is not active. For unlock use this command '/voice'")

async def setup(bot):   
    await bot.add_cog(ColorSettings(bot))