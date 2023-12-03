import discord
from discord.utils import get
import json
import os
name = "unregister"
ayars = json.loads(open(os.path.curdir.replace("/commands","")+"/settings.json","r").read())
usage = ayars["prefix"]+"unregister -id-"

async def run(message: discord.Message):
    auth = message.author.get_role(int(ayars["yetkili"]))
    if not auth:
        await message.reply("Yetkiniz yetersiz.")
        return
    global user
    user = None
    id = message.content.split(" ")[1]
    if id.startswith("<@"):
        async for u in message.guild.fetch_members():
            if u.mention == id:
                user = u
    elif id.isdigit():
        id = int(id)
        async for u in message.guild.fetch_members():
            if u.id == id:
                user = u
    else:
        await message.reply("Kayıt edilecek kullanıcının idsini yazın veya etiketleyin.")

    if not user:
        await message.channel.send("Kullanıcı bulunamadı.")
        return
    unrole = user.get_role(int(ayars["kayitli-rol"]))
    if not unrole:
        await message.reply("Kullanıcı zaten kayıtsız.")
        return
    await user.remove_roles(unrole)
    if user.get_role(message.guild.get_role(int(ayars["erkek-rol"])).id):
        role = message.guild.get_role(int(ayars["erkek-rol"]))
        await user.remove_roles(role)
    else:
        role = message.guild.get_role(int(ayars["kiz-rol"]))
        await user.remove_roles(role)
    await user.add_roles(message.guild.get_role(int(ayars["kayitsiz-rol"])))
    await message.reply("Kullanıcının kaydı başarıyla silindi.")
    return