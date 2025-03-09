from datetime import datetime
from typing import Any

data_now = datetime(2021, 12, 5, 1, 1, 1)

def greetings(data_now: Any) -> str:
    hour = int(datetime.strftime(data_now, "%H"))
    if 0 <= hour < 5:
        print ("Доброй ночи")
    elif 5 < hour < 12:
        print ("Доброе утро")
    elif 12 < hour < 19:
        print ("Добрый день")
    else:
        print ("Добрый вечер")

print(greetings(data_now))