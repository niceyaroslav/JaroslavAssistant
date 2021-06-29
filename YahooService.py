import yfinance as yf
import datetime

class YahooService:

    coin_dict = {
        "Ether": "",
        "Bitcoin": "",
        "Cardano": "",
        "Polkadot": "",
        "Stellar": "",
        "Ripple": "",
        "Tezos": "",
        "Litecoin": ""
    }

    @staticmethod
    def get_data(token):
        ticker = yf.Ticker(token)
        data = ticker.history(period="max")
        return data

kk = YahooService()
a = kk.get_data('XLM-EUR')