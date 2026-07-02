import telebot
import requests

# التوكنات الخاصة بك والمفتاح الجديد من Groq
BOT_TOKEN = "8350793522:AAHbEDNEFruQFiNm-7S73pioYmWxYTZSbQw"
GROQ_API_KEY = "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"

bot = telebot.TeleBot(BOT_TOKEN)

def ask_groq(user_message):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.1-8b-instant",  # نموذج سريع جداً وذكي
        "messages": [{"role": "user", "content": user_message}]
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return "عذراً، حدث خطأ في الاتصال بالسيرفر."
    except Exception as e:
        return "مشكلة في الشبكة، حاول مجدداً لاحقاً."

@bot.message_handler(func=lambda message: True)
def reply_with_groq(message):
    # إظهار أن البوت يكتب الآن (Typing...)
    bot.send_chat_action(message.chat.id, 'typing')
    
    # إرسال الرسالة إلى Groq وأخذ الرد
    response_text = ask_groq(message.text)
    
    # الرد على المستخدم في تليجرام
    bot.reply_to(message, response_text)

print("البوت شغال ومربوط بـ Groq...")
bot.infinity_polling()
