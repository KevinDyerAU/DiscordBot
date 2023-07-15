from discord.ext import commands
import discord

import openai

BOT_TOKEN = "MTEyNjczMTA3Mjc0MzQyMDA0NA.GAnYS9.2b9zPBOlzN2XZhrR2460EntzliNuUyHpkYTUP8"
CHANNEL_ID = 1126741465893175336

OPENAPI_API_KEY = "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"
openai.api_key=OPENAPI_API_KEY


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! Study bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! How can I help you tdoay?")

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

bot.run(os.environ["DISCORD_TOKEN"])
