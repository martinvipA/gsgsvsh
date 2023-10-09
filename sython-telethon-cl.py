import requests
import telebot
import os
api_token = '6387001801:AAHO-ZjQTEqkM9-mHJAFxb1UBel0CYnNSyg'
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مـرحـبـا ارسـل نـص لـتـحـويـلـه لـبـصـمـه بـصـوت قـوقـل")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    url = f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=ar&q={text}"
    response = requests.get(url)

    if response.status_code == 200:
        file_name = f"{message.from_user.id}.mp3"
        with open(file_name, 'wb') as file:
            file.write(response.content)

        with open(file_name, 'rb') as file:
            bot.send_voice(message.chat.id, file)

        # Delete the audio file after sending
        os.remove(file_name)
    else:
        bot.reply_to(message, "خطا")

bot.polling()
