import discord

call_name = ["penta"]
async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mentions: discord.Message.mentions, args: list[str]):
    """
    returns
    """

    await message.channel.send("Shutting Off...")

    #shuts down the bot
    await bot.close()