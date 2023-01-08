from importlib.machinery import SourceFileLoader
from dotenv import load_dotenv
import profunction as pfunc
import os

import discord

PREFIX = "$"

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = discord.Client(intents= discord.Intents.all())

#when bot is ready
@bot.event
async def on_ready():
   
 print(f"{bot.user} has connected to discord")
#when bot disconnects from discord
@bot.event
async def on_disconnect():
    print(f"{bot.user} has disconnected to discord")

#when bot receives message
@bot.event
async def on_message(message: discord.Message):

    #return if message is from bot or without prefix
    if message.author == bot.user or not message.content.startswith(PREFIX): return

    #CHECK IF USER HAS PROFILE: NOT=MAKE ONE + EXEC CMD; YES=EXEC CMD;
    if not pfunc.check_id(message.author.id):
        pfunc.make_profile(message.author)

    #get command and arguments in message
    message_cmd = message.content.split(" ")[0][1:].lower()
    args = message.content.split(" ")[1:]
    
    #debug prints
    print(f"{message.author.name}: {message.content}")
    print(f"args: {[arg for arg in args if len(arg) > 0]}\nmentions: {[user.id for user in message.mentions]}")

    #go through every *command*.py in commands folder
    for cmd in os.listdir("commands"):

        path = os.path.join("commands", cmd)
        if not os.path.isfile(path): continue

        #get cmd path then execute it
        cmd_import = SourceFileLoader(cmd, path).load_module()
        if message_cmd in cmd_import.call_name:

            #sends: discord module, bot, current message, mention's id, args
            await cmd_import.cmd(discord, bot, message, [user.id for user in message.mentions], [arg for arg in args if len(arg) > 0])

            break

bot.run(TOKEN) 