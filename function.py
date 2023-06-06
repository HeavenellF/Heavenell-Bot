import discord
from discord import app_commands
import requests

async def MCserver_online(interaction: discord.Interaction):
    # return total Player online right now
    json_url = 'url_here'

    try:
        response = requests.get(json_url)
        response.raise_for_status()

        json_data = response.json()

        if 'currentcount' in json_data:
            player_count = json_data['currentcount']
            await interaction.response.send_message(f'There are/is ``{player_count}`` Player(s) online right now')
        else:
            await interaction.response.send_message("Player count not found in the JSON.")
            
    except requests.RequestException as e:
        await interaction.response.send_message("Failed to fetch Dynmap JSON data:", str(e))