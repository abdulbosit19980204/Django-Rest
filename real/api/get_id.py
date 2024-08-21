from telethon import TelegramClient

# Replace with your own API ID, hash, and bot token
api_id = 27668593
api_hash = 'db44de3510fb53c30375bfce090989d9'
bot_token = '6189703946:AAGb1TA2yDg-sdu0c_AIDn39_07AuzvlZgE'

client = TelegramClient('get_group_id', api_id, api_hash).start(bot_token=bot_token)


async def main():
    async for dialog in client.iter_dialogs():
        print(f'{dialog.name}: {dialog.id}')


with client:
    client.loop.run_until_complete(main())
