import discord
from datetime import datetime
import utils.profunction as pfunc

context = {
    "name": ["topbal", "topbalance"],
    "description": "",
    "format": [
        []
    ],
    "admin": False
}

async def cmd(discord: discord, bot:discord.Client, message: discord.Message, mentions: discord.Message.mentions, args: list[int]):

    profiles = {profile['id']: profile['bit'] for profile in pfunc.get_profiles()}
    profiles_sorted = sorted(profiles.items(), key=lambda x:x[1] , reverse=True)

    embed = discord.Embed(
        title="Top 10 Balances",
        color=0xe4b634,
        timestamp=datetime.now()
    )

    for profile in profiles_sorted[:10]:
        line = f"{message.guild.get_member(profile[0]).name}: {profile[1]}"
        embed.add_field(name=line, value="** **", inline=False)

    return await message.channel.send(embed=embed)