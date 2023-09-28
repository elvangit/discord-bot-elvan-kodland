# daily automation experiment
import requests
import os
import random
import discord
from discord.ext import commands
from pass_generator import gen_pass
from modern_dict import m_dict
from datetime import datetime
# to enable intents in discord 2.0
intents = discord.Intents.all()
intents.message_content = True
# function initialization by prefix
bot = commands.Bot(command_prefix='$', intents=intents, help_command= None)
# on_ready event := Anything happens in discord server
@bot.event # decorator to modify python function itself if bot have logged in
async def on_ready(): # async to write a code not in chronologically
    print(f'We have logged in as {bot.user}')
# The async def keyword in Python is used to define a coroutine function. 
# A coroutine is a function that can be suspended and resumed at a later point in time. 
# This makes it ideal for asynchronous programming, where multiple tasks can be running concurrently.
@bot.event # decorator to modify python function for greeting hello
async def on_message(msg):
    username = msg.author.display_name 
    if msg.author == bot.user:
        return 
    elif msg.content == "Hello" or msg.content == "Hi" or msg.content == "Test":
        await msg.channel.send("Hi " + username + "!"+"  type $hello to start")
    await bot.process_commands(msg) #process_commands() at the end of your on_message. 
    # This is because overriding the default on_message forbids commands from running.
@bot.event # decorator to modify python function for welcoming message
async def on_member_join(member):
    guild = member.guild 
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f'Welcome to {guildname}!')
    await dmchannel.send(f'type $hello to start')          
# prompt command 
@bot.command() # calls the function
async def hello(ctx): # context
    await ctx.send(f'Hai! Saya adalah {bot.user} \U0001f642') #async bot to wait the previous instructions
    await ctx.send('=========================')
    await ctx.send(f'1. Saya bisa membantumu untuk menghasilkan kata sandi dengan ketik $pw')
    await ctx.send(f'2. Saya bisa membantumu mencari arti kata dengan ketik $dt <kata kapital> contoh $dt CRINGE')
    await ctx.send(f'3. Saya bisa membantumu membuat emoji dengan ketik $dt <kata> contoh $dt marah') 
    await ctx.send(f'4. Saya bisa membantumu memberikan gambar acak anjing dengan ketik $dog') 
    await ctx.send(f'5. Saya bisa membantumu memberikan gambar acak bebek dengan ketik $duck') 
    await ctx.send(f'6. Saya bisa membantumu memberikan meme hari ini dengan ketik $mem')
    await ctx.send(f'7. Saya bisa membantumu memberikan coinflip dengan ketik $coinflip')
    await ctx.send(f'8. Saya bisa membantumu memberikan random dice dengan ketik $dice')
    await ctx.send(f'9. Bantuan ketik $help') 
    await ctx.send('=========================')
    await ctx.send(f'daftar kata: CRINGE, BRB, LOL, GG, AFK, CREEPY(dev.)')
    await ctx.send(f'daftar kata penghasil emoji: marah, terbahak, keren, sedih, senyum, ok(dev.)')
    await ctx.send(f'Silakan pilih permintaanmu')               
# help
@bot.command(aliases = ["about"]) 
async def help(ctx):
    MyEmbed = discord.Embed(title = "Commands", description="These are available contacts to help you",color=discord.Colour.dark_blue())
    MyEmbed.set_thumbnail(url="https://logodownload.org/wp-content/uploads/2017/11/discord-logo-1-1.png")
    MyEmbed.add_field(name = "Contacts", value="vensiandoe@gmail.com",inline = False)
    await ctx.send(embed = MyEmbed)
# coinflip
@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('It is Head!')
    if num == 2:
        await ctx.send('It is Tail!')
# rolling dice
@bot.command()
async def dice(ctx):
    nums = random.randint(1,6)
    if nums == 1:
        await ctx.send('It is 1!')
    elif nums == 2:
        await ctx.send('It is 2!')
    elif nums == 3:
        await ctx.send('It is 3!')
    elif nums == 4:
        await ctx.send('It is 4!')
    elif nums == 5:
        await ctx.send('It is 5!')
    elif nums == 6:
        await ctx.send('It is 6!')
# password generator
@bot.command()
async def pw(ctx):
    await ctx.send(f'Kata sandi yang dihasilkan: {gen_pass(10)}')
# random local meme image
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('meme'))
    with open(f'meme/{img_name}', 'rb') as f: # local folder same workspace
        picture = discord.File(f)
    await ctx.send(file=picture)
# API to get random dog and duck image 
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    '''Setiap kali permintaan dog (anjing) dipanggil, program memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Setiap kali permintaan duck (bebek) dipanggil, program memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
# modern dictionary
@bot.command()
async def dt(ctx, arg):
    await ctx.send(f"{m_dict(arg)}")
# Cogs(related to class) is still running even there are changing(under development)
@bot.command()
async def load(ctx):
    await bot.load_extension("Cogs")
    await ctx.send('loaded')
@bot.command()
async def unload(ctx):
    await bot.unload_extension("Cogs")
    await ctx.send('unloaded')
@bot.command()
async def reload(ctx):
    await bot.reload_extension("Cogs")
    await ctx.send('reloaded')
# bot token
bot.run("token")
