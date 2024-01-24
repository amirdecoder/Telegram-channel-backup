from telethon import TelegramClient, events, sync


api_id = ''
api_hash = ''
phone = ''
username = 'Client'
channel = 'https://t.me/Channel'


client = TelegramClient(username, api_id, api_hash)
client.start()


messages = client.get_messages(channel)


text = ""
for message in messages:
    if message.message:
        text += f"{message.message} \n"


print(text)