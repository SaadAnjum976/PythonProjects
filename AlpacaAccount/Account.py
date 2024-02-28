import alpaca_trade_api as tradeapi
from alpaca_trade_api import REST
import config

api = tradeapi.REST(config.ALPACA_API_KEY, config.ALPACA_API_SECRET, config.ALPACA_API_BASE_URL)

class Account:
    def __init__(self) -> None:
        self.account_number = ''
        self.cash = ''
        self.equity = ''
        self.regt_buying_power = ''

acc = Account()
print(acc.account_number)

def accDetails():
    a = api.get_account()

    acc.account_number = getattr(a, 'account_number')
    acc.cash = getattr(a, 'cash')
    acc.equity = getattr(a, 'equity')
    acc.regt_buying_power = getattr(a, 'regt_buying_power')

accDetails()

print(acc.account_number)