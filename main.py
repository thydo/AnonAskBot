import discord
import os
from dotenv import load_dotenv

client = discord.Client()
load_dotenv()
TOKEN = os.getenv('TOKEN')

vetchannel = 845573121998323732

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.guild is None and message.content.startswith('!ask'):
        await message.channel.send('Thanks for submitting a question!')
        

client.run(TOKEN)
