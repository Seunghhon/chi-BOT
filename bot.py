import discord
from json import loads
from pathlib import Path

bot = discord.Bot(itents=discord.Intents.all())
TOKEN = loads(Path("config.json").read_text())["token"]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

bot.run(TOKEN)