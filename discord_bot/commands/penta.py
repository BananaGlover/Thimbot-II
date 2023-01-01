async def cmd(message, discord, client):

    await message.channel.send("Shutting Off...")
    #shuts down the bot
    await client.close()