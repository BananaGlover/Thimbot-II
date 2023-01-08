import discord

call_name = ["ping"]
async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mentions: discord.Message.mentions, args: list[str]):
    """
    returns mention to the message sender
    """


    await message.channel.send(message.author.mention)