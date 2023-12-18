import telebot
from telebot import types
from .api import weather_api

bot = telebot.TeleBot('6851193773:AAEVi8ps7IfuSKbQ8QNxucOFD3tXo_utuVc')

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == '👋 Hi~':
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Create new btn
#         btn1 = types.KeyboardButton('How to become an author on Habr?')
#         btn2 = types.KeyboardButton('Rule of site')
#         btn3 = types.KeyboardButton('Tips for designing a publication')
#         markup.add(btn1, btn2, btn3)
#         bot.send_message(message.from_user.id, '❓ Ask a question', reply_markup=markup)  # bor response
#     elif message.text == 'How to become an author on Habr?':
#         bot.send_message(message.from_user.id,
#                          'Вы пишете первый пост, его проверяют модераторы, и, если всё хорошо, отправляют в основную ленту Хабра, где он набирает просмотры, комментарии и рейтинг. В дальнейшем премодерация уже не понадобится. Если с постом что-то не так, вас попросят его доработать.\n \nПолный текст можно прочитать по ' + '[ссылке](https://habr.com/ru/sandbox/start/)',
#                          parse_mode='Markdown')

#     elif message.text == 'Rule of site':
#         bot.send_message(message.from_user.id,
#                          'Прочитать правила сайта вы можете по ' + '[ссылке](https://habr.com/ru/docs/help/rules/)',
#                          parse_mode='Markdown')

#     elif message.text == 'Tips for designing a publication':
#         bot.send_message(message.from_user.id,
#                          'Подробно про советы по оформлению публикаций прочитать по ' + '[ссылке](https://habr.com/ru/docs/companies/design/)',
#                          parse_mode='Markdown')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Hi~ I am a weather bot developed by Bayashat.\nTell me your city, to check the weather.")
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    city = message.text
    temperature = weather_api(city)
    bot.send_message(message.from_user.id, f"Weather of {city} is {temperature} °C")
    

# @bot.message_handler(commands=['end'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("🇰🇿 Қазақша")
#     btn2 = types.KeyboardButton('🇬🇧 English')
#     btn3 = types.KeyboardButton('🇷🇺 Русский')
    
#     markup.add(btn1, btn2, btn3)
     
#     bot.send_message(message.from_user.id, "🇰🇿 Тілді таңдаңыз /🇬🇧 Choose your language / 🇷🇺 Выберите язык ", reply_markup=markup)   

if __name__ == "__main__":
    bot.polling(none_stop=True)



