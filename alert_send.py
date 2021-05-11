import logging
import os

import telebot
from discord_webhook import DiscordWebhook

from wazirx_get import datas, logging

# initializing telegram bot
telegram_bot = telebot.TeleBot(
    os.environ.get('TELEGRAM_SECRET'),
    parse_mode='MARKDOWN'
)


def create_msg(datas):
    '''
        This function takes data(form api) as input and returns a message in a required format in string.
    '''
    def _message(data):
        message = "\n\n*Name: {}*\n*LTP:* {}\n*Lowest:* {}\n*Highest:* {}\n*Open:* {}\n"
        return (message.format(data['name'], data['last'], data['low'], data['high'], data['open']))

    final_message = ''

    for data in datas:
        final_message = final_message + _message(data)

    return final_message


def telegram_send(chat_id, message):
    '''
        This function will send notification to telegram
    '''
    try:
        telegram_bot.send_message(chat_id, message)
        logging.info('telegram message sent')
        return True

    except:
        logging.warning('telegram message not sent')
        return False


def discord_send(url, message):
    '''
        This function will send notification to discord
    '''
    try:
        webhook = DiscordWebhook(url=url, content=message)
        webhook.execute()
        logging.info('discord message sent')
        return True

    except:
        logging.warning('telegram message not sent')
        return False

    
if __name__ == '__main__':
    # telegram_send(os.environ.get('TELEGRAM_CHAT_ID'), create_msg(datas))
    discord_send(os.environ.get('DISCORD_WEBHOOK_URL'), create_msg(datas))
