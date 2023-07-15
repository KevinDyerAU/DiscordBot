from discord.ext import commands
import discord

import openai

import os

BOT_TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = 1126741465893175336

openai.api_key=os.environ["OPENAI_TOKEN"]


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! Bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! UltronAI bot is ready!")

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    text_content = message.content

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":text_content}]
    )

    await message.channel.send(response.choices[0].message.content)


bot.run(BOT_TOKEN)
