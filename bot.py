import discord
from json import loads
from pathlib import Path
import asyncio
import os

bot = discord.Bot(itents=discord.Intents.all())
TOKEN = loads(Path("config.json").read_text())["token"]
ADMIN = loads(Path("config.json").read_text())["admin"]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

@bot.slash_command(description="restart the bot")
async def restart(ctx):
    if ctx.author.id == ADMIN:
        embed = discord.Embed()
        embed.set_author(
            name = "Restarting...",
        )
        embed.color = 0x42B582
        await ctx.respond(embed=embed, delete_after=1)
        os.system("python bot.py")
        await bot.close()
    else:
        embed = discord.Embed()
        embed.set_author(
            name="You don't have permission!"
        )
        embed.color = discord.Color.red()
        await ctx.respond(embed=embed)

@bot.slash_command(description="Summon the bot")
async def play(ctx):
    if ctx.author.voice is None:
        embed = discord.Embed(description="You are not in the voice channel!", color=discord.Color.red())
        await ctx.respond(embed=embed)
        return
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(ctx.author.voice.channel)
    await ctx.author.voice.channel.connect()
    await ctx.respond(f"Connected to {ctx.author.voice.channel}")
    await asyncio.sleep(1)

bot.run(TOKEN)