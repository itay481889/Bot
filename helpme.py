import discord
from discord.ext import commands
import aiohttp 
import asyncio
import google
import sys


client = commands.Bot(command_prefix ='.')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Watching my servers | ItayShimada#0139'))
    print('Bot is ready')





@client.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] 
    number = int(number)
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
    await client.say(f"**I have deleted {len(mgs)} messages for you**")
    


@client.command(aliases=['platform'])
async def plat(ctx):
    await client.say('Running on ' + sys.platform)
















@client.command()
async def square(left : int, right : int):
    """squares two numbers together."""
    await client.say(left * right)


# After that, we add in the add command

@client.command(aliases=['Add', 'ADD'])
async def add(left : int, right : int):
    """Adds two numbers together."""
    await client.say(left + right)

# Finally, we implment the minus command

@client.command(aliases=['Minus', 'MINUS', 'Subtract', 'subtract', 'SUBTRACT'])
async def minus(left : int, right : int):
    """Takes two numbers away."""
    await client.say(left - right)














@client.event
async def on_member_join(member):
    channel = client.get_channel('536996443781726219')
    await client.send_message(channel, f"***:white_check_mark: {member.mention} has joined our server***")
    embed = discord.Embed(title="**{} has joined our server**".format(member.name), description='**Thank you! please read the server rules.**')
    embed.add_field(name="Mention", value=f"{member.mention}", inline=False)
    embed.add_field(name="The Rules", value="https://hastebin.com/ihetifofir.md", inline=False)
    embed.set_thumbnail(url="https://c.slashgear.com/wp-content/uploads/2018/08/discord_main.jpg")
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text='Have fun!')
    await client.send_message(channel, embed=embed)
    await client.send_message(member, "Hello please read the rules by using the command ```!rules```")
    await client.send_message(member, "The prefix is ```.```")





    


@client.event
async def on_member_remove(member):
    channel = client.get_channel('536996443781726219')
    await client.send_message(channel, f"***:x: {member.mention} has left our server...***")
    


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="535975389550608386")
    await client.add_roles(member, role)




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




@client.command(pass_context=True)
async def website():
    await client.say('https://betterserver.webnode.com/')











@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User, *reason: str):
    await client.ban(userName)
    await client.say(f"***:white_check_mark:  {userName} has been banned***")
    embed = discord.Embed(title=f"**Ban {str(userName)}**", description=f"**The user {str(userName)} has banned for {reason}**", color=0xbf0303)
    embed.add_field(name="Mention", value=f"{str(userName.mention)}", inline=False)
    embed.add_field(name="The Rules", value="https://hastebin.com/ihetifofir.md", inline=False)
    embed.set_thumbnail(url="https://c.slashgear.com/wp-content/uploads/2018/08/discord_main.jpg")
    embed.set_image(url="https://cdn.pixabay.com/photo/2016/10/19/09/41/rules-1752536_960_720.png")
    embed.set_footer(text='Please take care.')
    await client.send_message(ctx.message.channel, embed=embed)
       
    


@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def newban(ctx, userName: discord.User, *reason: str):
    await client.ban(userName)
    await client.say(f"***:white_check_mark:  {userName} has been banned***")
    embed = discord.Embed(title=f"**Ban {str(userName)}**", description=f"**The user {str(userName)} has banned for {reason}**", color=0xbf0303)
    embed.add_field(name="Mention", value=f"{str(userName.mention)}", inline=False)
    embed.add_field(name="The Rules", value="https://hastebin.com/ihetifofir.md", inline=False)
    embed.add_field(name='Moderator', value='{}'.format(ctx.message.author.name) + '#{}'.format(ctx.message.author.discriminator))
    embed.set_thumbnail(url="https://c.slashgear.com/wp-content/uploads/2018/08/discord_main.jpg")
    embed.set_image(url="https://cdn.pixabay.com/photo/2016/10/19/09/41/rules-1752536_960_720.png")
    embed.set_footer(text='Please take care.')
    await client.send_message(ctx.message.channel, embed=embed)

