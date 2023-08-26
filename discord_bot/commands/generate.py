import discord
import utils.profunction as pfunc

context = {
    "name": ["generate,", "gen"],
    "description": "",
    "format": [
        ["I"]
    ],
    "admin": True
}

async def cmd(bot:discord.Client, message: discord.Message, mention: discord.Member, args: list[int], format: int):
    
    self = pfunc.get_profile(message.author.id)
    self['bit'] += args[0]
    pfunc.modify_profile(self)

    return await message.channel.send(f"**{message.author.name}** generated {args[0]} Thimbits, they now have **{self['bit']}** Thimbits")