import telebot
bot = telebot.TeleBot('964603618:AAF2JBJnsWqho3fFoY9tndxkRFjJKBPMILM')


@bot.message_handler(commands=['start'])
def test(message):
    bot.reply_to(message, f'Hi, I am bot of Jaroslav. Nice to meet you {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


bot.polling(none_stop=True)
