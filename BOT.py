import discord
from discord.ext import commands
import random
import os

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
           print("DONE!")

@bot.command()
async def hi(ctx):
        await ctx.send("I have important, useless and not fun things to do. Don't disturb me.")

@bot.command()
async def randomnum(ctx):
    await ctx.send("The random number you asked for: {}".format(random.randint(-1000000000, 9999999999)))

@bot.command()
async def randomletter(ctx):
    bruh = ["A", "B", "C", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    await ctx.send("The random letter you asked for: {}".format(bruh[random.randint(0, 25)]))

@bot.command()
async def refresh(ctx):
    await ctx.send("Why are you tryna restart me? YOU GAY!?")

@bot.command()
async def joe(ctx):
    await ctx.send("JOE MAMA!")

@bot.command()
async def yuri(ctx):
    await ctx.send("YURI TARDED!")

@bot.command()
async def ligma(ctx):
    await ctx.send("LIGMA BALLS!")

@bot.command()
async def sugon(ctx):
    await ctx.send("SUGON THESE NUTS!")

@bot.command()
async def candese(ctx):
    await ctx.send("CANDESE NUTS FIT IN YO MOUTH!")

@bot.command()
async def suggest(ctx):
    await ctx.send("DM @qwert123qpei#6039 for command suggestions.\nYour suggestion should be like this:\n     command: <command>\n     use: <use>")

bot.run(os.environ(DISCORD_TOKEN))
