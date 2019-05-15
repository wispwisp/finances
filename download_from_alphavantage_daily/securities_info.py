import pandas as pd

import datetime
import urllib
import json

import apikey


def apply_request(req_str: str):
    """ Request to API. Returns json
    """
    assert isinstance(req_str, str)

    http = urllib.request.urlopen(req_str)
    return json.loads(http.read().decode('utf-8'))


def daily_prices_pattern(symbol, apikey=apikey.apikey):
    """ String request pattern, formatted by symbol and apikey
    - Data for security by its symbol (OHLC and volume)
    """
    return "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}".format(
        symbol, apikey
    )


def get_today_security_info(symbol: str):
    assert isinstance(symbol, str)

    j = apply_request(daily_prices_pattern(symbol))

    date = datetime.datetime.strptime(j['Global Quote']['07. latest trading day']
                                      , "%Y-%m-%d").date()

    open_ = float(j['Global Quote']['02. open'])
    high  = float(j['Global Quote']['03. high'])
    low   = float(j['Global Quote']['04. low'])
    close = float(j['Global Quote']['05. price'])

    volume = int(j['Global Quote']['06. volume'])

    return (date, open_, high, low, close, volume)
