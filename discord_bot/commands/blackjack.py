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
async def cmd(bot:discord.Client, message: discord.Message, mention: discord.Member, args: list[int], format: int):
    return await message.channel.send("no, bozo") 
    pass