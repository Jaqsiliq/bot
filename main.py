import os
import telebot
from telebot import types
from flask import Flask, request
from keste import keste
import confyg_1

TOKEN = '5028040922:AAFw6VoiWkkAUf_V6E8YxDUGo420ng4bt6I'
APP_URL = f'https://botqo.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
tekst = "<b>Aqırģı márte " + confyg_1.janalangan_waqit + " jańalandı.</b>\nKestede qátelerdi bayqasańız,\ndekanatqa xabarlasıń."





@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=2, one_time_keyboard=True)
    btn1 = types.KeyboardButton('1')
    btn2 = types.KeyboardButton('2')
    btn3 = types.KeyboardButton('3')
    btn4 = types.KeyboardButton('4')
    markup.add(btn1, btn2, btn3, btn4)
    start_handler = f"<b>Assalawma Aleykum {message.from_user.first_name} ! Kursni tanlang:</b>"
    bot.send_message(message.chat.id, start_handler, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def topar(message):
    get_message_bot = message.text
    if get_message_bot == "1":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=3) #one_time_keyboard=True сразу убирает клаву, после нажатия

        btn1 = types.KeyboardButton('1 KI (qq)')
        btn2 = types.KeyboardButton('1 AT (qq)')
        btn3 = types.KeyboardButton('1 DI (qq)')
        btn4 = types.KeyboardButton('1 KT (qq)')
        btn5 = types.KeyboardButton('1 Tel (qq)')
        btn6 = types.KeyboardButton('1 AX (qq)')
        btn7 = types.KeyboardButton('1 RI (qq)')
        btn8 = types.KeyboardButton('1 KI (o\'zb)')
        btn9 = types.KeyboardButton('1 AT (o\'zb)')
        btn10 = types.KeyboardButton('1 DI (o\'zb)')
        btn11 = types.KeyboardButton('1 KT (o\'zb)')
        btn12 = types.KeyboardButton('1 Tel (o\'zb)')
        btn13 = types.KeyboardButton('1 AX (o\'zb)')
        btn14 = types.KeyboardButton('1 RI (o\'zb)')
        btn15 = types.KeyboardButton('1 KI (rus)')
        btn16 = types.KeyboardButton('1 AT (rus)')
        btn17 = types.KeyboardButton('1 DI (rus)')
        btn18 = types.KeyboardButton('1 KT (rus)')
        btn19 = types.KeyboardButton('1 Tel (rus)')
        btn20 = types.KeyboardButton('1 AX (rus)')
        btn21 = types.KeyboardButton('1 RI (rus)')
        markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn14,btn15,btn16,btn17,btn18,btn19,btn20,btn21)
        send_mess = f"<b>Guruh tanlang:</b>"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, askname)

    if get_message_bot == "2":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=3) #one_time_keyboard=True сразу убирает клаву, после нажатия

        btn1 = types.KeyboardButton('2 KI (qq)')
        btn2 = types.KeyboardButton('2 AT (qq)')
        btn3 = types.KeyboardButton('2 DI (qq)')
        btn4 = types.KeyboardButton('2 KT (qq)')
        btn5 = types.KeyboardButton('2 Tel (qq)')
        btn6 = types.KeyboardButton('2 AX (qq)')
        #btn7 = types.KeyboardButton('1 RI (qq)')
        btn8 = types.KeyboardButton('2 KI (o\'zb)')
        btn9 = types.KeyboardButton('2 AT (o\'zb)')
        btn10 = types.KeyboardButton('2 DI (o\'zb)')
        btn11 = types.KeyboardButton('2 KT (o\'zb)')
        btn12 = types.KeyboardButton('2 Tel (o\'zb)')
        btn13 = types.KeyboardButton('2 AX (o\'zb)')
        #btn14 = types.KeyboardButton('1 RI (o\'zb)')
        btn15 = types.KeyboardButton('2 KI (rus)')
        btn16 = types.KeyboardButton('2 AT (rus)')
        btn17 = types.KeyboardButton('2 DI (rus)')
        btn18 = types.KeyboardButton('2 KT (rus)')
        btn19 = types.KeyboardButton('2 Tel (rus)')
        btn20 = types.KeyboardButton('2 AX (rus)')
        #btn21 = types.KeyboardButton('1 RI (rus)')
        markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn8,btn9,btn10,btn11,btn12,btn13,btn15,btn16,btn17,btn18,btn19,btn20)
        send_mess = f"<b>Guruh tanlang:</b>"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, askname)

    if get_message_bot == "3":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=3) #one_time_keyboard=True сразу убирает клаву, после нажатия

            btn1 = types.KeyboardButton('3 KI (qq)')
            btn2 = types.KeyboardButton('3 AT (qq)')
            btn3 = types.KeyboardButton('3 DI (qq)')
            btn4 = types.KeyboardButton('3 KT (qq)')
            btn5 = types.KeyboardButton('3 Tel (qq)')
            btn6 = types.KeyboardButton('3 AX (qq)')
            #btn7 = types.KeyboardButton('1 RI (qq)')
            btn8 = types.KeyboardButton('3 KI (o\'zb)')
            btn9 = types.KeyboardButton('3 AT (o\'zb)')
            btn10 = types.KeyboardButton('3 DI (o\'zb)')
            btn11 = types.KeyboardButton('3 KT (o\'zb)')
            btn12 = types.KeyboardButton('3 Tel (o\'zb)')
            btn13 = types.KeyboardButton('3 AX (o\'zb)')
            #btn14 = types.KeyboardButton('1 RI (o\'zb)')
            btn15 = types.KeyboardButton('3 KI (rus)')
            btn16 = types.KeyboardButton('3 AT (rus)')
            btn17 = types.KeyboardButton('3 DI (rus)')
            btn18 = types.KeyboardButton('3 KT (rus)')
            btn19 = types.KeyboardButton('3 Tel (rus)')
            btn20 = types.KeyboardButton('3 AX (rus)')
            #btn21 = types.KeyboardButton('1 RI (rus)')
            markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn8,btn9,btn10,btn11,btn12,btn13,btn15,btn16,btn17,btn18,btn19,btn20)
            send_mess = f"<b>Guruh tanlang:</b>"
            bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(message, askname)

    if get_message_bot == "4":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=3) #one_time_keyboard=True сразу убирает клаву, после нажатия

            btn1 = types.KeyboardButton('4 KI (qq)')
            btn2 = types.KeyboardButton('4 AT (qq)')
            btn3 = types.KeyboardButton('4 DI (qq)')
            btn4 = types.KeyboardButton('4 KT (qq)')
            btn5 = types.KeyboardButton('4 Tel (qq)')
            btn6 = types.KeyboardButton('4 AX (qq)')
            #btn7 = types.KeyboardButton('1 RI (qq)')
            btn8 = types.KeyboardButton('4 KI (o\'zb)')
            btn9 = types.KeyboardButton('4 AT (o\'zb)')
            btn10 = types.KeyboardButton('4 DI (o\'zb)')
            btn11 = types.KeyboardButton('4 KT (o\'zb)')
            btn12 = types.KeyboardButton('4 Tel (o\'zb)')
            btn13 = types.KeyboardButton('4 AX (o\'zb)')
            #btn14 = types.KeyboardButton('1 RI (o\'zb)')
            btn15 = types.KeyboardButton('4 KI (rus)')
            btn16 = types.KeyboardButton('4 AT (rus)')
            btn17 = types.KeyboardButton('4 DI (rus)')
            btn18 = types.KeyboardButton('4 KT (rus)')
            btn19 = types.KeyboardButton('4 Tel (rus)')
            btn20 = types.KeyboardButton('4 AX (rus)')
            #btn21 = types.KeyboardButton('1 RI (rus)')
            markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn8,btn9,btn10,btn11,btn12,btn13,btn15,btn16,btn17,btn18,btn19,btn20)
            send_mess = f"<b>Guruh tanlang:</b>"
            bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(message, askname)


