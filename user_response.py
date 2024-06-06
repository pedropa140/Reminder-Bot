import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import random
import datetime

from user import User, UserDatabase

from google.auth import load_credentials_from_file
from google.oauth2 import credentials
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

async def adduser(interaction : discord.Interaction, time_reminder : str, userDatabase : UserDatabase):
    if userDatabase.user_exists(str(interaction.user.id)):
        result_title = f'**User Already Created**'
        result_description = f'User already created for **{interaction.user.mention}**'
        embed = discord.Embed(title=result_title, description=result_description, color=0xFF5733)
        file = discord.File('images/icon.png', filename='icon.png')
        embed.set_thumbnail(url='attachment://icon.png')
        embed.set_author(name="Reminder-Bot says:")
        embed.set_footer(text="/adduser")
        await interaction.response.send_message(file=file, embed=embed, ephemeral=False)
    else:
        
        creds = None
    
        username_string = f'token/token_{str(interaction.user.id)}.json'
        if os.path.exists(username_string):
            creds = Credentials.from_authorized_user_file(username_string, SCOPES)

        await interaction.response.defer()
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                except Exception as e:
                    if os.path.exists(username_string):
                        os.remove(username_string)
            else:
                
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)

                auth_url, _ = flow.authorization_url()
                await interaction.followup.send(f"OPEN FOR GOOGLE CALENDAR PERMISSION: {auth_url}")
                while True:
                    try:
                        
                        flow.fetch_token(code = None)
                        
                        creds = flow.credentials
                        break
                    except Exception as e:
                        continue

                with open(username_string, "w") as token:
                    token.write(creds.to_json())
        
        def validate_time(time_str):
            hours, minutes = time_str.split(':')
            if not hours.isdigit() or not minutes.isdigit():
                return False
            hours = int(hours)
            minutes = int(minutes)
            if hours < 0 or hours > 24 or minutes < 0 or minutes > 60:
                return False
            return True
        check = validate_time(time_reminder)
        if check:
            userDatabase.add_user(User(str(interaction.user), str(interaction.user.id), time_reminder))
            result_title = f'**User Created**'
            result_description = f'User created for **{interaction.user.mention}**'
            embed = discord.Embed(title=result_title, description=result_description, color=0xFF5733)
            file = discord.File('images/icon.png', filename='icon.png')
            embed.set_thumbnail(url='attachment://icon.png')
            embed.set_author(name="Reminder-Bot says:")
            embed.set_footer(text="/adduser")
            await interaction.response.send_message(file=file, embed=embed, ephemeral=False)
        else:
            result_title = f'Invalid Output'
            result_description = f'Did not create user for **{interaction.user.mention}**'
            embed = discord.Embed(title=result_title, description=result_description, color=0xFF5733)
            file = discord.File('images/icon.png', filename='icon.png')
            embed.set_thumbnail(url='attachment://icon.png')
            embed.set_author(name="Reminder-Bot says:")
            embed.set_footer(text="/adduser")
            await interaction.response.send_message(file=file, embed=embed, ephemeral=False)

async def userinfo(interaction : discord.Interaction, userDatabase : UserDatabase):
    if not userDatabase.user_exists(str(interaction.user.id)):
        result_title = f'**User Not Found**'
        result_description = f'User not found for **{interaction.user.mention}**'
        embed = discord.Embed(title=result_title, description=result_description, color=0xFF5733)
        file = discord.File('images/icon.png', filename='icon.png')
        embed.set_thumbnail(url='attachment://icon.png')
        embed.set_author(name="Reminder-Bot says:")
        embed.set_footer(text="/userinfo")
        await interaction.response.send_message(file=file, embed=embed, ephemeral=False)
    else:
        discord_id = str(interaction.user.id)
        info = userDatabase.get_user_by_id(discord_id)
        result_title = f'Information about {info[0]}'
        description_string = f'**Name:**\t\t{info[0]}\n**Discord ID:**\t{info[1]}\n**Preferred Time:**\t{info[2]}'
        embed = discord.Embed(title=result_title, description=description_string, color=0xFF5733)
        file = discord.File('images/icon.png', filename='icon.png')
        embed.set_thumbnail(url='attachment://icon.png')
        embed.set_author(name="Reminder-Bot says:")
        embed.set_footer(text="/userinfo")
        await interaction.response.send_message(file=file, embed=embed, ephemeral=False)


