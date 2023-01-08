import discord

call_name = ["socks"]
async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mentions: discord.Message.mentions, args: list[str]):
    """
    returns a custom message meant for socks the top G
    """

    await message.channel.send("master <@463885299223625740>, your milkies are ready.")