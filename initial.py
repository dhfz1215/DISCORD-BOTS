#running discord bot
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message):
    if message.author == client.user: # 봇 자신이 보내는 메세지는 무시
        return

    if message.content.startswith('>hello'): # if the message '>hello'
        await message.channel.send('here') # return the message(in this case 'here)

client.run('ODY2NTI3OTM2OTE5NzY1MDMy.YPT3Bw.zf5T6COPmROnPr3vS1GDM4k3aq0') #token



