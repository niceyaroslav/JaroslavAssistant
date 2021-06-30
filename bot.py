from Constants import API_KEY
from YahooService import YahooService as ys
import telebot
from flask import Flask, request
import os

bot = telebot.TeleBot(API_KEY)
service = ys()
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text="""\
Hey buddy, I am CryptoPeaceDuke (read Crypto Pizdyuk, blyat).
Here you can ask me about the current prices for certain crypto coins. I will also periodically notify you If Stellar 
goes high in price, since my creator wants to ditch that shit real quick :)

To get a list of coins type "/coins".\
""")


@bot.message_handler(commands=['coins'])
def get_coin_list(message):
    bot.send_message(chat_id=message.chat.id, text=f"""\
Hey buddy! Here is the list of coins I can tell you price for:
{service.coin_dict_to_text()}
To get price of desired coin type coin "name, currency" like so -> Ether, USD\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


@bot.message_handler(regexp=r"[a-zA-Z]+,\s[a-zA-Z]{3}", content_types=["text"])
def get_price(message):
    words = message.text.split(", ")
    coin = words[0].capitalize()
    currency = words[1].upper()
    if coin in ys.coin_dict.keys():
        token = "-".join([ys.coin_dict[coin], currency])
        price = round(service.get_data(token), 4)
        bot.send_message(chat_id=message.chat.id, text=f"Current price for this coin is {price} {currency}")
    elif coin in ys.coin_dict.values():
        coin = coin.upper()
        token = "-".join([coin, currency])
        price = round(service.get_data(token), 4)
        bot.send_message(chat_id=message.chat.id, text=f"Current price for this coin is {price} {currency}")
    else:
        bot.send_message(chat_id=message.chat.id, text=f"Can't find data for {coin} :(")


@server.route('/' + API_KEY, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://jaroslav-bot.herokuapp.com/' + API_KEY)
    return "!", 200

# bot.polling(none_stop=True)


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 80)))

