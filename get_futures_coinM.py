import os
from binance.client import Client
import const

client = Client(const.Api, const.Secret)
# get coin-M futures account balance
coinm_balance = client.futures_coin_account_balance()[0]['balance']
z = len(coinm_balance)
s = str(coinm_balance)
bal = s[:z - 3]
print(bal,'$')
