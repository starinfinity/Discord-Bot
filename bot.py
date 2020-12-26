import os

import discord
import messagereader as mr
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('sg'):
        await message.channel.send(mr.message_reader(message.author.name, message.content.lower()))

client.run('add Discord token here or replace with os.getenv(\'TOKEN\') and add there')
