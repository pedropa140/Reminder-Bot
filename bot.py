import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import random
import datetime

import regular_response
import user_response
from user import User, UserDatabase

load_dotenv()

def run_discord_bot():
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        # client.loop.create_task(ping_at_specific_time(client))
    
    @client.event
    async def on_message(message : discord.message.Message):
        if message.author == client.user:
            return
        username = str(message.author)
        mention = str(message.author.mention)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f'{username} ({mention}) said: "{user_message}" ({channel})')

        if client.user.mentioned_in(message):
            message_content = str(message.content)
            parts = message_content.split()
            if len(parts) >= 2:
                command = parts[1]
                message.content = command
            if message.content.startswith('!'):
                await process_command(message, client)
    
    # async def ping_at_specific_time(client):
    #     while True:
    #         current_time = datetime.datetime.now().strftime("%H:%M")
    #         if current_time == "08:00":
    #             print(f'{current_time} BOT PINGED')
    #             user = await client.fetch_user('525874420703559702')
    #             await user.send("It's time to do something!")

    #         await asyncio.sleep(5)

    async def process_command(message : discord.message.Message, client : discord.Client):
        userDatabase = UserDatabase('user_database.db')
        print("Database Connected")
        if message.content == '!hello':
            await regular_response.hello(message)
        elif message.content == '!time':
            await regular_response.time(message)
        elif message.content == '!adduser':
            await user_response.adduser(message, client, userDatabase)
        elif message.content == '!userinfo':
            await user_response.userinfo(message, client, userDatabase)
        elif message.content == '!changereminder':
            await user_response.changereminder(message, client, userDatabase)
        elif message.content == '!deleteuser':
            await user_response.deleteuser(message, client, userDatabase)
        elif message.content == '!addtask':
            return NotImplementedError()
        elif message.content == '!gettask':
            return NotImplementedError()
        elif message.content == 'removetask':
            return NotImplementedError()
        elif message.content == '!completetask':
            return NotImplementedError()
        elif message.content == '!pomodoro':
            return NotImplementedError()
        elif message.content == '!help':
            return NotImplementedError()
        else:
            return NotImplementedError()
        userDatabase.close()
        print("Database Closed")

    client.run(TOKEN)
    
