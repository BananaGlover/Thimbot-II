import discord

context = {
    "name": ["penta"],
    "description": "",
    "format": [
        []
    ],
    "admin": True
}

async def cmd(bot:discord.Client, message: discord.Message, mention: discord.Member, args: list[int], format: int):
    
    await message.channel.send("Shutting Off...")

    #shuts down the bot
    await bot.close()