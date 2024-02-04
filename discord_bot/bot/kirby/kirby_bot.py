import os, _asyncio
import discord
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from itertools import cycle
import random
import json
import youtube_dl

client = commands.Bot(command_prefix='!', help_command=None)
status = cycle(["Made with Python", "Made by ...", "!help"])
players = {}

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_ready():
    change_status.start()
    print("I am ready")

@client.event
async def on_member_join(member):
    print(f"{member.mention} has joined the server")
    with open('users_kirby.json', 'r') as f:
        users = json.load(f)
    
    await update_data(users, member)

    with open('users_kirby.json', 'w') as f:
        json.dump(users, f)

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}ms')

#manage message
@client.event
async def on_message(message):
    with open('users_kirby.json', 'r') as f:
        users = json.load(f)
    
    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)
    
    with open('users_kirby.json', 'w') as f:
        json.dump(users, f)
    await client.process_commands(message)

@client.listen('on_message')
async def message(message):
    list_hello = ['hello', 'hi', 'slt', 'salut', 'yo', 'bjr', 'bonjour']
    if message.content.lower() in list_hello:
        len_list_hello = len(list_hello)
        number = random.randint(0, len_list_hello)
        await message.channel.send(f"{list_hello[number]} {message.author.mention}")

    list_bad_words = ["""liste gros mots"""]
    if message.content.lower() in list_bad_words:
        len_list_bad_words = len(list_bad_words)
        number = random.randint(0, len_list_bad_words)
        await message.channel.purge(limit=1)
        await message.channel.send(f"Message censuré de {message.author.mention}, évitez les gros mots s'il vous plaît")

#profile system
@client.command()
async def profil(message):
    with open('users_kirby.json', 'r') as f:
        users = json.load(f)
    await message.channel.send(f"Profil de {message.author.mention} :\n-niveau : {users[str(message.author.id)]['level']}\n-experience total : {users[str(message.author.id)]['experience']}")

#level system
async def update_data(users, user):
    if not str(user.id) in users:
        users[str(user.id)] = {}
        users[str(user.id)]['experience'] = 0
        users[str(user.id)]['level'] = 1
        users[str(user.id)]['program'] = []

async def add_experience(users, user, exp):
    users[str(user.id)]['experience'] += exp

async def level_up(users, user, channel):
    experience = users[str(user.id)]['experience']
    lvl_start = users[str(user.id)]['level']
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await channel.send("{} a monté de niveau jusqu'au niveau {}".format(user.mention, lvl_end))
        users[str(user.id)]['level'] = lvl_end

#music system
@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        await ctx.send("Je suis maintenant connecté dans votre salon vocal")
    else:
        await ctx.send("Désolé vous devez être dans un salon vocal pour éxecuter cette commande")

@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("J'ai quitté le salon vocal")
    else:
        await ctx.send("Désolé mais je ne suis pas dans un salon vocal")

@client.command(pass_context=True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Désolé mais je ne suis pas entrain de jouer pour le moment")

@client.command(pass_context=True)
async def reprend(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Désolé mais en ce moment aucun son n'est en pause")

@client.command(pass_context=True, aliases=['tg'])
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("J'ai arrêté de jouer")








youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

@client.command(name='play_song', help='To play song')
async def play(ctx,url):
    try :
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=client.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except:
        await ctx.send("The bot is not connected to a voice channel.")








#management
@client.command(aliases=["c"])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, *, amount : int):
    await ctx.channel.purge(limit=amount+1)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

client.run('ODI4NjYzODM0NzA5MTk2ODAw.YGs3Vg.RS3ANGl3xipjvhNFzoDycraOpHw')