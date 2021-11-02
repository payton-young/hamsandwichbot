import discord
import os
import requests
import json

from discord.ext import commands


#HAM is a project by Payton Young, this code started from an easily found disocrdbot template
#template link can be found in first commit
#this project is to practice utilzing python libraries and maintaing version control

#can't be uploaded to github
#will keep token locally and perhaps figure out secure distribution

#testing zenquotes api functionality

"""
Changing from client class to bot class since bot is a subclass of client and provides more features
"""
description = "HAM is a project by Payton Young"

#client = discord.Client()
bot = commands.Bot(command_prefix='!', description=description)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)     
        
f = open("../token","r")
token = f.read()
bot.run(token)