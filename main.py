import telebot

TOKEN_BOT = ""
bot = telebot.TeleBot(token=TOKEN_BOT)


@bot.message_handler(content_types=["new_chat_members"])
def new_chat_members(m):
    bot.ban_chat_member(m.chat.id, m.from_user.id, 0)
    bot.unban_chat_member(m.chat.id, m.from_user.id)


bot.polling()
