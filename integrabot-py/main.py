#this is a Python project
import discord
import os
from datetime import datetime
import pytz
import requests
import json
import re
import random
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()


def get_IDtime():
    current_time = datetime.now().strftime("%H:%M:%S")
    return("WIB: " + current_time)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n" + json_data[0]['a']
    return(quote)


def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    # print(response.joke)
    json_data = json.loads(response.text)
    return(json_data['setup']+"\n" + "||"+json_data["delivery"]+"||")


def get_meme():
    response = requests.get("https://memeapi.pythonanywhere.com/")
    # print(response.joke)
    json_data = json.loads(response.text)
    return(json_data["memes"][0]["url"])


# print(get_meme())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello! @here')

    if message.content.startswith('!help'):
        await message.channel.send("""List of active commands:\n
        1) !wib - WIB Time \n
        2) !quote - Tell me a quote! \n
        3) !joke - Tell me a joke! \n
        4) !meme - Send me a meme!
        """)

    if message.content.startswith('!wib'):
        IDTime = get_IDtime()
        await message.channel.send(IDTime)

    if message.content.startswith('!quote'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('!joke'):
        joke = get_joke()
        await message.channel.send(joke)

    if message.content.startswith('!meme'):
        meme = get_meme()
        await message.channel.send(meme)

# print(os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))
