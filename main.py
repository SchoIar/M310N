
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import discord
import asyncio
import requests
import random
from discord.ext import tasks

#counter = 1
#meow
intents = discord.Intents.all() #MUST ALSO ADD iNTENTS IN DISCORD DEV PORTAL
bot = commands.Bot(command_prefix='.', help_command=None, intents = intents, case_insensitive=True)
bot.remove_command("help")

initial_extensions = ['cogs.music']
for extension in initial_extensions:
    bot.load_extension(extension)

@bot.event
async def on_ready():
    print('Logged in as')
    a = bot.user
    print(f"    {a}")
    print('-====-------=====-')
    print(bot.user.id)
    print('-====-------=====-')
    await bot.change_presence(activity=discord.Game(name="Missile Wars: play.ultimamc.net"))

@bot.event #requires intents 
async def on_member_join(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}. Please read the rules & enjoy your stay!'.format(member, guild)
            await guild.system_channel.send(to_send)
        else:
            to_send = 'Welcome {0.mention} to {1.name}! Please read the rules and enjoy your stay!'.format(member, guild)
            await member.send(to_send)

@bot.event #nothing here thusfar, not sure what u'd like added.
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command()
async def help(ctx):
        em = discord.Embed(title = "M3's Help", description ="", color = 0x00a8ff)
        em.add_field(name="`$clear`", value="Clears channel message history (admin only)")
        em.add_field(name="`$rpt`", value="Make the bot echo you (admin only) ")
        em.add_field(name="`$dice`", value="Rolls a dice (6 faces)")
        em.add_field(name="`$add`", value="adds two numbers together!")
        em.add_field(name="`$choose`", value="chooses between multiple choices!")
        em.add_field(name="`$helpmusic`", value="help commands for M31ON's music commands")
        em.set_footer(text="M31ON")
        await ctx.send(embed=em) 

@bot.command()
async def helpmusic(ctx):
        em = discord.Embed(title = "Music Help", description ="", color = 0x00a8ff)
        em.add_field(name="`$p`", value="play's a song from youtube! (uses YoutubeDl")
        em.add_field(name="`$summon", value="Make the bot join the call ")
        em.add_field(name="`$q`", value="Shows the queue")
        em.add_field(name="`$skip`", value="Skips the current song")
        em.add_field(name="`$pause/$resume`", value="Pauses/resumes the current song")
#theres more but i cant be bothered to list them out, just check the cog LOL

@bot.command(name='dice', aliases=['roll','rolladice'])
async def dice(ctx):
    answer = random.randint(1, 6)
    await ctx.send(f'The dice rolled a {answer}')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command(name='choose')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def ip(ctx):
    await ctx.send('The IP is: play.ultimamc.net')

@bot.command()
async def clear(ctx):
    if ctx.author.guild_permissions.administrator:
            await ctx.channel.delete()
            new_channel = await ctx.channel.clone(reason="Channel was cleared")
            await new_channel.edit(position=ctx.channel.position)
            await new_channel.send("`Channel was cleared`")
    else:
            await ctx.send("insufficiant perms")

@bot.command()
async def rpt(ctx,*,message="Error: No/Invalid message entered"):
    if ctx.author.guild_permissions.administrator:
        embed = discord.Embed(title="", description=message, color=discord.Color.green())
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)
    else:
        await ctx.send("insufficiant perms")

## LOOP BTC amt. 
@bot.command()
async def startBTC(ctx): #Note: Zero is used to represent false, and One is used to represent true.
    myLoop.start()
    await ctx.channel.purge(limit=1)
    await ctx.send('starting...')
    
@bot.command()
async def stopBTC(ctx): #Note: Zero is used to represent false, and One is used to represent true.
    myLoop.stop()
    await ctx.channel.purge(limit=1)
    await ctx.send('stopping...')

@tasks.loop(seconds = 6) # repeat after every 10 seconds
async def myLoop():
    channel = bot.get_channel(974969930774626304) #could also make it based on ctx
    #obv replace above w ur channel's ID
    await channel.send('BTCprices are BLAH') 
#Bitcoin prices JUST an example. Can use for anything. 

load_dotenv()
discordtoken= os.getenv('token')
bot.run(discordtoken)