#embed.add_field(name='Moderator', value='{}'.format(ctx.message.author.name) + '#{}'.format(ctx.message.author.discriminator))

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User, *reason: str):
    await client.kick(userName)
    await client.say(f"***:white_check_mark:  {userName} has been kicked***")
    embed = discord.Embed(title=f"**Kick {str(userName)}**", description=f"**The user {str(userName)} has kicked for {reason}**", color=0xbf0303)
    embed.add_field(name="Mention", value=f"{str(userName.mention)}", inline=False)
    embed.add_field(name="The Rules", value="https://hastebin.com/ihetifofir.md", inline=False)
    embed.set_thumbnail(url="https://c.slashgear.com/wp-content/uploads/2018/08/discord_main.jpg")
    embed.set_image(url="https://cdn.pixabay.com/photo/2016/10/19/09/41/rules-1752536_960_720.png")
    embed.set_footer(text='Please take care.')
    await client.send_message(ctx.message.channel, embed=embed)









@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *reason: str):
    await client.say(f"***:white_check_mark:  {userName} has been warned***")
    embed = discord.Embed(title=f"**Warn {str(userName)}**", description=f"**The user {str(userName)} has warned for {reason}**", color=0xbf0303)
    embed.add_field(name="Mention", value=f"{str(userName.mention)}", inline=False)
    embed.add_field(name="The Rules", value="https://hastebin.com/ihetifofir.md", inline=False)
    embed.set_thumbnail(url="https://c.slashgear.com/wp-content/uploads/2018/08/discord_main.jpg")
    embed.set_image(url="https://cdn.pixabay.com/photo/2016/10/19/09/41/rules-1752536_960_720.png")
    embed.set_footer(text='Please take care.')
    await client.send_message(ctx.message.channel, embed=embed)
    









@client.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def mute(ctx,member:discord.Member, duration: int, *, reason):
    role = discord.utils.get(member.server.roles, name='Member')
    Mute = discord.utils.get(member.server.roles, name='Mute')
    await client.remove_roles(member, role)
    await client.add_roles(member, Mute)
    await client.say(f"***:white_check_mark:  {str(member.mention)} has been muted***")
    embed = discord.Embed(title=f"**Mute {str(member.mention)}**", description=f"**The user {str(member.mention)} has muted for {duration} because of {reason}**", color=0xbf0303)
    embed.add_field(name="Mention", value=f"{str(member.mention)}", inline=False)
    embed.add_field(name="The Rules", value="https://hastebin.com/ihetifofir.md", inline=False)
    embed.set_thumbnail(url="https://c.slashgear.com/wp-content/uploads/2018/08/discord_main.jpg")
    embed.set_image(url="https://cdn.pixabay.com/photo/2016/10/19/09/41/rules-1752536_960_720.png")
    embed.set_footer(text='Please take care.')
    await client.send_message(ctx.message.channel, embed=embed)
    await asyncio.sleep(duration)
    await client.remove_roles(member, Mute)
    await client.add_roles(member, role)
    
    


    

    
@client.command(pass_context=True)
async def da2():
    message = await client.say("Press the reaction for the role ```example2```")
    await client.add_reaction(message, emoji='\U0001F44D')
    
   
    
    
    




@client.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def unmute(ctx,member:discord.Member):
    role=discord.utils.get(member.server.roles, name='Member')
    Mute=discord.utils.get(member.server.roles, name='Mute')
    await client.remove_roles(member, Mute)
    await client.add_roles(member, role)
    await client.say(f"***:white_check_mark:  {str(member.mention)} has been unmuted***")
    embed = discord.Embed(title=f"**Unmute {str(member.mention)}**", description=f"**The user {str(member.mention)} has unmuted for Auto**", color=0x00ff00)
    embed.add_field(name="Mention", value=f"{str(member.mention)}", inline=False)
    embed.add_field(name="The Rules", value="https://hastebin.com/ihetifofir.md", inline=False)
    embed.set_thumbnail(url="https://c.slashgear.com/wp-content/uploads/2018/08/discord_main.jpg")
    embed.set_image(url="https://cdn.pixabay.com/photo/2016/10/19/09/41/rules-1752536_960_720.png")
    embed.set_footer(text='Please take care.')
    await client.send_message(ctx.message.channel, embed=embed)











@client.command()
async def support():
    await client.say("""```css
Support - All of the commands.
-------------------------------
Mod commands:
Clear - Clear messages.
Ban - Ban's the mentioned user.
Kick - Kick's the mentioned user.
Mute - Mute's the mentioned user.
Unmute - Unmute's the mentioned user.
-------------------------------------
Music commands:
Join - The bot will join the voice channel where the user is.
Leave - The bot will leave the voice channel.
Play - The bot will play the song or the video from the url.
Pause - The bot will pause the music.
Resume - The bot will continue playing the music.
Stop - The bot music system will turn off and the music will stop.
------------------------------------------------------------------
For more info about this commands do:
.I(Name of the command)
Example: .Icommands```""")
    
    

