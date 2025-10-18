import requests


def parse_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",  # какие валюты получаем
        "vs_currencies": "usd"  # в каких валютах показывать цену
    }

    response = requests.get(url, params=params)
    data = response.json()  # преобразуем JSON в Python-словарь

    # Преобразуем результат в список списков — удобно для записи в Google Sheets
    result = []
    for coin, price in data.items():
        result.append([coin, price['usd']])

    return result

