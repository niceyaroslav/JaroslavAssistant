from Constants import API_KEY
from YahooService import YahooService as ys
import telebot


bot = telebot.TeleBot(API_KEY)
service = ys()


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
To get price of desired coin type coin name, currency like so -> Ether, USD"\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


@bot.message_handler(regexp=r"[a-zA-Z]+,\s[a-zA-Z]{3}", content_types=["text"])
def get_price(message):
    words = message.text.split(", ")
    if words[0].capitalize() in ys.coin_dict.keys():
        token = "-".join([ys.coin_dict[words[0]], words[1].upper()])
        price = round(service.get_data(token), 4)
        bot.send_message(chat_id=message.chat.id, text=f"Current price for this coin is {price} {words[1]}")
    else:
        bot.send_message(chat_id=message.chat.id, text=f"Can't find data on this coin :(")


bot.polling(none_stop=True)

