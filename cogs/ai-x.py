import requests
from discord.ext import commands
import json






class AIX(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx, *, message):
        server = ctx.guild.id
        myServer = 1135247310226468926
        channel = ctx.channel.id
        myChannel = 1168229070820098139
        if server == myServer:
            if channel == myChannel:
                url = 'https://www.chatbase.co/api/v1/chat'
                headers = {
                    'Authorization': 'Bearer c2529c04-dfbc-4d81-8cae-84230518824c',
                    'Content-Type': 'application/json'
                }
                data = {
                    "messages": [
                        {"content": f"{message}", "role": "user"}
                    ],
                    "chatbotId": "BWvFpTutFsmPhJBLQl4wx",
                    "stream": False,
                    "temperature": 0
                }

                response = requests.post(url, headers=headers, data=json.dumps(data))
                json_data = response.json()

                if response.status_code == 200:
                    await ctx.send(f"**{json_data['text']}**")
                else:
                    await ctx.send('Error: ' + json_data['message'])
        else:
            await ctx.send("You're only able to use Pepperoni-X AI in Support server")


async def setup(bot):
    await bot.add_cog(AIX(bot))