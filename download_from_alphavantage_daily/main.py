#!env python

import os
import time

import symbols
from securities_info import get_today_security_info

if __name__ == '__main__':
    for symbol in symbols.symbols:
        print("Loading", symbol, "...")

        # create file if not exists
        path = "/market_data/" + symbol + ".csv"
        if not os.path.isfile(path):
            with open(path, "a") as myfile:
                myfile.write("date;open;high;low;close;volume\n")

        # write current data to file
        with open(path, "a") as myfile:
            myfile.write(';'.join(map(str, get_today_security_info(symbol))) + "\n")

        # "up to 5 API requests per minute and 500 requests per day"
        time.sleep(60) # Delay for 1 minute (60 seconds).