async def changereminder(interaction : discord.Interaction, time_reminder : str, userDatabase : UserDatabase):
    if not userDatabase.user_exists(str(interaction.user.id)):
        result_title = f'User Not Found'
        result_description = f'User not found for **{interaction.user.mention}**'
        embed = discord.Embed(title=result_title, description=result_description, color=0xFF5733)
        file = discord.File('images/icon.png', filename='icon.png')
        embed.set_thumbnail(url='attachment://icon.png')
        embed.set_author(name="Reminder-Bot says:")
        embed.set_footer(text="/changereminder")
        await interaction.response.send_message(file=file, embed=embed, ephemeral=False)
    else:
        def validate_time(time_str):
            hours, minutes = time_str.split(':')
            if not hours.isdigit() or not minutes.isdigit():
                return False
            hours = int(hours)
            minutes = int(minutes)
            if hours < 0 or hours > 24 or minutes < 0 or minutes > 60:
                return False
            return True
        check = validate_time(time_reminder)
        if check:
            userDatabase.update_time_preference(str(interaction.user.id), time_reminder)
            result_title = f'Preference Time Changed'
            result_description = f'**{interaction.user.mention}** will be notified at {time_reminder}'
            embed = discord.Embed(title=result_title, description=result_description, color=0xFF5733)
            file = discord.File('images/icon.png', filename='icon.png')
            embed.set_thumbnail(url='attachment://icon.png')
            embed.set_author(name="Reminder-Bot says:")
            embed.set_footer(text="/changereminder")
            await interaction.response.send_message(file=file, embed=embed, ephemeral=False)
        else:
            result_title = f'Invalid Output'
            result_description = f'Did not change preference time for **{interaction.user.mention}**'
            embed = discord.Embed(title=result_title, description=result_description, color=0xFF5733)
            file = discord.File('images/icon.png', filename='icon.png')
            embed.set_thumbnail(url='attachment://icon.png')
            embed.set_author(name="Reminder-Bot says:")
            embed.set_footer(text="/changereminder")
            await interaction.response.send_message(file=file, embed=embed, ephemeral=False)

async def deleteuser(interaction : discord.Interaction , userDatabase : UserDatabase):
    username_string = f'token/token_{str(interaction.user.id)}.json'
    if not userDatabase.user_exists(str(interaction.user.id)) and not os.path.exists(username_string):
        result_title = f'User Not Found'
        result_description = f'User not found for **{interaction.user.mention}**'
        embed = discord.Embed(title=result_title, description=result_description, color=0xFF5733)
        file = discord.File('images/icon.png', filename='icon.png')
        embed.set_thumbnail(url='attachment://icon.png')
        embed.set_author(name="Reminder-Bot says:")
        embed.set_footer(text="/deleteuser")
        await interaction.response.send_message(file=file, embed=embed, ephemeral=False)
    else:
        os.remove(username_string)
        print(f"The file {username_string} has been deleted successfully.")
        userDatabase.delete_user(str(interaction.user.id))
        result_title = f'**User Deleted**'
        result_description = f'User deleted for **{interaction.user.mention}**'
        embed = discord.Embed(title=result_title, description=result_description, color=0xFF5733)
        file = discord.File('images/icon.png', filename='icon.png')
        embed.set_thumbnail(url='attachment://icon.png')
        embed.set_author(name="Reminder-Bot says:")
        embed.set_footer(text="/deleteuser")
        await interaction.response.send_message(file=file, embed=embed, ephemeral=False)