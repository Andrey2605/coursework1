from datetime import datetime

from settings import JSON_PATH, EXCEL_PATH
from src.external_api import get_currency, get_stock
from src.reports import spending_by_category
from src.services import top_cashback_categories
from src.utils import get_json_currency, get_json_stock, get_xlsx
from src.views import sort_by_date, info_card, top_5
from views import greetings


def main():

    """Главная"""

    """Функцию, принимающую на вход строку с датой и временем в формате YYYY-MM-DD HH:MM:SS"""
    data_now = datetime.now()



    """Приветствие """

    greeting = greetings(data_now)

    """Сортиовка по полседним транзакциям настоящего месяца"""

    sort_list = sort_by_date(data_now)


    cards = info_card(sort_list)

    """Топ-5 транзакций"""

    top_transactions = top_5(sort_list)

    """Курсы валют"""

    currency_rates = [get_currency(code) for code in get_json_currency(JSON_PATH)]

    """Акции"""

    stock_prices = [get_stock(stock) for stock in get_json_stock(JSON_PATH)]


    result = {
        "greeting": greeting,
        "cards": cards,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices,
    }


    """События"""

    """Выгодные категории повышенного кешбэка"""

    services = top_cashback_categories(sort_list)

    """Отчеты"""

    """Траты по категории"""

    df = get_xlsx(EXCEL_PATH)

    sped = spending_by_category(df , "Каршеринг")


if __name__ == "__main__":
    main()
