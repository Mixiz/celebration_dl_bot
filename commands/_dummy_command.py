import telebot


# Template Dummy Command
def exec(bot: telebot.TeleBot, message):
    bot.send_message(message.chat.id, "dummy")
