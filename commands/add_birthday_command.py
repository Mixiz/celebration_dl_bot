import telebot


# Command start
def exec(bot: telebot.TeleBot, message):
    bot.send_message(message.chat.id, "dummy")
