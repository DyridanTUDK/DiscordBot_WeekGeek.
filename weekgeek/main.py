import time
import discord
import os
import pandas as pd

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$search"):
        command = 'scrapy crawl newcrawl -o booklog.json'
        os.system(command)
        await message.channel.send(f"I'm done looking for all the data use commdand '$hello' to generate titles")
    if message.content.startswith('$latest'):
            books = pd.read_json('booklog.json')
            for book in books['Title']:
                paragraph = books['paragraph']
                titleLink = books['links']
                for i in book:
                    currentIndex = book.index(i)
                    currentPara = paragraph[0][currentIndex]
                    currentLink = titleLink[0][currentIndex]
                    time.sleep(5)
                    print(currentPara)
                    embed = discord.Embed(title=i,description=currentPara,url=currentLink)
                    await message.channel.send(embed=embed)
            await message.channel.send(f'<@&1136593185917898762>')
    if message.content.startswith("$clear"):
        delete_json()
        await message.channel.send("Database cleared")


# Create a function that deletes data after sending the embedded message to discord
def delete_json():
    os.remove('booklog.json')
    print("json db has been cleared")
# Sleeper function



client.run('MTEzNTYzMzU3ODc2ODcyODEyNA.Gdqtyf.wv837dBJH3SvgDbSRo05boaC37W-EtedBQOSt8')