# main.py
import os

import discord

from dotenv import load_dotenv

#loads the Token from the .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
#What data we want to read from the api

#Establishes intents which are the permissions for the bot
intents = discord.Intents.default()

#Enables intent allowing the bot to read other user's messages
intents.message_content = True

#Creates an instance of the Client class that will be used to work with the bot
client = discord.Client(intents = intents) 

############################################################################

@client.event
#Event Listener for when the bot is turned online
async def on_ready():
    print(f"{client.user} has connected to Discord!")

    #Creates a counter to keep track of how many servers the bot is in
    guild_count = 0

    #Loops through each server this bot is in
    for guild in client.guilds:

        #prints the server's ID and Name
        print(f"- {guild.id} (name: {guild.name})")

        #Increments the guild counter
        guild_count += 1

    print(f"{client.user} is in {guild_count} servers")

############################################################################

@client.event

async def on_message(message):

    #Checks if the message that was sent is equal to "Hello"

    if message.content.lower() == "hello":

        await message.channel.send("hello user!")

############################################################################

#Runs the bot using the Token
client.run(TOKEN)