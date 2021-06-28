import os
# import logging
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import telebot


TOKEN = '964603618:AAF2JBJnsWqho3fFoY9tndxkRFjJKBPMILM'
PORT = int(os.environ.get('PORT', 8443))
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


bot.polling(none_stop=True)
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)
#
# logger = logging.getLogger(__name__)

#
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id,
#                              text="I'm a bot, please talk to me!")
#
#
# def helpp(update, context):
#     """Send a message when the command /help is issued."""
#     context.bot.send_message(chat_id=update.effective_chat.id,
#                              text="No help for U, bech!")
#
#
# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id,
#                              text=update.message.text)
#
#
# def error(update, context):
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, context.error)
#
#
# def main():
#     """Start the bot."""
#     # Create the Updater and pass it your bot's token.
#     # Make sure to set use_context=True to use the new context based callbacks
#     # Post version 12 this will no longer be necessary
#     updater = Updater(TOKEN, use_context=True)
#
#     # Get the dispatcher to register handlers
#     dp = updater.dispatcher
#
#     # on different commands - answer in Telegram
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("help", help))
#
#     # on noncommand i.e message - echo the message on Telegram
#     dp.add_handler(MessageHandler(Filters.text, echo))
#
#     # log all errors
#     dp.add_error_handler(error)
#
#     # Start the Bot
#     updater.start_webhook(listen="0.0.0.0",
#                           port=int(PORT),
#                           url_path=TOKEN,
#                           webhook_url='https://jaroslav-bot.herokuapp.com/' + TOKEN)
#
#     # Run the bot until you press Ctrl-C or the process receives SIGINT,
#     # SIGTERM or SIGABRT. This should be used most of the time, since
#     # start_polling() is non-blocking and will stop the bot gracefully.
#     updater.idle()


# if __name__ == '__main__':
#     main()

