import json

import requests

BASE_URL = 'https://api.wazirx.com'

MARKET_STATUS_URL = '/api/v2/market-status'

MARKET_TICKER_URL = '/api/v2/tickers'

URL = BASE_URL + MARKET_TICKER_URL


def get_data(url, unit):
    data = {}
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    data = data.get(unit)
    return data


data = get_data(URL, 'dogeinr')
