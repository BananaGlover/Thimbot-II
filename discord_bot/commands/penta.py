import discord

context = {
    "name": ["penta"],
    "description": "",
    "format": [
        []
    ],
    "admin": True
}

async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mentions: discord.Message.mentions, args: list[int]):

    await message.channel.send("Shutting Off...")

    #shuts down the bot
    await bot.close()