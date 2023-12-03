import discord
import time,json,os

name="nuke"
ayars = json.loads(open(os.path.curdir.replace("/commands","")+"/settings.json","r").read())
usage = ayars["prefix"]+"nuke"
async def run(message: discord.Message):
    await message.reply("------3 saniye içerisinde nuke atılıyor------")
    time.sleep(3)
    await message.channel.clone()
    await message.channel.delete()