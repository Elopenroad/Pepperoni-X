from discord.ext import commands
import discord
from chart.voice_active import voice
from database import Server
from peewee import *


online = 0
voiceActive = 0
channel_id = None
voice_active_message = None
activerecommendation = True
voice_active_message_id = None


db = SqliteDatabase('database.db')
db.connect()


class VoiceActive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice_active_message = None
        self.channel_id = None

    @commands.hybrid_command()
    async def voice(self, ctx):
        """
        A live chart for monitoring voice status
        """
        global voice_active_message

        try:
            server = ctx.guild.id
            message = Server.get(Server.serverGuild == server)
            voice_active_message = await self.bot.get_channel(int(message.channelId)).fetch_message(int(message.MessageId))
            message.delete_instance()
            await voice_active_message.delete()
        except Server.DoesNotExist:
            print("Server record not found")
        except discord.NotFound:
            print("Voice Message Not Found")
        except Exception as e:
            print(f"An error occurred: {e}")
        server_id = ctx.guild.id
        print("Error not from here")
        if ctx.author.guild_permissions.administrator:
            global channel_id 
            global online
            global voiceActive
            global activerecommendation


            channel_id = ctx.channel.id
            member_count = ctx.guild.member_count
            online = sum(1 for member in ctx.guild.members if member.status != discord.Status.offline)


            for voice_channel in ctx.guild.voice_channels:
                voiceActive += len(voice_channel.members) 
            
            urlvoice = voice(online=online, voiceActive=voiceActive , backgroundcolor='white')
            embed = discord.Embed(color=discord.Color.from_rgb(128,251,241),title="Server Live Analyzing", description=f"""***You got {online} online members
                                                                                        And\n {voiceActive} voice active right now***""").set_image(url=urlvoice)
            global voice_active_message_id
            voice_active_message = await ctx.send(embed=embed)
            voice_active_message_id = voice_active_message.id
            server = ctx.guild.id
            print(server)
            Server.create(serverGuild=server , MessageId=voice_active_message_id  ,channelId=channel_id  ,theme='white', channelNotification="None" ,numberNotification=0)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        server_id = member.guild.id
        try:
            guild_record = Server.get(Server.serverGuild == server_id)
        except Server.DoesNotExist:
            print(f"Server record with serverGuild {server_id} not found.")
            return

        if guild_record is None:
            print("guild_record is None")
            return

        if guild_record.channelId is None:
            print('Channel Not found')
            return

        if before.channel != after.channel:
            await self.update_voice_active_message(member.guild)
            if guild_record.notification == True:
                if after.channel:
                    voice_members_count = len(after.channel.members)
                    goal = guild_record.numberNotification
                    if voice_members_count >= goal:
                        channel = self.bot.get_channel(int(guild_record.channelNotification))
                        embed = discord.Embed(title='**Achievement Accomplished**',color=discord.Color.blue(),
                                            description="Congratulations on your remarkable achievement! "
                                                        "Your dedication and hard work have truly paid off. Well done!")
                        embed.set_image(url='https://images-ext-1.discordapp.net/external/RId0oBG6wHrEXospMRPiAM0Pa5bSVW0ZUpL9Wo7GC7c/https/image.tensorartassets.com/posts/images/634544442883306222/61aa3828-f3f8-4e0b-b8c9-49018b125c68.gif?width=405&height=607')

                        await channel.send(embed=embed)
                        
    async def update_voice_active_message(self, guild):
        server_id = guild.id
        try:
            guild_record = Server.get(Server.serverGuild == server_id)
            print(f" Server theme from voice listener{guild_record.theme} from {server_id} as {guild_record.serverGuild} database")

        except Server.DoesNotExist:
            # Handle the case where the record doesn't exist (e.g., create a new record)
            # You can also print a message for debugging.
            print(f"Server record with serverGuild {server_id} not found.")
            return
        global voiceActive
        global online
        global activerecommendation
        global voice_active_message
        global voice_active_message_id


        voiceActive = 0
        online = 0 
        for member in guild.members:
            if member.status != discord.Status.offline:
                online += 1
        for voice_channel in guild.voice_channels:
            voiceActive += len(voice_channel.members)
        print(f"{str(guild_record.theme)} the color before request")
        if guild_record.MessageId:
            urlvoice = voice(online=online, voiceActive=voiceActive , backgroundcolor=str(guild_record.theme))
            try:
                print(guild_record.MessageId)
                voice_active_message = await self.bot.get_channel(int(guild_record.channelId)).fetch_message(int(guild_record.MessageId))
            except discord.NotFound:
                # Handle the case where the message is not found
                print('Message not found')
                return

            embed = discord.Embed(
                color=discord.Color.from_rgb(128, 251, 241),
                title="Server Live Analyzing",
                description=f"""***You got {online} online members
                                        And\n {voiceActive} voice active right now***"""
            ).set_image(url=urlvoice)

            # Edit the message's embed
            await voice_active_message.edit(embed=embed)
            

async def setup(bot):
    await bot.add_cog(VoiceActive(bot))
    