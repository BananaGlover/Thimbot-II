import discord

context = {
    "name": ["socks"],
    "description": "",
    "format": [
        []
    ],
    "admin": False
}

async def cmd(bot:discord.Client, message: discord.Message, mention: discord.Member, args: list[int], format: int):
    
    await message.channel.send("master <@463885299223625740>, your milkies are ready.")