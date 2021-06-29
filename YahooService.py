import yfinance as yf
import datetime


class YahooService:

    coin_dict = {
        "Ether": "ETH",
        "Bitcoin": "BTC",
        "Cardano": "ADA",
        "Polkadot": "DOT1",
        "Stellar": "XLM",
        "Ripple": "XRP",
        "Litecoin": "LTC",
        "Doge": "DOGE"
    }

    def coin_dict_to_text(self):
        coins = ""
        for k, v in self.coin_dict.items():
            coins += f"{k} - {v}\n"
        return coins

    def generate_coin_id(self, coin_name, currency):
        proper_name = coin_name.capitalize()
        return f"{self.coin_dict[proper_name]}-{currency}"

    @staticmethod
    def get_data(token):
        ticker = yf.Ticker(token)
        now = datetime.datetime.now().date().isoformat()
        data = ticker.history(start=now, stop=now, interval="15m")
        return data["Close"][-1]


if __name__ == '__main__':
    kk = YahooService()
    a = kk.get_data('XLM-USD')