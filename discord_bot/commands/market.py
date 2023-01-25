import discord
import utils.markfunction as mfunc

context = {
    "name": ["market"],
    "description": "",
    "format": [
        ["I"],
        ["S", "I"]
    ],
    "admin": False
}

async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mention: discord.Message.mentions, args: list[int]):

    hour = args[0]
    if not 0 < hour < 25:
        return await message.channel.send("you can only see data from 1H to 24H")

    mfunc.generate_graph(hour)
    graph = discord.File("./images/graph.png")
    return await message.channel.send(file=graph)