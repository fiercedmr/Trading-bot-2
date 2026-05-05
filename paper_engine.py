import datetime
import random

capital = 100000
position = None
trade_log = []
trade_counter = 0

SLIPPAGE = 0.002
BROKERAGE = 20
DECAY_PER_MIN = 0.001
RISK_PER_TRADE = 0.12
STEP2_MULTIPLIER = 1.2

def apply_slippage(price, side="buy"):
    return price * (1.002 if side == "buy" else 0.998)

def apply_market_noise(price):
    return price * (1 + random.uniform(-0.003, 0.003))

def get_qty(price, multiplier=1):
    return int((capital * RISK_PER_TRADE * multiplier) / price)

def buy(price, step2=False):
    global position
    price = apply_market_noise(price)
    price = apply_slippage(price, "buy")

    qty = get_qty(price, STEP2_MULTIPLIER if step2 else 1)

    position = {
        "entry": price,
        "qty": qty,
        "time": datetime.datetime.now(),
        "step2": step2
    }

def sell(price):
    global capital, position

    price = apply_market_noise(price)
    price = apply_slippage(price, "sell")

    hold_min = (datetime.datetime.now() - position["time"]).seconds / 60
    decay = price * DECAY_PER_MIN * hold_min
    price -= decay

    pnl = (price - position["entry"]) * position["qty"] - BROKERAGE
    capital += pnl

    trade_log.append(capital)

    position = None

def should_force_loss():
    global trade_counter
    trade_counter += 1
    return trade_counter % 5 == 0
