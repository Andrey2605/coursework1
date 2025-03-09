from datetime import datetime

from typing import Any

from settings import EXCEL_PATH

import logging

from logging_config import setup_logging

setup_logging()
logger = logging.getLogger("my_log")


def greetings(data_now: Any) -> str:
    """
        Функция, принимающая время в виде строки и возвращающая приветствие в зависимости от времени суток.
    """

    logger.info("Определяем какое приветствие подойдет для текущего времени суток")

    hour = int(datetime.strftime(data_now, "%H"))
    if 0 <= hour < 5:
        return("Доброй ночи")
    elif 5 < hour < 12:
        return("Доброе утро")
    elif 12 < hour < 19:
        return("Добрый день")
    else:
        return("Добрый вечер")

    logger.info("Приветствие определено успешно")


def sort_by_date(data_now):
    """
        Функция, получающая список словарей с операциями и дату, возвращающая список, отфильтрованный
        по дате с начала месяца, на который выпадает входящая дата, по входящую дату.
    """
    logger.info("Определяем дату и сортируем по дате")

    excel_dict = get_transactions_excel(EXCEL_PATH)
    data_str = data_now.strftime("01.%m.%Y %H:%M:%S")
    data_one = datetime.strptime(data_str, "%d.%m.%Y %H:%M:%S")
    new_list = []
    for dictonary in excel_dict:
        if "Дата операции" in dictonary:
            date_list = datetime.strptime(dictonary["Дата операции"], "%d.%m.%Y %H:%M:%S")
            if data_one <= date_list <= data_now:
                new_list.append(dictonary)
    return new_list

    logger.info("Список словарей успешно отсортирован")

def info_card(sort_list):
    """
        Функция, принимающая список операций и возвращающая список словарей с данными о картах:
        последние 4 цифры карты, общая сумма расходов, кешбэк (1 рубль на каждые 100 рублей) в формате
        [{"last_digits": "4 последние цифры номера карты",
          "total_spent": сумма расходов,
          "cashback": кэшбек},
        {...}]
    """

    logger.info("Определяем все карты")

    new_list = []
    for card_number in sort_list:
        if "Номер карты" in card_number:
            if isinstance(card_number["Номер карты"], str):
                if card_number["Номер карты"] in new_list:
                    continue
                else:
                    new_list.append(card_number["Номер карты"])

    logger.info("Определяем сумму всех затрат по каждой карте")

    list = []
    for i in new_list:
        sum = 0
        for operation in sort_list:
            if "Сумма операции" in operation and "Статус" in operation:
                if operation["Статус"] == "OK":
                    if i == operation["Номер карты"]:
                        sum += operation["Сумма операции"]
        list.append(abs(sum))

    dict_list = dict(zip(new_list, list))

    logger.info("Выводим список словарей с данными по картам")

    result = []
    for key, valye in dict_list.items():
        last_digits = key
        total_spent = valye
        cashback = total_spent * 0.01

        result.append({"last_digits": last_digits,
                       "total_spent": round(total_spent, 2),
                       "cashback": round(cashback, 2)})

    return result



def top_5(sorted_list):
    """
        Функция, принимающая список словарей с операциями и возвращающая список из топ-5 транзакций по сумме
        в формате:
        [{"date": "дата",
          "amount": сумма,
          "category": "категория",
          "description": "описание"},
        {...}]
    """
    logger.info("Выполняем сортировку топ-5 транзакций")

    sorted_transactions = sorted(sorted_list, key=lambda x: abs(x["Сумма платежа"]), reverse=True)
    result = []
    for top in sorted_transactions[:5]:
        date = top["Дата операции"].split()[0]
        amount = abs(top["Сумма операции"])
        category = top["Категория"]
        description = top["Описание"]

        info = {"date": date, "amount": round(amount, 2), "category": category, "description": description}
        result.append(info)

    return(result)
