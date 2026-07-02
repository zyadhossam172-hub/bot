import telebot

BOT_TOKEN = "اكتب_التوكن_بتاعك_هنا"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f"أهلاً بك يا {user_name}! البوت شغال أونلاين على السيرفر بنجاح 🚀")

print("البوت شغال...")
bot.infinity_polling()
