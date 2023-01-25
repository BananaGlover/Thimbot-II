import discord

context = {
    "name": ["blackjack"],
    "description": "",
    "format": [
        []
    ],
    "admin": False
}

#HIT, STAND, SPLIT, DOUBLE
async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mention: discord.Message.mentions, args: list[int]):
    return await message.channel.send("no, bozo") 
    pass