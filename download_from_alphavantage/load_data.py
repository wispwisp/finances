#!env python

import requests
import time

import symbols
import apikey

pattern = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey={}&datatype=csv"

if __name__ == '__main__':
    for symbol in symbols.symbols:
        print("Loading", symbol, "...")

        url= pattern.format(symbol, apikey.apikey)
        response = requests.get(url)

        path = "/market_data/" + symbol + ".csv"
        with open(path, 'wb') as f:
            f.write(response.content)

        # "up to 5 API requests per minute and 500 requests per day"
        time.sleep(60) # Delay for 1 minute (60 seconds).
