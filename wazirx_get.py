import json

import requests

BASE_URL = 'https://api.wazirx.com'

MARKET_STATUS_URL = '/api/v2/market-status'

MARKET_TICKER_URL = '/api/v2/tickers'

URL = BASE_URL + MARKET_TICKER_URL


def get_data(url, list_of_units):
    data = {}
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    list_data = []
    for unit in list_of_units:
        list_data.append(data.get(unit))
    return list_data


list_of_units = ['etcinr', 'dogeinr']
datas = get_data(URL, list_of_units)
# print(data)
