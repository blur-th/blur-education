
# Copyright (c) 2026 Blur (www.blur-th.com)
# Licensed under the MIT License.

import time
import random
from datetime import datetime

def fetch_mock_data(symbol="BTC/USDT", limit=5):
    """
    Simulate fetching data from an exchange API.
    """
    print(f"Fetching {limit} candles for {symbol}...")
    
    data = []
    base_price = 45000
    
    for i in range(limit):
        timestamp = int(time.time() * 1000) - (i * 60000) # 1 minute intervals
        open_p = base_price + random.uniform(-50, 50)
        high = open_p + random.uniform(0, 50)
        low = open_p - random.uniform(0, 50)
        close = random.uniform(low, high)
        volume = random.uniform(0.1, 2.0)
        
        data.append({
            "timestamp": datetime.fromtimestamp(timestamp / 1000),
            "open": open_p,
            "high": high,
            "low": low,
            "close": close,
            "volume": volume
        })
        
    return data

def main():
    data = fetch_mock_data()
    for candle in data:
        print(candle)

if __name__ == "__main__":
    main()
