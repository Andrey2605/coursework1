import json

import pandas as pd


def get_transactions_excel(file_path)->list:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями."""
    try:
        transactions_excel = pd.read_excel(file_path)
        transact_excel = transactions_excel.to_dict(orient="records")
        return transact_excel
    except FileNotFoundError:
        return []

def get_json_currency(file_path)->list:
    """ Функция, принимающая путь к JSON файлу и возвращающая список данных из файла. """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if "user_currencies" in data:
                result = data["user_currencies"]

        return result

    except FileNotFoundError:
        return []

def get_json_stock(file_path)->list:
    """ Функция, принимающая путь к JSON файлу и возвращающая список данных из файла."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if "user_stocks" in data:
                result = data["user_stocks"]

        return result

    except FileNotFoundError:
        return []


def get_xlsx(path: str) -> tuple[list[dict], pd.DataFrame]:
    """Функция, принимающая путь до Excel-файла и возвращающая список словарей и DataFrame."""
    return pd.read_excel(path)

