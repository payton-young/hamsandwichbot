import discord
import os

#HAM is a project by Payton Young, this code started from an easily found disocrdbot template
#below is the template
#https://discordpy.readthedocs.io/en/latest/quickstart.html#a-minimal-bot

#this project is to practice utilzing python libraries and maintaing version control

#token can't be publically assigned for security reasons
#can't be uploaded to github
#will keep token locally and perhaps figure out secure distribution

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
        


client.run(os.getenv('TOKEN'))