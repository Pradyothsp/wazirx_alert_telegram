import os

# import requests
import telebot
from discord_webhook import DiscordEmbed, DiscordWebhook

from wazirx_get import datas

telegram_bot = telebot.TeleBot(
    os.environ.get('TELEGRAM_SECRET'),
    parse_mode='MARKDOWN'
)


def create_msg(datas):
    def _message(data):
        message = "\n\n*Name: {}*\n*LTP:* {}\n*Lowest:* {}\n*Highest:* {}\n*Open:* {}\n"
        return (message.format(data['name'], data['last'], data['low'], data['high'], data['open']))

    final_message = ''

    for data in datas:
        final_message = final_message + _message(data)

    return final_message


def telegram_send(chat_id, message):
    telegram_bot.send_message(chat_id, message)
    return True


def discord_send(url, message):
    webhook = DiscordWebhook(url=url, content=message)
    webhook.execute()
    return True


telegram_send(os.environ.get('TELEGRAM_CHAT_ID'), create_msg(datas))
discord_send(os.environ.get('DISCORD_WEBHOOK_URL'), create_msg(datas))
