import os
import telebot
from telebot import types
from flask import Flask, request

TOKEN = '5028040922:AAFw6VoiWkkAUf_V6E8YxDUGo420ng4bt6I'
APP_URL = f'https://botqo.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

# zzzzzzzzoooooooorrrr asdas
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(commands=['go'])
def start(message):
    bot.reply_to(message, 'Assalawma Aleykum!, ' + message.from_user.first_name)

@bot.message_handler(commands=['keste'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Заказать доставку')
    btn2 = types.KeyboardButton('О нас')
    markup.add(btn1, btn2)
    start_handler = f"<b>Привет {message.from_user.first_name}, что именно тебя интересует?</b>"
    bot.send_message(message.chat.id, start_handler, parse_mode='html', reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo(message):
    bot.reply_to(message, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
