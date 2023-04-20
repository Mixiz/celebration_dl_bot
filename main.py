import telebot
from telebot.types import CallbackQuery
import private_config
from commands import *

bot = telebot.TeleBot(private_config.token)


@bot.message_handler(commands=['help'])
def help(message):
    help_command.exec(bot, message)


@bot.message_handler(commands=['start'])
def start(message):
    start_command.exec(bot, message)


@bot.message_handler(commands=['add_birthday'])
def add_birthday(message):
    add_birthday_command.exec(bot, message)


@bot.message_handler(commands=['get_birthdays'])
def get_birthdays(message):
    get_birthdays_command.exec(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    print(f'test query handler {call.from_user.username} {call.data}')
    # command = cb_query.data['command']
    bot.send_message(call.message.chat.id, "You send command")


print('Start')
bot.polling(none_stop=True)
