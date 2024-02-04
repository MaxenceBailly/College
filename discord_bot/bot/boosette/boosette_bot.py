import os, time, discord, random, json, gtts, os
from typing import Mapping
from discord.ext import commands, tasks
from itertools import cycle
from discord import FFmpegPCMAudio

client = commands.Bot(command_prefix='b!', help_command=None)
status = cycle(["Fait avec Python !", "Fait par ...", "b!aide"])

@client.event
async def on_member_join(member):
    print(f"{member.mention} has joined the server")
    with open('users_boosette.json', 'r') as f:
        users = json.load(f)
    
    await update_data(users, member)

    with open('users_boosette.json', 'w') as f:
        json.dump(users, f)

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_ready():
    change_status.start()
    print("I am ready")

@client.event
async def on_message(message):
    await client.process_commands(message)
    with open('users_boosette.json', 'r') as f:
        users = json.load(f)
    
    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)
    
    with open('users_boosette.json', 'w') as f:
        json.dump(users, f)
    await client.process_commands(message)

#level system
async def update_data(users, user):
    if not str(user.id) in users:
        users[str(user.id)] = {}
        users[str(user.id)]['experience'] = 0
        users[str(user.id)]['level'] = 1

async def add_experience(users, user, exp):
    users[str(user.id)]['experience'] += exp

async def level_up(users, user, channel):
    experience = users[str(user.id)]['experience']
    lvl_start = users[str(user.id)]['level']
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await channel.send("{} a monté de niveau jusqu'au niveau {}".format(user.mention, lvl_end))
        users[str(user.id)]['level'] = lvl_end


@client.listen('on_message')
async def message(message):
    current_path = os.path.dirname(os.path.realpath(__file__))
    directory = 'servers_logs'
    file_server = (f"{current_path}\{directory}\{message.guild.name}_{message.guild.id}.txt")
    with open(file_server, 'a') as file:
        file.write((f"[{message.channel.name}] {message.author.name} : {message.content}\n"))

    list_hello = ['hello', 'hi', 'slt', 'salut', 'yo', 'bjr', 'bonjour']
    if message.content.lower() in list_hello:
        len_list_hello = len(list_hello)
        number = random.randint(0, len_list_hello)
        await message.channel.send(f"{list_hello[number]} {message.author.mention}")
    
    list_dieu = ['dieu']
    if message.content.lower() in list_dieu:
        await message.channel.send(f"{message.author.mention} tu parle de dieu ? C'est ... notre dieu à tous, nous le vénérons depuis des siècles.")
    
    if message.channel.is_nsfw():
        pass
    else:
        list_bad_words = ["""liste des gros mots"""]
        if message.content.lower() in list_bad_words:
            len_list_bad_words = len(list_bad_words)
            number = random.randint(0, len_list_bad_words)
            await message.channel.purge(limit=1)
            await message.channel.send(f"Message censuré de {message.author.mention}, évitez les gros mots s'il vous plaît")

#nsfw commands
@client.command()
async def image(message):
    path = 'img'
    current_path = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(f"{current_path}\{path}")
    number_files = len(files)
    random_image = random.randint(0, (number_files - 1))
    image = files[random_image]
    image = image.replace("'", "")
    image = (f"{current_path}\{path}\{image}")

    await message.channel.send(file=discord.File(image))

#general commands
@client.command()
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=829813126929186827&permissions=8&scope=bot")

@client.command()
async def aide(ctx):
    await ctx.send("-----HELP-----\n- b!rejoins : pour faire rejoindre le bot dans ton salon vocal\n- b!part : pour faire partir le bot du salon vocal dans lequel il se trouve\n- b!dit : pour demander au bot de dire quelque chose dans le salon vocal\n- b!invite : pour inviter le bot dans ton propre serveur ! :wink:")

@client.command()
async def dit(ctx, *, text):
    if not (ctx.author.voice):
        await message.channel.send("Désolé mais je doit être dans un salon vocal pour parler, faites : b!rejoins")
    else:
        authorname = str(ctx.message.author)
        authorname = authorname.split("#")
        authorname = authorname.pop(0)

        lang = 'fr'
        filename = 'temp.mp3'
        audio = gtts.gTTS(text=(f"{authorname} dit {text}"), lang=lang, slow=False)
        audio.save(filename)
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio('temp.mp3')
        player = voice.play(source)

@client.command(pass_context=True)
async def rejoins(ctx):
    if (ctx.author.voice):
        authorname = str(ctx.message.author)
        authorname = authorname.split("#")
        authorname = authorname.pop(0)

        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        lang = 'fr'
        filename = 'temp.mp3'
        audio = gtts.gTTS(text=(f"{authorname} m'a invité"), lang=lang, slow=False)
        audio.save(filename)
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio('temp.mp3')
        player = voice.play(source)
        await ctx.send("je suis maintenant connecté dans votre salon vocal")
    else:
        await ctx.send("Désolé, vous devez être dans un salon vocal pour exécuté cette commande")

@client.command(pass_context=True)
async def part(ctx):
    if (ctx.voice_client):
        authorname = str(ctx.message.author)
        authorname = authorname.split("#")
        authorname = authorname.pop(0)
        
        lang = 'fr'
        filename = 'temp.mp3'
        audio = gtts.gTTS(text=(f"{authorname} m'a demandé de partir"), lang=lang, slow=False)
        audio.save(filename)
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio('temp.mp3')
        player = voice.play(source)
        time.sleep(4)
        await ctx.guild.voice_client.disconnect()
        await ctx.send("J'ai quitté le salon vocal")
    else:
        await ctx.send("Désolé mais je ne suis pas dans un salon vocal")

#management
@client.event
async def  on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Non non non petit(e) filou(te) :wink:, mais tu n'as pas la permission d'utiliser ceci.")

@client.command(aliases=["eff"])
@commands.has_permissions(manage_messages = True)
async def effacer(ctx, *, amount : int):
    await ctx.channel.purge(limit=amount+1)

@effacer.error
async def effacer_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Non non non petit(e) filou(te) :wink:, mais tu n'as pas la permission d'utiliser ceci.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Désolé Msieur ou Mdame (:wink:) mais il manque le nombre de message à supprimer.")

@client.command()
@commands.has_permissions(kick_members = True)
async def dégage(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def bannir(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

extensions = ['test']

@client.command()
async def charger(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def enlever(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run('ODI5ODEzMTI2OTI5MTg2ODI3.YG9lsg.TlnzyT2FCAxZcE7__sM30_rGqZ4')