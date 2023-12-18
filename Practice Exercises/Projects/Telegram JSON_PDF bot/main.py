import io
import json, requests, telebot, config
from reportlab.pdfgen import canvas 

bot = telebot.TeleBot(config.token)
BASE_URL = "https://api.telegram.org/bot"


@bot.message_handler(commands=['start'])
def send_start_message(message):
    chat_id = message.chat.id
    text_to_send = f'Привет, ваш chat_id={chat_id}'
    who_is = message.from_user

    send_message(bot.token, chat_id, text_to_send + '\n' + str(who_is))


def send_message(token, chat_id, text):
    url = f'{BASE_URL}{token}/sendMessage'  # https://api.telegram.org/bot{token}/sendMessage?chat_id=1241221&&text=Hello
    params = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, params=params)

    if response.status_code == 200:
        print('Сообщение успешно отправлено')
    else:
        print(f'Ошибка при отправке сообщения. Код ошибки: {response.status_code}')

states = {}

@bot.message_handler(commands=['pdf'])
def start_create_pdf(message):
    # initialize state for user
    states[message.chat.id] = {'waiting_for_json': True}
    
    # ask json-string from user
    bot.send_message(message.chat.id, 'Do you want to create PDF from JSON?  Send me JSON-string.')
    

@bot.message_handler(func=lambda message: states.get(message.chat.id, {}).get('waiting_for_json', False))
def handle_json_input(message):
    try:
        json_data = message.text
        data = json.loads(json_data)
        
        pdf_file = io.BytesIO()
        pdf = canvas.Canvas(pdf_file)
        pdf.drawString(100, 750, str(data))
        pdf.save()
        
        pdf_file.seek(0)
        
        send_document(bot.token, message.chat.id, pdf_file)
        
        # reset the state
        states[message.chat.id] = {}
            
    except json.JSONDecodeError:
        bot.reply_to(message, 'Error parsing JSON. Please send a valid JSON string')
        

def send_document(token, chat_id, document):
    url = f"{BASE_URL}{token}/sendDocument"
    files = {'document': ('document.pdf', document)}
    
    response = requests.post(url, params={'chat_id': chat_id}, files=files)
    
    if response.status_code == 200:
        print('Message sent successfully')
    else:
        print(f'An error occurred while sending message. Err code: {response.status_code}')


if __name__ == "__main__":
    bot.polling(none_stop=True)