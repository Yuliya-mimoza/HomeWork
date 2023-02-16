import telebot
import wikipedia
bot = telebot.TeleBot('6167930148:AAGsB_9kJylr6IugQRIiOly53hNiMlXtkuo')
@bot.message_handler(content_types=['text'])


def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Напиши любое слово и я напишу его значение в википедии")
    else:
        get_text_messages(message)


def get_text_messages(message):
    try:
        wikipedia.set_lang("ru")
        bot.send_message(message.from_user.id,
                         wikipedia.summary(str(message.txt)))
    except:
        bot.send_message(message.from_user.id, "Такого слова нет в википедии")
        bot.send_message(message.from_user.id, """ Можете найти в интернете по ссылке: 
        """+"""https://yandex.ru/search/?clid=2186621&text="""+message.text.replace(' ', '+') +
                         """&lr=56&redircnt=1643944361.1""")


bot.polling(none_stop=True, interval=0)
