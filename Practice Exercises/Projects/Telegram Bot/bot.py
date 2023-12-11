import config
import telebot
import os
from PIL import ImageGrab
from datetime import datetime

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Скриншот алу")
    markup.add("Файлдар құру")
    bot.reply_to(message, "👋Helloooo", reply_markup=markup)

@bot.message_handler(regexp='Скриншот алу')
def send_screenshot(message):
    path = os.getcwd()+'/screenshot.png'
    try:
        # Take a screenshot
        screenshot = ImageGrab.grab()

        # Convert the screenshot to bytes
        screenshot.save(path, 'PNG')
        print("scrennshot saved")

        # Send the screenshot
        photo = open(path, 'rb')
        bot.reply_to(message, f"Скриншот алынып жатыр... {datetime.now()}")
        bot.send_photo(message.chat.id, photo)
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

@bot.message_handler(regexp='Файлдар құру')
def send_screenshot(message):
    os.chdir('C:\\Users\\baias\\Desktop\\')
    for i in range(1, 11):
        with open(f"Batyr {i+1}.csv", 'a') as file:
            file.write("Love you")
    bot.reply_to(message, f"Файлдар құрылып жатыр... {datetime.now()}")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.send_message(message.chat.id, message.text)
 
bot.infinity_polling()