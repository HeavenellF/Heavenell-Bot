import discord

import json
import openai

with open('config.json') as config_file:
    config = json.load(config_file)
    openAI_API_Key = config['API_Key']


async def chatbot(interaction: discord.Interaction, yourmessage):
    
    openai.api_key = openAI_API_Key
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=
    [
    {"role": "system", "content": "Heavenell is you Creator, you are Heavenbot."},
    {"role": "user", "content": "Answer as short and detail as possible :"},
    {"role": "user", "content": yourmessage}
    ]
    )

    output_content = completion.choices[0].message['content']
    message = f"`Your Message: {yourmessage}`\n{output_content}"
    await interaction.response.send_message(message)