def askname(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    button_text = message.text
# 1-kurslar
    if button_text == '1 KI (qq)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst, reply_markup=types.ReplyKeyboardRemove(selective=False),
                            parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 AT (qq)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 DI (qq)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 KT (qq)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 Tel (qq)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 AX (qq)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 RI (qq)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 KI (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 AT (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 DI (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 KT (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 Tel (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 AX (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 RI (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 KI (rus)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 AT (rus)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 DI (rus)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 KT (rus)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 Tel (rus)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 AX (rus)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '1 RI (rus)':
        bot.send_message(message.chat.id, keste(button_text, 1) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)


# 2-kurslar


    if button_text == '2 KI (qq)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst, reply_markup=types.ReplyKeyboardRemove(selective=False),
                            parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 AT (qq)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 DI (qq)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 KT (qq)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 Tel (qq)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 AX (qq)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)


    if button_text == '2 KI (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 AT (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 DI (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 KT (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 Tel (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 AX (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)


    if button_text == '2 KI (rus)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 AT (rus)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 DI (rus)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 KT (rus)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 Tel (rus)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '2 AX (rus)':
        bot.send_message(message.chat.id, keste(button_text, 2) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)




# 3-kurslar


    if button_text == '3 KI (qq)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst, reply_markup=types.ReplyKeyboardRemove(selective=False),
                            parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 AT (qq)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 DI (qq)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 KT (qq)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 Tel (qq)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 AX (qq)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)


    if button_text == '3 KI (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 AT (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 DI (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 KT (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 Tel (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 AX (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)


    if button_text == '3 KI (rus)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 AT (rus)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 DI (rus)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 KT (rus)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 Tel (rus)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '3 AX (rus)':
        bot.send_message(message.chat.id, keste(button_text, 3) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)




# 4-kurslar


    if button_text == '4 KI (qq)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst, reply_markup=types.ReplyKeyboardRemove(selective=False),
                            parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 AT (qq)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 DI (qq)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 KT (qq)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 Tel (qq)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 AX (qq)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)


    if button_text == '4 KI (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 AT (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 DI (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 KT (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 Tel (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 AX (o\'zb)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)


    if button_text == '4 KI (rus)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 AT (rus)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 DI (rus)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 KT (rus)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 Tel (rus)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),

        markup = types.ReplyKeyboardRemove(selective=False)

    if button_text == '4 AX (rus)':
        bot.send_message(message.chat.id, keste(button_text, 4) + tekst,
                         reply_markup=types.ReplyKeyboardRemove(selective=False),
                         parse_mode='html')
        markup = types.ReplyKeyboardRemove(selective=False)



















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
