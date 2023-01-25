import discord
from datetime import datetime
import utils.profunction as pfunc

context = {
    "name": ["stats"],
    "description": "",
    "format": [
        ["M"],
        []
    ],
    "admin": False
}

async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mention: discord.Message.mentions, args: list[int], format: int):

    profile = pfunc.get_profile(message.author.id)
    stats = {
        "Name": message.author.name,
        "Thimbits": profile['bit'],
        "Thimcoins": profile['coin'],
    }

    embed = discord.Embed(
        title=f"{message.author.name}'s stats",
        color=0xe4b634,
        timestamp=datetime.now()
    )

    stats_str: str
    for key, value in stats.items():
        line = f"{key}: **{value}**"
        embed.add_field(name=line, value="** **", inline=False)

    return await message.channel.send(embed=embed)