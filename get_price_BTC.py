import os
from binance.client import Client
import const

client = Client(const.Api, const.Secret)

btc_price = client.get_symbol_ticker(symbol='BTCUSDT')['price']
size = len(btc_price)
bt = str(btc_price)
btc = btc_price[:size -6]
print(btc,'$')

