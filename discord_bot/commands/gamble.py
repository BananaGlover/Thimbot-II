import discord
import utils.profunction as pfunc
import random

context = {
    "name": ["gamble"],
    "description": "",
    "format": [
        ["I"]
    ],
    "admin": False
}

async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mention: discord.Message.mentions, args: list[int]):

    self = pfunc.get_profile(message.author.id)
    amount = args[0]

    #return if self has no bits
    if self['bit'] <= 0 or self['bit'] < amount:
        return await message.channel.send("you don't have enough Thimbits to gamble")

    if random.choice([True, False]):
        self['bit'] += amount
        await message.channel.send(f"**{message.author.name}** gambled **{amount}** Thimbits and __won__, they now have **{self['bit']}** Thimbits")
    else:
        self["bit"] -= amount
        await message.channel.send(f"**{message.author.name}** gambled **{amount}** Thimbits and __lost__, they now have **{self['bit']}** Thimbits")

    return pfunc.modify_profile(self)