from config import db_connection
from telebot import types


# Command help
def exec(bot, message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("help"))
    markup.add(types.KeyboardButton("start"))
    bot.send_message(message.chat.id, "reply", reply_markup=markup)
