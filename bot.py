import discord
from json import loads
from pathlib import Path
import asyncio
import os
import random
from discord.ext import commands

bot = commands.Bot(itents=discord.Intents.all())

TOKEN = loads(Path("config.json").read_text())["token"]
ADMIN = loads(Path("config.json").read_text())["admin"]
CHID = loads(Path("config.json").read_text())["ChId"]


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")


@bot.slash_command(description="restart the bot")
async def restart(ctx):
    if ctx.author.id == ADMIN:
        embed = discord.Embed()
        embed.set_author(
            name="Restarting...",
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
async def summon(ctx):
    if ctx.author.voice is None:
        embed = discord.Embed(
            description="You are not in the voice channel!", color=discord.Color.red())
        await ctx.respond(embed=embed)
        return
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(ctx.author.voice.channel)
    await ctx.author.voice.channel.connect()  # connect to the voice channel
    await ctx.respond(f"Connected to {ctx.author.voice.channel}")
    await asyncio.sleep(1)


@bot.slash_command(description="Disconnect the bot")
async def stop(ctx):
    if ctx.voice_client is not None:
        embed = discord.Embed(description="Disconnected!",color=discord.Color.red())
        await ctx.voice_client.disconnect()
        await ctx.respond(embed=embed)
    else:
        await ctx.respond("I'm not connected to a voice channel!")

@bot.slash_command(description="Get user's avatar")
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f"{user.name}'s avatar", color=discord.Color.blurple())
    embed.set_image(url=user.avatar)
    await ctx.respond(embed=embed)

@bot.slash_command(description="ohno")
async def ohno(ctx):
    rand_num = random.randint(1, 294)
    url = f'https://www.raylu.net/f/ohno/ohno{rand_num:03d}.png'
    embed = discord.Embed()
    embed.set_image(url=url)
    await ctx.respond(embed=embed)

@bot.event
async def on_message(message):
    if message.content == "!test":
        print("It works!")
        await message.channel.send("test")
    await bot.process_commands(message)


lol = "🟦"
valorant = "🟥"
overwatch = "⬜"
pubg = "🟫"
tft = "🟪"
etc = "🟩"

# @bot.slash_command(description="Vote for the game")
# async def vote(ctx):
#     button1 = Button(label=lol, style=discord.ButtonStyle.gray)
#     button2 = Button(label=valorant, style=discord.ButtonStyle.gray)
#     button3 = Button(label=overwatch, style=discord.ButtonStyle.gray)
#     button4 = Button(label=pubg, style=discord.ButtonStyle.gray)
#     button5 = Button(label=tft, style=discord.ButtonStyle.gray)
#     button6 = Button(label=etc, style=discord.ButtonStyle.gray)
#     view = View()
#     view.add_item(button1)
#     view.add_item(button2)
#     view.add_item(button3)
#     view.add_item(button4)
#     view.add_item(button5)
#     view.add_item(button6)
#     embed=discord.Embed(title="**Vote for the games you play!**", color=discord.Color.blurple())
#     embed.add_field(name="※You can vote for more than one game",value="",inline=False)
#     embed.add_field(name="", value=f"```yml\n{lol} | LEAGUE OF LEGENDS```", inline=False)
#     embed.add_field(name="", value=f"```yml\n{valorant} | VALORANT```", inline=False)
#     embed.add_field(name="", value=f"```yml\n{overwatch} | OVERWATCH```", inline=False)
#     embed.add_field(name="", value=f"```yml\n{pubg} | PUBG: BATTLEGROUNDS```", inline=False)
#     embed.add_field(name="", value=f"```yml\n{tft} | TEAMFIGHT TACTICS```", inline=False)
#     embed.add_field(name="", value=f"```yml\n{etc} | ETC...```", inline=False)
#     await ctx.respond(embed=embed, view=view)

@bot.slash_command(description="Vote for the game")
async def vote(ctx):
    embed = discord.Embed(title="**Vote for the games you play!**", color=discord.Color.blurple())
    embed.add_field(name="Roles will be automatically assigned based on your game selection", value="", inline=False)
    embed.add_field(name="", value=f"{lol}  LEAGUE OF LEGENDS", inline=False)
    embed.add_field(name="", value=f"{valorant}  VALORANT", inline=False)
    embed.add_field(name="", value=f"{overwatch}  OVERWATCH", inline=False)
    embed.add_field(name="", value=f"{pubg}  PUBG: BATTLEGROUNDS", inline=False)
    embed.add_field(name="", value=f"{tft}  TEAMFIGHT TACTICS", inline=False)
    embed.add_field(name="", value=f"{etc}  ETC...", inline=False)
    embed.set_footer(text="※ You can vote for more than one game")

    message = await ctx.send(embed=embed)
    await message.add_reaction(lol)
    await message.add_reaction(valorant)
    await message.add_reaction(overwatch)
    await message.add_reaction(pubg)
    await message.add_reaction(tft)
    await message.add_reaction(etc)

