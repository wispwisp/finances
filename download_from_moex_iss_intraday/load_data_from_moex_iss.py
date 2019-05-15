#!env python

import pandas as pd
import argparse
import os

import datetime
import urllib
import json

def get_shares_deals_today(security):
    url_pattern = "http://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{}/trades.json?start={}"

    result = []
    counter = 0
    while True:
        url = url_pattern.format(security, counter)
        http = urllib.request.urlopen(url)

        j = json.loads(http.read().decode('utf-8'))
        if 'trades' not in j.keys() and 'data' in j['trades'].keys():
            raise ValueError("Invalid responce JSON")

        # No data, exit cyce
        if len(j['trades']['data']) == 0:
            break

        # [0"TRADENO", 1"TRADETIME", 2"BOARDID", 3"SECID", 4"PRICE", 5"QUANTITY",
        # 6"VALUE", 7"PERIOD", 8"TRADETIME_GRP", 9"SYSTIME", 10"BUYSELL", 11"DECIMALS"],
        for trade in j['trades']['data']:
            ts = pd.Timestamp(trade[1])
            price = trade[4]
            volume = trade[5]
            operation = trade[10]
            desimals = trade[11]
            result.append((ts, price, volume, operation, desimals))

        counter += 5000

    return pd.DataFrame(result, columns=[
        'time', 'price', 'volume', 'operation', 'desimals'
    ]).set_index('time')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('security', type=str, help='security to load')
    args = parser.parse_args()

    security = args.security
    print('load', security)

    s = get_shares_deals_today(security)
    s.index = pd.DatetimeIndex(s.index)

    today = pd.Timestamp.now()

    path = "/market_data/" + str(today.year)
    if not os.path.isdir(path):
        os.makedirs(path)

    month = today.strftime('%m')
    path = path + "/" + month
    if not os.path.isdir(path):
        os.makedirs(path)

    day = today.strftime("%d")
    path = path + "/" + day + "_" + security + '.csv'
    s.to_csv(path)
