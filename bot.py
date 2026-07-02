import telebot

BOT_TOKEN = "8350793522:AAHbEDNEFruQFiNm-7S73pioYmWxYTZSbQw"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا زياد! بوت التليجرام بتاعك شغال بنجاح فوراً 🚀")

print("البوت مستعد وشغال...")
bot.infinity_polling()