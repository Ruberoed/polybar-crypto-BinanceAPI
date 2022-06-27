import os
from binance.client import Client
import const

client = Client(const.Api, const.Secret)

balance = client.futures_coin_account_balance()[0]['balance']
z = len(balance)
s = str(balance)
bal = s[:z - 3]
print(bal,'$')
