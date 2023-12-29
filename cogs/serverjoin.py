from discord.ext import commands
import discord
import aiohttp
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
from database import Server
from peewee import *




webhook_url = "https://discord.com/api/webhooks/1168233581148119080/jV1okpd5JE7Mr9SMY5BOP5cNG6kL5iHUN2fqzYNznQVqauXgaxTAOOHI_pbatSwwbZQF"
webhook = DiscordWebhook(url=webhook_url)

class JoinServer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        server_name = guild.name
        try:
            server_count = len(self.bot.guilds)
            embed = DiscordEmbed(title=f"Bot has joined the server: {server_name}",color="03b2f8")
            embed.set_image(url='https://images-ext-2.discordapp.net/external/Faf6_WsYfq41ckjX83I8Tkd2LJguZqgJqM1j_eG-HmE/https/1.bp.blogspot.com/-IR7xnX3-V1E/Wa94ttVHldI/AAAAAAAACBk/KQBW5JEf5jwnmJWAyioDMU5xwUinERunwCLcBGAs/s1600/CutePizzaRun.gif?width=500&height=281')
            embed.set_footer(text=f'Server joined : {server_count}')
            webhook.add_embed(embed)
            response = webhook.execute()
        except Exception as e:
                print(f'Error in sending webhook: {e}')

    current_day = datetime.now().strftime("%A")
    print(current_day)


async def setup(bot):
    await bot.add_cog(JoinServer(bot))
