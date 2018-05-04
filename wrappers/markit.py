#!/usr/bin/env python3

import json

import requests


def lookup_ticker_symbol(company_name):
    endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input='
    response = requests.get(endpoint+company_name).text
    ticker_symbol = json.loads(response)[0]['Symbol']
    return ticker_symbol


def quote_last_price(ticker_symbol, submitted_key):
    endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol='
    response = requests.get(endpoint+ticker_symbol).text
    valid_keys = ['Open',               \
                    'ChangePercentYTD', \
                    'MarketCap',        \
                    'MSDate',           \
                    'Symbol',           \
                    'Volume',           \
                    'Change',           \
                    'Name',             \
                    'Status',           \
                    'High',             \
                    'LastPrice',        \
                    'ChangePercent',    \
                    'ChangeYTD',        \
                    'Low',              \
                    'Timestamp']
    # Let's introduce some control flow
    if submitted_key in valid_keys:
        value = json.loads(response)[submitted_key]
        return value
    else:
        return 'Error: you entered a bad key!'


if __name__ == '__main__':
    import os
    os.system('clear')
    print('*********************************\n')
    print('Welcome to My Trading Application\n\n')
    company_name = input('What company do you want market data for? ')
    submitted_key = input('What do you want to know about {0}? '.format(company_name))
    print(quote_last_price(lookup_ticker_symbol('Tesla'), submitted_key))
