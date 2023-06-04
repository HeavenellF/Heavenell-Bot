from typing import Optional

import discord
from discord import app_commands

import random
import os

import gptBot
import json


# Load the API_Key from the config.json File
with open('config.json') as config_file:
    config = json.load(config_file)
    API_Key = config['API_Key']

MY_GUILD = discord.Object(id=0)  # replace with your Guild ID


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)


    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

# Discord Bot setup
intents = discord.Intents.default()  # Create a new instance of the default Intents

intents.typing = False  # Disable receiving typing events from users
intents.presences = False  # Disable receiving presence update events
intents.message_content = True  # Enable receiving message content in message events
intents.guilds = False  # Disable receiving guild-related events
intents.members = False  # Disable receiving member-related events
intents.reactions = False  # Disable receiving reaction-related events

client = MyClient(intents=intents)  # Initialize the bot client with the configured intents

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.tree.command()
async def nothing(interaction: discord.Interaction):
    """DO NOT EXECUTE THIS COMMAND"""
    await interaction.response.send_message(content=":skull:")

# Command Group /heaven ------
heaven_group = app_commands.Group(name="heaven", description = "nothing to see here")

@heaven_group.command(name="hello", description="the Bot will greets you")
async def heaven_hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello, {interaction.user.mention}')


# running the Bot
client.tree.add_command(heaven_group)
client.run(API_Key)