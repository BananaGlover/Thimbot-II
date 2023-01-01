from importlib.machinery import SourceFileLoader
import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"{client.user} has connected to discord")

@client.event
async def on_disconnect():
    print(f"{client.user} has disconnected to discord")

@client.event
async def on_message(message: discord.Message):
    #return if message is from bot
    if message.author == client.user:
        return

        #check if message is command
    for cmd in os.listdir("discord_bot\commands"):

        path = os.path.join("discord_bot\commands", cmd)
        if not os.path.isfile(path): continue

        if message.content == cmd[:-3]:

            #get cmd path then execute it
            cmd_import = SourceFileLoader(cmd, path).load_module()

            await cmd_import.cmd(message, discord, client)

client.run(TOKEN)