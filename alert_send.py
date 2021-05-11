import os

import telebot
from discord_webhook import DiscordWebhook

from log import logger
from wazirx_get import datas

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
    ''' This function will send notification to telegram.

        Parameters
        ----------
        chat_id : int
            Telegram chat id
        message : str
            Message to be sent to telegram
    '''
    try:
        telegram_bot.send_message(chat_id, message)
        logger.info('telegram message sent')
        return True

    except:
        logger.error('telegram message not sent')
        return False


def discord_send(url, message):
    '''
        This function will send notification to discord
    '''
    try:
        webhook = DiscordWebhook(url=url, content=message)
        webhook.execute()
        logger.info('discord message sent')
        return True

    except:
        logger.error('telegram message not sent')
        return False

def main():
    message = create_msg(datas)
    telegram_send(os.environ.get('TELEGRAM_CHAT_ID'), message)
    discord_send(os.environ.get('DISCORD_WEBHOOK_URL'), message)

if __name__ == '__main__':
    main()
