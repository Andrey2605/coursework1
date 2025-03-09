from datetime import datetime

import pytest

from src.views import greetings




data_now = datetime(2021, 12, 5, 1, 1, 1)


def test_greetings():
    assert greetings(data_now) == "Доброй ночи"
