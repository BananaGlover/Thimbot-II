import discord
import profunction as pfunc

call_name = ["balance", "bal"]
async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mentions: discord.Message.mentions, args: list[str]):
    """
    returns user's balance
    """

    if len(args) > 1:
        return await message.channel.send("```$bal [@user] (1)```")


    if len(mentions) > 0:
        if pfunc.check_profile(mentions[0]):
            target = pfunc.get_profile(mentions[0])
    else:
        target = pfunc.get_profile(message.author.id)

    await message.channel.send(f"**{message.guild.get_member(target['id']).name}** has **{target['coin']:,}** Thimbits")

    