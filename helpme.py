import discord
from discord.ext import commands

client = commands.Bot(command_prefix ='.')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Twitch.com/ShimadaBot'))
    print('Bot is ready')

    
    
@client.command(pass_context=True)
async def whois(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description='Here is what I could find:', color=ctx.message.author.color)
    embed.add_field(name='Name', value='{}'.format(user.name))
    embed.add_field(name='ID', value='{}'.format(user.id), inline=True)
    embed.add_field(name='Status', value='{}'.format(user.status), inline=True)
    embed.add_field(name='Highest Role', value='<@&{}>'.format(user.top_role.id), inline=True)
    embed.add_field(name='Joined at', value='{:%d/%h/%y at %H:%M}'.format(user.joined_at), inline=True)
    embed.add_field(name='Created at', value='{:%d/%h/%y at %H:%M}'.format(user.created_at), inline=True)
    embed.add_field(name='Discriminator', value='{}'.format(user.discriminator), inline=True)
    embed.add_field(name='Playing', value='{}'.format(user.game))
    embed.set_footer(text="{}'s Info".format(user.name), icon_url='{}'.format(user.avatar_url))
    embed.set_thumbnail(url=user.avatar_url)
    await client.send_message(ctx.message.channel, embed=embed)
    
    
    
    
    
    
    

client.run("NTQyMDczNTcxNTkwMDEyOTM5.Dzos8g.35BRQZJ2kPsiNFdTVTnSdY40rms")
