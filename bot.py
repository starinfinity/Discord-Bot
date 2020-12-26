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
    # if message.content.startswith('sg hi'):
    #     await message.channel.send('Hello! ' + nc.namecaller())
    # if message.content.startswith('sg bye'):
    #     await message.channel.send('bye! ' + nc.namecaller())
    # if message.content.startswith('sg yomomma'):
    #     await message.channel.send(ym.yomomma())
    # if message.content.startswith('sg currency'):
    #     await message.channel.send('i am still setting up the bank')
    # if message.content.startswith('sg help'):
    #     await message.channel.send(help.helper())
    # if message.content.startswith('sg roast'):
    #     await message.channel.send(roast.roaster())
    # if message.content.startswith('sg die'):
    #     await message.channel.send('First, i will kill you. Bitch!')
    # if message.content.startswith('sg pickup'):
    #     await message.channel.send(pick.pickup())

client.run('add Discord token here or replace with os.getenv(\'TOKEN\') and add there')
