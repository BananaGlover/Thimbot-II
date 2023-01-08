import discord
import profunction as pfunc

call_name = ["give"]
async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mentions: discord.Message.mentions, args: list[str]):
    """
    allows user to give coin to another user
    """

    #$give {mention} {amount}

    #COMMAND INTEGRETY CHECKS
    if len(args) != 2:
        return await message.channel.send("```$give [@user] [amount] (1)```")
    elif len(mentions) != 1:
        return await message.channel.send("```$give [@user] [amount] (2)```")
    elif mentions[0] != int(args[0][2:-1]):
        return await message.channel.send("```$give [@user] [amount] (3)```")
    elif not args[1].isdigit():
        return await message.channel.send("```$give [@user] [amount] (4)```")

    if mentions[0] == message.author.id:
        return await message.channel.send("You cannot give Thimbits to yourself bozo")

    if pfunc.check_profile(mentions[0]):
        target = pfunc.get_profile(mentions[0])
    amount = int(args[1])

    #AMOUNT CHECK
    if pfunc.get_profile(message.author.id)['coin'] < amount:
        return await message.channel.send(f"**{message.author.name}** has not enough Thimbits")

    target['coin'] += amount
    pfunc.modify_profile(target)

    sender = pfunc.get_profile(message.author.id)
    sender['coin'] -= amount
    pfunc.modify_profile(sender)

    return await message.channel.send(f"**{message.author.name}** succesfully gave **{amount}** Thimbits to **{message.guild.get_member(mentions[0]).name}**")
    



    #CHECK IF TARGET HAS PROFILE -> YES: CONTINUE; NO: RETURN

    #CHECK IF SENDER HAS ENOUGH -> YES: CONTINUE; NO: RETURN

    #REMOVE COIN FROM SENDER / ADD COIN TO TARGET

    #SEND CONFIRMATION MESSAGE