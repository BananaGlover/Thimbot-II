from importlib.machinery import SourceFileLoader
from dotenv import load_dotenv

import utils.profunction as pfunc
import utils.markfunction as mfunc

from datetime import datetime
import asyncio
import os

import discord

PREFIX = "$"

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = discord.Client(intents= discord.Intents.all())

#when bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to discord")

    while True:
        mfunc.update()
        await asyncio.sleep(int((60/mfunc.UPDATE_PER_HOUR)*60))



#when bot disconnects from discord
@bot.event
async def on_disconnect():
    print(f"{bot.user.name} has disconnected to discord")



#when bot receives message
@bot.event
async def on_message(message: discord.Message):

    #return if message is from bot or without prefix
    if message.author == bot.user or not message.content.startswith(PREFIX): return

    #CHECK IF USER HAS PROFILE: NO -> MAKE ONE + EXEC CMD || YES -> EXEC CMD;
    if not pfunc.check_id(message.author.id):
        pfunc.make_profile(message.author)

    #get content = mentions + arguments
    content = message.content.split()[1:]
    message_cmd = message.content.split()[0][1:].lower()

    #go through every *command*.py in commands folder
    for cmd in os.listdir("commands"):

        path = os.path.join("commands", cmd)
        if not os.path.isfile(path): continue

        #get cmd path then execute it
        cmd_import = SourceFileLoader(cmd, path).load_module()

        #if given name is in command's names
        if message_cmd in cmd_import.context['name']:                

            #assign mention
            if message.mentions: mention = message.mentions[0]
            else: mention = None

            pass_args: list[int] = []
            pass_mention = None

            #########################    MOLD ALRORITHM    #########################

            correct:bool = False

            #TO FIX -> MANAGE MULTIPLE FORMAT AND EXPECTING THEM
            
            #loop through every format
            for format in cmd_import.context['format']:

                print(f"format: {format}, content: {content}")

                if len(format) == 0 and len(content) == 0:
                    correct = True
                    break 

                #compare format[i] to given 
                for index in range(len(content)):
                    given = content[index].lower()
                    expected = format[index]

                    #MAKE "ALL" CONVERSION TO MAX BIT
                    if given == "all":
                        given = str(pfunc.get_profile(message.author.id)['bit'])

                    if mention and given == f"<@{mention.id}>": #GIVEN MENTION

                        if not pfunc.get_profile(mention.id):
                            return await message.channel.send(f"**{mention.name}** doesn't have a profile")

                        if expected == "M": pass_mention = mention
                        else: return await message.channel.send(f"ERROR: WAS NOT EXPECTING MENTION")

                    elif given.isdigit(): #GIVEN INT

                        if expected == "I": pass_args.append(int(given))
                        else: return await message.channel.send("ERROR: WAS NOT EXPECTING INT")

                    else:
                        if expected == "S": pass_args.append(str(given))
                        else: return await message.channel.send("ERROR: WAS NOT EXPECTING STRING")

                    if index == len(content) - 1:
                        correct = True
                        break

                if correct:
                    break

            if correct != True:
                return await message.channel.send("INVALID FORMAT")

            ######################################################################

            #RETURNS IF NOT ADMIN TRY TO EXECUTE ADMIN COMMAND
            if message.author.guild_permissions.administrator == False and cmd_import.context['admin'] == True:
                return await message.channel.send("only administators can run this command")

            #debug prints
            print(f"\n[{datetime.now()}]")
            print(f"user: {message.author.name}")
            print(f"cmd: {message.content}")
            print(f"args: {pass_args}")
            print(f"mention: {pass_mention}\n")

            #sends: discord module, bot, current message, mention's id, args
            return await cmd_import.cmd(discord, bot, message, pass_mention, pass_args)

bot.run(TOKEN) 