import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


# Do not exceed 5000 symbols
def get_help_text():
    return """
/start - Do the main add birthday scenario
/add_birthday - Add info about birthday
/get_birthdays - Get all saved birthdays
    """


# Command help
def exec(bot: telebot.TeleBot, message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Start", callback_data='c start'))
    markup.add(InlineKeyboardButton("Add Birthday", callback_data='c add_birthday'))
    markup.add(InlineKeyboardButton("Get Birthdays", callback_data='c get_birthdays'))
    bot.send_message(message.chat.id, get_help_text(), reply_markup=markup)
