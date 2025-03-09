import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
CURRENCY_API_KEY = os.getenv("CURRENCY_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")



def get_currency(code):
    """Функция конвертации"""
    amount = 1
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"
    headers = {"apikey": CURRENCY_API_KEY}
    response = requests.get(url, headers=headers)
    result = response.json()

    result = {"currency": code, "rate": round(result["result"], 2)}

    return (result)

def get_stock(stock):
    """Функция с акциями"""
    url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/prev?adjusted=true&apiKey={STOCK_API_KEY}"
    headers = {"apikey": STOCK_API_KEY}
    response = requests.get(url, headers=headers)
    result = response.json()

    result = {"stock": stock, "price": round(result["results"][0]["c"], 2)}

    return (result)