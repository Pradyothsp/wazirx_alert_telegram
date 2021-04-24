import os

import telebot

from wazirx_get import data

bot = telebot.TeleBot(
    os.environ.get('TELEGRAM_SECRET'), parse_mode='MARKDOWN')

chat_id = os.environ.get('TELEGRAM_CHAT_ID')


def send_message(data):
    message = "*Name:* {}\n*Last Traded Price:* {}\n*Lowest:* {}\n*Highest:* {}\n*Open:* {}\n"
    return (message.format(data['name'], data['last'], data['low'], data['high'], data['open']))


bot.send_message(chat_id, send_message(data))
