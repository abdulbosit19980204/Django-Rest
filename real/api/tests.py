from pyexpat.errors import messages
import aiocron
import random
from django.test import TestCase
from telethon.sync import TelegramClient, events

api_id = 27668593
api_hash = 'db44de3510fb53c30375bfce090989d9'
bot_token = '6189703946:AAGb1TA2yDg-sdu0c_AIDn39_07AuzvlZgE'
group_id = 1209619850
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
# List of users who can help
helpers = ['@abdulbosit', '@johndoe', '@janesmith']


# Cron job to send a message every day at 8 AM
@aiocron.crontab('1 9 * * *')
async def send_daily_message():
    # Randomly select a helper for the day
    today_helper = random.choice(helpers)
    message = f'Today {today_helper} can help you.'

    # Send the message to the group
    await bot.send_message(group_id, message)


# Start the bot
print("Bot is running...")
bot.run_until_disconnected()
