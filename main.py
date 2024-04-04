import requests
import time
import telebot
import os


API_URL = "https://min-api.cryptocompare.com/data/pricemulti"
PRICE_KEY = os.getenv('PRICE_CURRENCY', "USD")
PADDING_STRING = f"{'='*20}"

bot = telebot.TeleBot(os.getenv("TOKEN"))

def fetch_data():
    while True:
        try:
            params = {
                'tsyms': PRICE_KEY,
                'fsyms': os.getenv('CURRENCIES', "BTC,ETH"),
            }
            response = requests.get(API_URL, params=params)
            data = response.json()
            msg = f"{PADDING_STRING}\n\n"
            for key in data:
                msg += f"{key}: {data[key][PRICE_KEY]}\n"
            msg += f"\n{PADDING_STRING}"
            bot.send_message(os.getenv("CHAT_ID"), msg)
        except Exception as e:
            print(f"error fecting data:{e}")

        time.sleep(60*int(os.environ.get("TIMEOUT", 60)))

if __name__ == "__main__":
    fetch_data()