@client.event
async def on_message(message):
    if message.content.startswith('!rules'):
        embed = discord.Embed(title="***Server Rules!***", description="**Hello everyone, please read the server rules!**", color=0x5269ff)
        embed.add_field(name="Creator", value="ItayShimada#0139", inline=False)
        embed.add_field(name="Rules", value="https://hastebin.com/ihetifofir.md", inline=False)
        embed.set_thumbnail(url="https://c.slashgear.com/wp-content/uploads/2018/08/discord_main.jpg")
        embed.set_image(url="https://cdn.pixabay.com/photo/2016/10/19/09/41/rules-1752536_960_720.png")
        embed.set_footer(text='Please send the command "imagree" to accept the rules and see the server.')
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith('imagree'):
        role=discord.utils.get(message.author.server.roles, name='Verified')
        Unverified=discord.utils.get(message.author.server.roles, name='Unverified')
        await client.remove_roles(message.author, Unverified)
        await client.add_roles(message.author, role)
    await client.process_commands(message)
   








    

@client.command(pass_context=True)
async def membercount(ctx):
    await client.say("`{0.name} has this amount of members: {0.member_count}`".format(ctx.message.server))



    
@client.command()
async def Iclear():
    await client.say("""```css
Clear - The command clears the messages by using .clear (amount)
The amount has to be between 2 and 100.```""")





@client.command()
async def Ijoin():
    await client.say("""```css
Join - The bot will join the voice channel where the user is.```""")
  





@client.command()
async def Ileave():
    await client.say("""```css
Leave - The bot will leave the voice channel.```""")







@client.command()
async def Iplay():
    await client.say("""```css
Play - The bot will play the song or the video from the url.```""")




@client.command()
async def Ipause():
    await client.say("""```css
Pause - The bot will pause the music.```""")






@client.command()
async def Iresume():
    await client.say("""```css
Resume - The bot will continue playing the music.```""")







@client.command()
async def Istop():
    await client.say("""```css
Stop - The bot music system will turn off and the music will stop.```""")





@client.command()
async def Iban():
    await client.say("""```css
Ban - The command bans the mentioned user.```""")






@client.command()
async def Ikick():
    await client.say("""```css
Kick - The command kicks the mentioned user.```""")

    
    
@client.command()
async def Icommands():
    await client.say("""```css
Commands - This command gives you a list with helpful commands.```""")




@client.command()
async def Imute():
    await client.say("""```css
Mute - This command mutes the mentioned user.```""")



@client.command()
async def Iunmute():
    await client.say("""```css
Unmute - This command unmutes the mentioned user.```""")


players = {}
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel) 

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server 
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url): 
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()





@client.command(pass_context=True)
async def pause(ctx): 
    id = ctx.message.server.id
    players[id].pause()






@client.command(pass_context=True)
async def stop(ctx): 
    id = ctx.message.server.id
    players[id].stop()





@client.command(pass_context=True)
async def resume(ctx): 
    id = ctx.message.server.id
    players[id].resume()




@client.command()
@commands.has_permissions(manage_messages=True)
async def say(*args):
    output = ''
    for word in args:
        output+=word
        output+= ' '
    await client.say(output)
    



@client.command()
async def cat():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://aws.random.cat/meow") as resp:
            await client.say((await resp.json())["file"])
    


#@client.command(pass_context = True)
#async def createserver(ctx):
#    await client.create_channel(ctx.message.server, 'General 1', type=discord.ChannelType.voice)
#    await client.create_channel(ctx.message.server, 'General 2', type=discord.ChannelType.voice)
#    await client.create_channel(ctx.message.server, 'General Chat', type=discord.ChannelType.text)
#    perms = discord.Permissions(send_messages=True,read_messages=True,manage_messages=True)
#    await client.create_role(ctx.message.server,name="<ROLE_NAME>",permissions=perms)
           
 

Token = 'NTM1NzgyOTQxMzY0NTg0NDQ4.DyNT8g.7-HkB6me2S3RMNdOk0NFltBs9zE'


client.run('NTM1NzgyOTQxMzY0NTg0NDQ4.DyNT8g.7-HkB6me2S3RMNdOk0NFltBs9zE')


    
