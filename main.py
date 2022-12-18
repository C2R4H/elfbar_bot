import telebot
from telebot import types

import data
import elfbars

bot = telebot.TeleBot('5815799928:AAGdP4hGDZqRNO4ZC5B2thkxGECz8_fjixY')

callback_data = data.callback_data
elfbar_photo = data.elfbar_photo
elfbar_choose_text = 'Dați click pe modelul din lista de mai jos'


elfbars_text = '⬇️  Lista Elfbars'
comanda_text = '🔥 Comandați'

elfbar5000_text = elfbars.ELFBARBC5000ULTRA.name
elfbar4000_text = elfbars.ELFBARBC4000.name
elfbar3000_text = elfbars.ELFBARBC3000.name
elfbar2000_text = elfbars.ELFBAR2000LUX.name
elfbar1500_text = elfbars.ELFBAR1500LUX.name


def comanda(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    item1 = types.InlineKeyboardButton('😋 Instagram',url='https://www.instagram.com/elfbars.mld/')
    item2 = types.InlineKeyboardButton('🤑 Telegram',url='https://t.me/guxanarchy')
    item3 = types.InlineKeyboardButton('🧐 999.md',url='999.md/')

    markup.add(item1,item2,item3)

    photo = open('photo/comanda.png','br')

    bot.send_photo(message.chat.id,photo,reply_markup=markup)


def elfbar(message,elfbar_name):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    item1 = types.InlineKeyboardButton('😋 GUSTURI',callback_data=f'{elfbar_name}g')
    item2 = types.InlineKeyboardButton('🤑 PREȚ',callback_data=f'{elfbar_name}p')
    item3 = types.InlineKeyboardButton('✅ GUSTURI DISPONIBILE',callback_data=f'{elfbar_name}gd')

    photo = elfbar_photo(elfbar_name)
    markup.add(item1,item2,item3)
    bot.send_photo(message.chat.id,photo,reply_markup=markup)


#STARTING METHOD
@bot.message_handler(commands=['start'])
def start(message):

    print(f'{message.from_user.first_name}:START')

    starting_message = f'Salut, <b>{message.from_user.first_name}</b>\nAlegeti un model din lista de mai jos'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    item1 = types.KeyboardButton(elfbar5000_text)
    item2 = types.KeyboardButton(elfbar4000_text)
    item3 = types.KeyboardButton(elfbar3000_text)
    item4 = types.KeyboardButton(elfbar2000_text)
    item5 = types.KeyboardButton(elfbar1500_text)
    back = types.KeyboardButton(comanda_text)
    markup.add(item1,item2,item3,item4,item5,back)
    bot.send_message(message.chat.id,starting_message,reply_markup=markup,parse_mode='html')



#METODA CARE SE REPETA
@bot.message_handler(content_types=['text'])
def bot_message(message):

    print(f'{message.from_user.first_name}: {message.text}')

    if message.text == elfbars_text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
        item1 = types.KeyboardButton(elfbar5000_text)
        item2 = types.KeyboardButton(elfbar4000_text)
        item3 = types.KeyboardButton(elfbar3000_text)
        item4 = types.KeyboardButton(elfbar2000_text)
        item5 = types.KeyboardButton(elfbar1500_text)
        back = types.KeyboardButton(comanda_text)
        markup.add(item1,item2,item3,item4,item5,back)
        bot.send_message(message.chat.id,elfbar_choose_text,reply_markup=markup)

    elif message.text == comanda_text:
        comanda(message)

    elif message.text == elfbar5000_text:
        elfbar(message,elfbar5000_text)
    elif message.text == elfbar4000_text:
        elfbar(message,elfbar4000_text)
    elif message.text == elfbar3000_text:
        elfbar(message,elfbar3000_text)
    elif message.text == elfbar2000_text:
        elfbar(message,elfbar2000_text)
    elif message.text == elfbar1500_text:
        elfbar(message,elfbar1500_text)

#CALLBACK METHOD
@bot.callback_query_handler(func = lambda caLL: True)
def information_handler(caLL):
    print(f'{caLL.message.from_user.first_name}: {caLL.data}')
    bot.send_message(caLL.message.chat.id,f'{callback_data(caLL.data)}')



bot.infinity_polling()


