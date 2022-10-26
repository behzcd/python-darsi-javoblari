# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 22:53:51 2022

@author: Administrator
"""
#https://github.com/kodchi/uzbek-transliterator.git
#https://github.com/eternnoir/pyTelegramBotAPI


from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '5798225165:AAFbLfu42IY8Z3kLnv9oGriUEWRTSGB6Ps4'
bot = telebot.TeleBot("TOKEN", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, hush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob)

bot.infinity_polling()


# matn = input("Matn kiriting:")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
   
