import time
import random
from paper_engine import *

def simulate_trade():
    global position

    price = 100

    if position is None:
        buy(price, step2=False)
        print("Entered trade")

    for _ in range(10):
        if position is None:
            break

        current_price = price * (1 + random.uniform(-0.02, 0.03))
        change = (current_price - position["entry"]) / position["entry"]

        if should_force_loss():
            print("Forced Loss")
            sell(position["entry"] * 0.7)
            break

        if change >= 0.30:
            sell(current_price)
            print("Target hit")
            break

        elif change <= -0.25 and not position["step2"]:
            print("Step2 entry")
            buy(current_price, step2=True)

        elif change <= -0.25:
            sell(current_price)
            print("Stop loss")
            break

    print("Capital:", capital)


while True:
    try:
        simulate_trade()
        time.sleep(10)
    except Exception as e:
        print("Error:", e)
        time.sleep(5)
