import discord
from discord.ext import commands, tasks
from itertools import cycle

#Bot installation
client = commands.Bot(command_prefix='py!', help_command=None)
status = cycle(["Made with Python", "py!help"])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_ready():
    change_status.start()
    print("I am ready")

#
@client.command()
async def help(ctx):
    await ctx.send(f"-----HELP-----\nPython est un bot permettant d'apprendre facilement le python. Pour commencer vous pouvez faire la commande : py!index pour avoir toute la liste des cours disponnibles.")

#tout se qui concerne les cours en pythons
cours_all = ["-----les variables-----\nles variables sont des sortes d'objet que l'on assigne à des chiffres, textes,etc...Il y a plusieurs sortes de variables tel que les 'integer', les 'string', les 'list', etc...Les variables se définisse avec un nom puis ce dont la variables est assignée, par exemple :\n `a = 1` ou `a = 'bonjour'`.",
        "-----afficher du texte-----\nPour afficher du texte en python en mode console il ne suffit juste d'utiliser la fonction `print()` tel que `print('Hello world')` qui affichera : `Hello world`.",
        "-----demander à entrer du texte-----\nPour demander d'entrer du texte il suffit juste d'utiliser la fonction input tel que : `input('Entrez quelque chose : ')`, il est possible aussi d'assigner directement ce qui a été entré dans une variable tel que : `a = input('Entrez quelque chose : ')`.",
        "-----si, sinon, sinon si, finalement-----\nIl est possible d'utiliser if (qui veut dire 'si' en anglais) tel que :```a = 1\nif a == 1: \n print('a est égal à 1')```\nqui va regarder si la variable a est égal à 1 alors il affiche 'a est égal à 1'. Il est possible d'utiliser else (qui veut dire 'sinon en anglais') tel que :```\na = 1\nif a == 1:\n    print('a est égal à 1')\nelse:\n print('a n est pas égal à 1')```\nqui va regarder si la variable a est égal à 1 alors il affiche 'a est égal à 1' sinon il affiche 'a n est pas égal à 1'.Il est possible d'utiliser elif (qui veut dire 'sinon si' en anglais) tel que :```\na = 1\nif a == 1:\n    print('a est égal à 1')\nelif a == 4:\n    print('a est égal à 4')\nelse:\n    print('a n est pas égal à 1 ou à 4')```\nqui va regarder si la variable a est égal à 1 alors il affiche 'a est égal à 1' sinon si la variable a est égal à 4 alors il affiche 'a est égal à 4' sinon il affiche 'a n est pas égal à 1 ou à 4'.Il est possible d'utiliser finally (qui veut dire 'finalement' en anglais) tel que :\n```a = 1\nif a == 1:\n    print('a est égal à 1')\nelif a == 4:\n    print('a est égal à 4')\nelse:\n    print('a n est pas égal à 1 ou à 4')\nfinally:\n    a == 2```\nqui va regarder si la variable a est égal à 1 alors il affiche a' est égal à 1' sinon si la variable a est égal à 4 alors il affiche 'a est égal à 4' sinon il affiche 'a n'est pas égal à 1 ou à 4' et puis finalement.",
        "-----faire des boucles-----\nPour faire des boucles il y a plusieurs moyen possible, premièrement avec for tel que :\n```for i in range(3):\n    print('bonjour')```\nqui va dans ce cas là afficher bonjour 3 fois, deuxièmement avec while tel que :\na = 3\n```while a != 0:\n    print('bonjour')\n    a -= 1```\nqui va dans ce cas là afficher bonjour tant que a est différent de 0.",
        "",
        "",
        ""]

@client.command(aliases=['install'])
async def installation(ctx):
    await ctx.send("python : https://www.python.org/downloads (conseil : prendre la dernière version)\nvisual studio code : https://code.visualstudio.com/download")

@client.command()
async def index(ctx):
    await ctx.send("Voici l'index de toute les lessons dans l'ordre d'apprentissage (tapez la commande : py!cours <numéro du cours>) : \n1- variables\n2- afficher\n3- demander à entrer du texte\n4- si, sinon, sinon si, finalement\n5- faire des boucles\n***coming soon***")

@client.command()
async def cours(ctx, *, amount : int):
    await ctx.send(cours_all[amount-1])

#running bot
client.run('ODI4MjQ0MTAxOTAzMTU1MjQw.YGmwbQ.dEvf-LmMF5Jmb1fceQY02xJ-LJw')