import logging

from logging_config import setup_logging

setup_logging()
logger = logging.getLogger("my_log")



def top_cashback_categories(data):
    """
        На вход функции поступают данные для анализа, год и месяц.
        На выходе — JSON с анализом, сколько на каждой категории можно заработать кешбэка в указанном месяце года,
        в формате:
        {"Категория 1": 1000,
        "Категория 2": 2000,
        "Категория 3": 500}
    """
    logger.info("Определяем все категории")
    new_lists = []
    for card_number in data:
        if "Категория" in card_number:
            if isinstance(card_number["Категория"], str):
                if card_number["Категория"] in new_lists:
                    continue
                else:
                    new_lists.append(card_number["Категория"])

    logger.info("Определяем сумму всех затрат по каждой категории")
    list = []
    for i in new_lists:
        sum = 0
        for operation in data:
            if "Сумма операции" in operation and "Статус" in operation:
                if operation["Статус"] == "OK":
                    if i == operation["Категория"]:
                        sum += operation["Сумма операции"]
        list.append(abs(sum))

    dict_list = dict(zip(new_lists, list))


    new_dict = {key: round(value * 0.01, 2) for key, value in dict_list.items()}

    logger.info("Сортируем и выводим")

    sorted_by_values = dict(sorted(new_dict.items(), key=lambda item: item[1], reverse=True))

    return (sorted_by_values)



