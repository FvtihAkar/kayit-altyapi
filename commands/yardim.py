import discord
import importlib
import os,json

name = "yardim"
ayars = json.loads(open(os.path.curdir.replace("/commands","")+"/settings.json","r").read())
usage = ayars["prefix"]+"yardim"
async def run(message: discord.Message):
    commands = []
    for file in os.listdir(os.curdir+"/commands"):
        if file.endswith(".py"):
                file = file.replace(".py","")
                command = importlib.import_module(f"commands.{file}")
                command = {"ad": file,"komut": command.usage}
                commands.append(command)
    description = "AD | KULLANIM\n\n"
    for com in commands:
        description += f"{com['ad']} | {com['komut']}\n"
    emb = discord.Embed(title="KOMUTLAR",description=description,color=discord.Color.dark_red())
    await message.channel.send("",embed=emb)
    return