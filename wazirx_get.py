import json
import logging

import requests

BASE_URL = 'https://api.wazirx.com'

MARKET_TICKER_URL = '/api/v2/tickers'

URL = BASE_URL + MARKET_TICKER_URL

logging.basicConfig(filename='logs.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO,
                    )


def get_data(url, list_of_units):
    data = {}
    json_data = json.dumps(data)
    try:
        r = requests.get(url=url, data=json_data)
        data = r.json()
        list_data = []
        for unit in list_of_units:
            list_data.append(data.get(unit))
        return list_data
    except:
        logging.warning('api not working')


list_of_units = ['dogeinr', 'etcinr']
datas = get_data(URL, list_of_units)
# print(data)
