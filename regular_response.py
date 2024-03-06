import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import random
import datetime

from user import User, UserDatabase

async def hello(message : discord.message.Message):
    options = ["Hi ", "Hey ", "Hello ", "Howdy ", "Hi there ", "Greetings ", "Aloha ", "Bonjour ", "Ciao ", "Hola ", "How's it going? ", "Howdy-do ", "Good day ", "Wassup ", "What's popping? ", "What's up? ", "Hiya ", "What's new? ", "How are you? "]
    current_time = datetime.datetime.now().time().hour
    if current_time > 12:
        options.append("Good Afternoon! ")
    else:
        options.append("Good Morning! ")
    chosen_string = options[random.randint(0, len(options) - 1)]
    string = chosen_string + message.author.mention
    embed = discord.Embed(title = chosen_string, description=string, color=0xFF5733)
    file = discord.File('images/icon.png', filename='icon.png')
    embed.set_thumbnail(url='attachment://icon.png')
    embed.set_author(name="Reminder-Bot says:")
    embed.set_footer(text="!hello")
    await message.channel.send(file=file, embed=embed)

async def time(message : discord.message.Message):
    date = datetime.datetime.now()
    year = str(date.year).zfill(2)
    day = str(date.day).zfill(2)
    month = str(date.month).zfill(2)
    hour = str(date.hour).zfill(2)
    minute = str(date.minute).zfill(2)
    second = str(date.second).zfill(2)

    result_string = f'**Today is:** {year}-{day}-{month}\n**The time is:** {hour}:{minute}:{second}'
    embed = discord.Embed(title=result_string, color=0xFF5733)
    file = discord.File('images/icon.png', filename='icon.png')
    embed.set_thumbnail(url='attachment://icon.png')
    embed.set_author(name="Reminder-Bot says:")
    embed.set_footer(text="!time")
    await message.channel.send(file=file, embed=embed)

async def pomodoro(message : discord.message.Message):
    return NotImplementedError()

async def help(message : discord.message.Message):
    # result_string = f'!Help'
    # help_description = f''''''
    # embed = discord.Embed(title=result_string, description=help_description, color=0xFF5733)
    # file = discord.File('images/icon.png', filename='icon.png')
    # embed.set_thumbnail(url='attachment://icon.png')
    # embed.set_author(name="Reminder-Bot says:")
    # embed.set_footer(text="!help")
    # await message.channel.send(file=file, embed=embed)
    return NotImplementedError()

async def invalidInput(message : discord.message.Message):
    return NotImplementedError()