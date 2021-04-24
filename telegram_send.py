import os
from datetime import datetime

import telebot
from telebot.types import Message

from wazirx_get import datas

bot = telebot.TeleBot(os.environ.get('TELEGRAM_SECRET'), parse_mode='MARKDOWN')

chat_id = os.environ.get('TELEGRAM_CHAT_ID')

def get_message_data(datas):
    def _message(data):
        message = "\n\n*Name:* {}\n*Last Traded Price:* {}\n*Lowest:* {}\n*Highest:* {}\n*Open:* {}\n"
        return (message.format(data['name'], data['last'], data['low'], data['high'], data['open']))

    final_message = ''

    for data in datas:
        final_message = final_message + _message(data)

    return final_message

try:
    bot.send_message(chat_id, get_message_data(datas))
    print("message sent success at {}".format(datetime.now()))

except:
    print("message failed at: {}".format(datetime.now()))
