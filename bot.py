import discord
import os
import importlib
import json
import sqlite3

ayars = json.loads(open("settings.json","r").read())


intents = discord.Intents.all()

client = discord.Client(intents=intents)
commands = []

@client.event
async def on_ready():
    print(f'{client.user.display_name} Adıyla giriş yapıldı.')
    for file in os.listdir(os.curdir+"/commands"):
        if os.path.exists("/commands/__pycache__"):
            os.rmdir("/commands/__pycache__")
        
        if file.endswith(".py"):
            file = file.replace(".py","")
            command = importlib.import_module(f"commands.{file}")
            commands.append(command)
            print(f"Komut yüklendi : {file}")

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    for com in commands:
        if message.content.startswith(ayars["prefix"]+com.name):
            await com.run(message)

@client.event
async def on_member_join(member: discord.Member):
    kanalize = member.guild.get_channel(int(ayars["hg-log"]))
    await kanalize.send(f"{member.display_name} Adında bir kullanıcı katıldı !\nHoşgeldin {member.mention}\n{member.guild.get_role(int(ayars['yetkili'])).mention}")
    await member.add_roles(member.guild.get_role(int(ayars["kayitsiz-rol"])))


async def on_member_leave(member: discord.Member):
    kanalize = member.guild.get_channel(int(ayars["hg-log"]))
    await kanalize.send(f"{member.display_name} Adında bir kullanıcı aramızdan ayrıldı !\Görüşürüz {member.mention}")


client.run(ayars["token"])