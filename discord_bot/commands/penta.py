async def cmd(message, discord, client):

    await message.channel.send("Shutting Off...")
    await client.close()