import discord
from discord.ext import commands
import aspose.words as aw
from os import system


token = "your_bot_token"
formats = ["docx", "odt"]
path = "the_path_where_the_files_will_be_process"


intents = discord.Intents.default()
intents.message_content = True
intents.typing = True
bot = commands.Bot(
    command_prefix="$",
    description="",
    intents=intents,
)

@bot.event
async def on_message(message):
    if message.content.startswith("$convert"):
        for i in message.attachments:
            for j in formats:
                if i.filename.endswith("."+j):
                    await i.save(fp=path+i.filename)
                    doc = aw.Document(path+i.filename)
                    new_name = "".join(i.filename.split(".")[:-1])+".pdf"
                    doc.save(path+new_name)
                    await message.channel.send(file=discord.File(path+new_name))
                    system("DEL "+path+i.filename)
                    system("DEL "+path+new_name)
                    break


bot.run(
    token,
    reconnect=True
)