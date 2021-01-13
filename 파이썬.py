import discord
token = "Nzk2MTc1NTgxOTk3MTcwNzAw.X_UGSg.SWwz2IsQCQs1q0ra5nKyt9ujFOc"
client = discord.Client()

@client.event
async def on_ready():
    print("Starting...")

@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕! 반가워!")
    if message.content.startswith("!오버워치"):
        await message.channel.send("https://playoverwatch.com/ko-kr/")
    if message.content.startswith("!하이픽셀"):
        await message.channel.send("하이픽셀주소:Mc.hypixel.net")
    if message.content.startswith("!포나"):
        await message.channel.send("포나주소:https://www.epicgames.com/fortnite/ko/home?sessionInvalidated=true")
    if message.content.startswith("!포트나이트"):
        await message.channel.send("포나주소:https://www.epicgames.com/fortnite/ko/home?sessionInvalidated=true")
    if message.content.startswith("!포나"):
        await message.channel.send("포나주소:https://www.epicgames.com/fortnite/ko/home?sessionInvalidated=true")
    if message.content.startswith("!배틀그라운드"):
        await message.channel.send("https://pubg.game.daum.net/pubg/index.daum")
    if message.content.startswith("!카트라이더"):
        await message.channel.send("https://kart.nexon.com/events/2021/0107/Update.aspx")
    if message.content.startswith("!도움말"):
        

client.run("token")