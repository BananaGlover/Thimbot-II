import discord
import utils.profunction as pfunc

context = {
    "name": ["balance", "bal"],
    "description": "",
    "format": [
        ["M"],
        []
    ],
    "admin": False
}

async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mention: discord.Member, args: list[int]):

    target = pfunc.define_target(mention, message.author)

    return await message.channel.send(f"**{message.guild.get_member(target['id']).name}** has **{target['bit']:,}** Thimbits")