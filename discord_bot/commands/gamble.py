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

async def cmd(bot:discord.Client, message: discord.Message, mention: discord.Member, args: list[int], format: int):
    
    profile = pfunc.get_profile(message.author.id)
    amount = args[0]

    #return if self has no bits
    if profile['bit'] < amount:
        return await message.channel.send("you don't have enough Thimbits to gamble")

    if random.choice([True, False]):
        profile['bit'] += amount
        await message.channel.send(f"**{message.author.name}** gambled **{amount}** Thimbits and __won__, they now have **{profile['bit']}** Thimbits")
    else:
        profile["bit"] -= amount
        await message.channel.send(f"**{message.author.name}** gambled **{amount}** Thimbits and __lost__, they now have **{profile['bit']}** Thimbits")

    return pfunc.modify_profile(profile)