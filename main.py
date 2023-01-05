import telebot
import private_config
from commands import *

bot = telebot.TeleBot(private_config.token)


@bot.message_handler(commands=['help'])
def help(message):
    help_command.exec(bot, message)


@bot.message_handler(commands=['start'])
def start(message):
    start_command.exec(bot, message)


print('Start')
bot.polling(none_stop=True)
