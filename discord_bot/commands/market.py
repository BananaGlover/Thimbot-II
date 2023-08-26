import discord
import utils.markfunction as mfunc
import utils.profunction as pfunc
from datetime import datetime

context = {
    "name": ["market"],
    "description": "",
    "format": [
        ["S", "I"]
    ],
    "admin": False
}

async def cmd(bot:discord.Client, message: discord.Message, mention: discord.Member, args: list[int], format: int):

    func = args[0]
    num = args[1]
    profile = pfunc.get_profile(message.author.id)
    
    if func == "see":
        if not 0 < num < 25:
            return await message.channel.send("you can only see data from 1H to 24H")

        mfunc.generate_graph(num)
        graph = discord.File("./images/graph.png")
        
        embed = discord.Embed(
        title=f"MARKET",
        color=0xe4b634,
        timestamp=datetime.now()
        )

        return await message.channel.send(file=graph)

    elif func == "buy":

        price = mfunc.get_latest_data() * num
        if profile['bit'] >= price:
            #enough to buy x coin

            profile['bit'] -= price
            profile['coin'] += num
            pfunc.modify_profile(profile)

            return await message.channel.send(f"**{message.author.name}** succesfully bought **{num}** Thimcoins for **{price}** Thimbits, they now have **{profile['coin']}** Thimcoins")

        else:
            #not enough
            return await message.channel.send(f"**{message.author.name}** doesn't have enough to buy **{num}** Thimcoins for **{price}** Thimbits")
        

    elif func == "sell":
        
        price = mfunc.get_latest_data() * num
        if profile['coin'] < num:
            #selling too many coins
            return await message.channel.send("you don't have enough Thimcoins")
        else:
            #enough coins
            profile['coin'] -= num
            profile['bit'] += price
            pfunc.modify_profile(profile)

            return await message.channel.send(f"**{message.author.name}** succesfully sold **{num}** Thimcoins for **{price}** Thimbits, they now have **{profile['bit']}** Thimbits")
