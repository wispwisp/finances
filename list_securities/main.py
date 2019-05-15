#!env python

import argparse
from symbols_scrapper import SP500Scrapper


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Work with securities data')
    parser.add_argument('-s', '--source', type=str, default='sp',
                        choices=['sp'],
                        dest='source', action='store', help='sp - S&P500')
    args = parser.parse_args()

    if args.source == "sp":
        s = SP500Scrapper()
        print(s.get_string())
    else:
        print("No args specified, see -h, --help")
