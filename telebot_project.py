from transliterate import  to_cyrillic, to_latin
import telebot

TOKEN='1992391532:AAHWZLZcSY53x3Vbef3mlEKS-ZqJibaT0f8'

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalumu alaykum, Xush kelibsiz!"
    javob+=  "\nMatn kiriting:"
    bot.reply_to(message, javob)
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg= message.text
    javob= lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin()
    # if msg.isascii():
    #     javob= to_cyrillic(msg)
    # else:
    #      javob= to_latin(msg)
    bot.reply_to(message, javob(msg))

    
bot.polling()
