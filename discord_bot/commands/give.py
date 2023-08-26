import discord
import utils.profunction as pfunc

context = {
    "name": ["give"],
    "description": "",
    "format": [
        ["M", "I"]
    ],
    "admin": False
}

async def cmd(bot:discord.Client, message: discord.Message, mention: discord.Member, args: list[int], format: int):
    
    #initialise variables
    self = pfunc.get_profile(message.author.id)
    target = pfunc.get_profile(mention.id)

    amount = args[0]

    #AMOUNT CHECK
    if pfunc.get_profile(message.author.id)['bit'] < amount:
        return await message.channel.send(f"**{message.author.name}** has not enough Thimbits")

    #add bit to target
    target['bit'] += amount
    pfunc.modify_profile(target)

    #remove bit to self
    self['bit'] -= amount
    pfunc.modify_profile(self)

    return await message.channel.send(f"**{message.author.name}** succesfully gave **{amount}** Thimbits to **{mention.name}**")