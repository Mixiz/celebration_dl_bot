import telebot
from db_connection.db_connection import get_user_birthdays


# Command start
def exec(bot: telebot.TeleBot, message):
    bot.send_message(message.chat.id, get_user_birthdays(message.from_user.id), reply_markup='')
