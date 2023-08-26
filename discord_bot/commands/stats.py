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

async def cmd(bot:discord.Client, message: discord.Message, mention: discord.Member, args: list[int], format: int):
    
    target = pfunc.define_target(mention, message.author)
    target_member = message.guild.get_member(target['id'])

    stats = {
        "Name": target_member.name,
        "Thimbits": target['bit'],
        "Thimcoins": target['coin'],
    }

    embed = discord.Embed(
        title=f"{target_member.name}'s stats",
        color=0xe4b634,
        timestamp=datetime.now()
    )

    for key, value in stats.items():
        line = f"{key}: **{value}**"
        embed.add_field(name=line, value="** **", inline=False)

    return await message.channel.send(embed=embed)