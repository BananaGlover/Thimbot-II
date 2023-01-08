import discord
from datetime import datetime

call_name = ["debug, dbg"]
async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mentions: discord.Message.mentions, args: list[str]):
    """
    returns embed with all of target's user attributes.
    """
    
    if len(args) > 0 and message.guild.get_member(int(args[0][2:-1])):
        target = discord.User = message.guild.get_member(int(args[0][2:-1]))
    else:
        target = message.author

    embed = discord.Embed(
        title=target.name,
        color=0x00ff00,
        timestamp=datetime.now()
    )

    #list of field to be added later
    stats: list = []
    attr_lst = [a for a in dir(target) if not a.startswith("_") and not callable(getattr(target, a))]
    for attr in attr_lst:
        stats.append([attr, getattr(target, attr)])

    #implement fields
    for line in stats:
        embed.add_field(name=line[0], value=line[1], inline=False)

    await message.channel.send(embed=embed)