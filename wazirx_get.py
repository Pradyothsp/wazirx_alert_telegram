import json

import requests

from log import logger

BASE_URL = 'https://api.wazirx.com'

MARKET_TICKER_URL = '/api/v2/tickers'

URL = BASE_URL + MARKET_TICKER_URL


def get_data(url, list_of_units):
    data = {}
    json_data = json.dumps(data)
    try:
        r = requests.get(url=url, data=json_data)
        logger.info('api data received')
        data = r.json()
        list_data = []
        for unit in list_of_units:
            list_data.append(data.get(unit))
        return list_data
    except:
        logger.error('api not working')


list_of_units = ['dogeinr', 'etcinr']
datas = get_data(URL, list_of_units)
# print(data)
