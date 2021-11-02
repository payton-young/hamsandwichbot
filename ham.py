import discord
import os
import requests
import json

from discord.ext import commands


#HAM is a project by Payton Young, this code started from an easily found disocrdbot template
#template link can be found in first commit
#this project is to practice utilzing python libraries and maintaing version control

#testing zenquotes api functionality
#combined functions from multiple tutorials to get a better understanding of pythons
#logic and operation flow
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
    #await bot.process_commands

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    #necessary so every message is interreted and then passed to commands
    #can include more text based logic if need be such as an automated response
    
    await bot.process_commands(message)

@bot.command()
async def inspire(ctx):
    print("debugging message")
    quote = get_quote()
    await ctx.send(quote)     

@bot.command()
async def test (ctx,arg):
    await ctx.send(arg)


f = open("../token","r")
token = f.read()
bot.run(token)
