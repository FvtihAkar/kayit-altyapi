import discord
from discord.utils import get
import json
import os
name = "e"

ayars = json.loads(open(os.path.curdir.replace("/commands","")+"/settings.json","r").read())
usage = ayars["prefix"]+"e -id- -isim- -yaş-"
async def run(message: discord.Message):
    auth = message.author.get_role(int(ayars["yetkili"]))
    if not auth:
        await message.reply("Yetkiniz yetersiz.")
        return
    global user
    user = None
    id = message.content.split(" ")[1]
    isim = message.content.split(" ")[2]
    yas = message.content.split(" ")[3]
    print(id,isim,yas)
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
    unrole = user.get_role(int(ayars["kayitsiz-rol"]))
    if not unrole:
        await message.reply("Kullanıcı zaten kayıtlı.")
        return
    display_name = f"{ayars['tag']} {isim} | {yas}"
    newu = await user.edit(nick=display_name)
    await newu.add_roles(message.guild.get_role(int(ayars["kayitli-rol"])))
    await newu.add_roles(message.guild.get_role(int(ayars["erkek-rol"])))
    await newu.remove_roles(message.guild.get_role(int(ayars["kayitsiz-rol"])))
    try:
        await user.dm_channel.send("Kaydınız başarılı !!")
    except:
        pass
    await message.reply(f"{newu.display_name} Adlı kullanıcının kaydı başarılı !")
    await message.guild.get_channel(int(ayars["kayit-log"])).send(f"{newu.display_name} adlı kullanıcı, {message.author.display_name} adlı admin tarafından kayıt edildi.")
    return