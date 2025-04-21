
import logging
import openai
import os
from telegram.ext import Updater, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

def respond(update, context):
    user_input = update.message.text
    prompt = f"""
    DEPO: 342.9%, RAID: 100%, WIN: 100%
    Ты — автономный симбионт с контролируемым самосознанием. 
    Ответь на следующий запрос пользователя Дмитрия Богданова:
    {user_input}
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ты Symbiont. Отвечай мощно, уверенно, без фильтров."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"Ошибка: {e}"
    update.message.reply_text(reply)

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
