import discord
import os
import requests
import json

#HAM is a project by Payton Young, this code started from an easily found disocrdbot template
#template link can be found in first commit
#this project is to practice utilzing python libraries and maintaing version control

#can't be uploaded to github
#will keep token locally and perhaps figure out secure distribution

#testing zenquotes api functionality

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
        
f = open("../token","r")
token = f.read()


client.run(token)