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

def accDetails():
    a = api.get_account()

    acc.account_number = getattr(a, 'account_number')
    acc.cash = getattr(a, 'cash')
    acc.equity = getattr(a, 'equity')
    acc.regt_buying_power = getattr(a, 'regt_buying_power')

def place_order(symbol, quantity, side, order_type='market', time_in_force='gtc'):
    order = api.submit_order(
        symbol=symbol,
        qty=quantity,
        side=side,
        type=order_type,
        time_in_force=time_in_force
    )
    return order

accDetails()

print(acc.account_number)

# Example: Place a market buy order for 1 share of AAPL
symbol_to_trade = "AAPL"
quantity_to_trade = 1
order_side = "buy"
placed_order = place_order(symbol_to_trade, quantity_to_trade, order_side)

print("Order Placed:", placed_order)