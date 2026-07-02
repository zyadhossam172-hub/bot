import telebot
import requests

# التوكنات الخاصة بك التي قمت بإرسالها
BOT_TOKEN = "8350793522:AAHbEDNEFruQFiNm-7S73pioYmWxYTZSbQw"
GEMINI_API_KEY = "AQ.Ab8RN6IKjnybhjuwrRyBdejR1FjLgQJB6jueWdazOVHL9TABFQ"

bot = telebot.TeleBot(BOT_TOKEN)

# دالة لإرسال الكلام لـ Gemini AI والمطالبة بالرد
def ask_gemini(user_message):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [{
            "parts": [{"text": user_message}]
        }]
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            return "عذراً، حدث خطأ في الاتصال بـ Gemini AI."
    except Exception as e:
        return "مشكلة في الشبكة، حاول مجدداً لاحقاً."

# استقبال أي رسالة نصية من المستخدم والرد عليها عبر Gemini
@bot.message_handler(func=lambda message: True)
def reply_with_gemini(message):
    # إظهار أن البوت يكتب الآن (Typing...)
    bot.send_chat_action(message.chat.id, 'typing')
    
    # إرسال الرسالة لجمناي وأخذ الرد
    gemini_response = ask_gemini(message.text)
    
    # الرد على المستخدم في تليجرام
    bot.reply_to(message, gemini_response)

print("البوت شغال ومربوط بـ Gemini AI...")
bot.infinity_polling()
