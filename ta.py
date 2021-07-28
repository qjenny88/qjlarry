import ccxt
import yfinance
import pandas_ta as ta
import panda as pd

exchange = ccxt.binance()

bars = exchange.fetch_ohlcv('')import ccxt, yfinance
import pandas_ta as ta
import panda as pd

exchange = ccxt.binance()

bars = exchange.fetch_ohlcv('VET/USDT', timeframe='5m', limit=500)

print(bars)
