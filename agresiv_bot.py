import telebot
from token_1 import my_token

bot = telebot.TeleBot(my_token)
photo_url = "https://telegra.ph/file/f015154891ec60cbfa59e.png"


@bot.message_handler(commands=['start', 'info'])
def start(message):
    bot.send_message(message.chat.id, "Я бот, который способен только спамить!!!\n"
                     f"Поэтому ничем помочь я не могу {message.from_user.first_name}")


@bot.message_handler(content_types='text')
def spam(message):
    bot.send_photo(message.chat.id, photo=photo_url,
                   caption=' "Я научился писать телеграм ботов тут - https://stepik.org/course/107302/ '
                           ', а ты что сделал, а? А ну иди делом займись!"')

bot.polling(none_stop=True)
