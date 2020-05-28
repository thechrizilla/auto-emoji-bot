import discord
from discord.ext import commands


client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if "sayori" in message.content.lower():
        await message.add_reaction("<:ddlc_sayori1:714704429483294773>")
    if "yuri" in message.content.lower():
        await message.add_reaction("<:ddlc_yuri1:714704430871740446>")
    if "monika" in message.content.lower():
        await message.add_reaction("<:ddlc_monika1:714704429567180850>")
    if "natsuki" in message.content.lower():
        await message.add_reaction("<:ddlc_natsuki1:713926007907942511>")
    if "shafin" in message.content.lower():
        await message.add_reaction("<:shafin:713536401681154099>")
    if "omri" in message.content.lower():
        await message.add_reaction("<:omri:715678198251388979>")
    if "bryson" in message.content.lower():
        await message.add_reaction("<:bryson:715680587465097729>")

        


    



client.run('NzE1NjM3MjM0ODk1OTQ1ODQ5.XtAHgA.a9evdjYaqXN2EdoXb34cBT38DYU')