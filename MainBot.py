from typing import Optional

import discord
from discord import app_commands

import random
import os

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


# running the Bot
client.run(API_Key)