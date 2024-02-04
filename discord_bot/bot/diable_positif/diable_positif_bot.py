import discord
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='dp!', help_command=None)
status = cycle(["Made with Python", "Made by ...", "dp!help"])

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

@client.listen('on_message')
async def message(message):
    dico_video = {"49.3" : "https://youtu.be/CIq0cZTd5dw",
                  "la retraite" : "https://youtu.be/iOtIlA_X6xk",
                  "la précarité étudiante" : "https://youtu.be/rDhtMq3bAY8",
                  "la banlieue" : "https://youtu.be/Z6wqwQ3SJTk",
                  "la chasse de loisir" : "https://youtu.be/H0qjrn13_7k"}
    if "49.3" in message.content.lower() and message.author.name != "Diable Positif":
        element = "49.3"
        await message.channel.send(f"Haha, tu parle de {element}, j'ai une vidéo la dessus, va la voir sinon je te tue :smiling_imp: : {dico_video.get(element)}")
    if "la retraite" in message.content.lower() and message.author.name != "Diable Positif":
        element = "la retraite"
        await message.channel.send(f"Haha, tu parle de {element}, j'ai une vidéo la dessus, va la voir sinon je te tue :smiling_imp: : {dico_video.get(element)}")
    if "la précarité étudiante" in message.content.lower() and message.author.name != "Diable Positif":
        element = "la précarité étudiante"
        await message.channel.send(f"Haha, tu parle de {element}, j'ai une vidéo la dessus, va la voir sinon je te tue :smiling_imp: : {dico_video.get(element)}")
    if "la banlieue" in message.content.lower() and message.author.name != "Diable Positif":
        element = "la banlieue"
        await message.channel.send(f"Haha, tu parle de {element}, j'ai une vidéo la dessus, va la voir sinon je te tue :smiling_imp: : {dico_video.get(element)}")
    if "chasse de loisir" in message.content.lower() and message.author.name != "Diable Positif":
        element = "la chasse de loisir"
        await message.channel.send(f"Haha, tu parle de {element}, j'ai une vidéo la dessus, va la voir sinon je te tue :smiling_imp: : {dico_video.get(element)}")


client.run('ODMwNzMzMTQxNjU2MjA3MzYw.YHK-hw.4ObXMm5mGiLUaCOCNEuUEkWIzwM')