# @bot.event
# async def on_raw_reaction_add(payload):
#     if payload.channel_id == 1104824866152136835:
#         guild = bot.get_guild(payload.guild_id)
#         member = guild.get_member(payload.user_id)

#         if payload.emoji.name == ":blue_square:":
#             role = discord.utils.get(guild.roles, name="League of Legends")
#             await member.add_roles(role)
#         elif payload.emoji.name == ":red_square:":
#             role = discord.utils.get(guild.roles, name="Valorant")
#             await member.add_roles(role)

#@bot.event
#async def on_reaction(ctx,reaction, message):
    # ChId = "1104824866152136835"
    # if reaction.message.channel.id != ChId:
    #     return
    # else:
    #     if reaction.emoji == lol:
    #         await message.author.add_roles(discord.utils.get(message.guild.roles, id="1108669437374107670"))
    #     elif reaction.emoji == valorant:
    #         await message.author.add_roles(discord.utils.get(message.guild.roles, id="1108669437374107670"))
    #     elif reaction.emoji == overwatch:
    #         await message.author.add_roles(discord.utils.get(message.guild.roles, id="1108669437374107670"))
    #     elif reaction.emoji == pubg:
    #         await message.author.add_roles(discord.utils.get(message.guild.roles, id="1108669437374107670"))
    #     elif reaction.emoji == tft:
    #         await message.author.add_roles(discord.utils.get(message.guild.roles, id="1108669437374107670"))
    #     elif reaction.emoji == etc:
    #         await message.author.add_roles(discord.utils.get(message.guild.roles, id="1108669437374107670"))
    #     else:
    #         return

@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    with open('config.json', 'r') as f:
        data = loads(f.read())
        roleIds = data.get["roleIds"]
    
    ChId = CHID
    if payload.channel_id != ChId:
        return  
    guild = bot.get_guild(payload.guild_id)
    member = payload.member
    if str(payload.emoji) == lol:
        role = discord.utils.get(guild.roles, id=roleIds[0]['lol'])
        if role:
            await member.add_roles(role)
    elif str(payload.emoji) == valorant:
        role = discord.utils.get(guild.roles, id=roleIds[1]['valorant'])
        if role:
            await member.add_roles(role)
    elif str(payload.emoji) == overwatch:
        role = discord.utils.get(guild.roles, id=roleIds[2]['overwatch'])
        if role:
            await member.add_roles(role)
    elif str(payload.emoji) == pubg:
        role = discord.utils.get(guild.roles, id=roleIds[3]['pubg'])
        if role:
            await member.add_roles(role)
    elif str(payload.emoji) == tft:
        role = discord.utils.get(guild.roles, id=roleIds[4]['tft'])
        if role:
            await member.add_roles(role)
    elif str(payload.emoji) == etc:
        role = discord.utils.get(guild.roles, id=roleIds[5]['etc'])
        if role:
            await member.add_roles(role)
    else:
        return

# Debugging
# @bot.event
# async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
#     ChId = 1104824866152136835
#     if payload.channel_id != ChId:
#         return
#     guild = bot.get_guild(payload.guild_id)
#     member = payload.member
#     if str(payload.emoji) == lol:
#         role = discord.utils.get(guild.roles, id=1157010136158716015)
#         if role:
#             await member.add_roles(role)
#             print(f"Assigned role '{role.name}' to {member.display_name}")
#         else:
#             print(f"Role with ID '1157010136158716015' not found.")
#     elif str(payload.emoji) == valorant:
#         role = discord.utils.get(guild.roles, id=1157010136158716015)
#         if role:
#             await member.add_roles(role)
#             print(f"Assigned role '{role.name}' to {member.display_name}")
#         else:
#             print(f"Role with ID '1157010136158716015' not found.")
#     elif str(payload.emoji) == overwatch:
#         role = discord.utils.get(guild.roles, id=1157010136158716015)
#         if role:
#             await member.add_roles(role)
#             print(f"Assigned role '{role.name}' to {member.display_name}")
#         else:
#             print(f"Role with ID '1157010136158716015' not found.")
#     elif str(payload.emoji) == pubg:
#         role = discord.utils.get(guild.roles, id=1157010136158716015)
#         if role:
#             await member.add_roles(role)
#             print(f"Assigned role '{role.name}' to {member.display_name}")
#         else:
#             print(f"Role with ID '1157010136158716015' not found.")
#     elif str(payload.emoji) == tft:
#         role = discord.utils.get(guild.roles, id=1157010136158716015)
#         if role:
#             await member.add_roles(role)
#             print(f"Assigned role '{role.name}' to {member.display_name}")
#         else:
#             print(f"Role with ID '1157010136158716015' not found.")
#     elif str(payload.emoji) == etc:
#         role = discord.utils.get(guild.roles, id=1157010136158716015)
#         if role:
#             await member.add_roles(role)
#             print(f"Assigned role '{role.name}' to {member.display_name}")
#         else:
#             print(f"Role with ID '1157010136158716015' not found.")
#     else:
#         return

bot.run(TOKEN)
