import pandas as pd #yfinance me trae un dataframe, por eso traigo pandas 
import yfinance as yf
import os

os.makedirs("bolsa", exist_ok=True)

def getSymbolInfo(symbol, period):
    try:
        df = yf.Ticker(symbol).history(period=period)  # me trae un dataframe
        if not df.empty:
           file_path = os.path.join("bolsa", f"{symbol}.csv")
           df.to_csv(file_path, index=True)
        else:
            print("❌ Error obteniendo el ticker")
    except Exception as e:
        print(f"❌ Error con {symbol}: {e}")     


symbols = ["BTC-USD", "SPY", "GC=F"]

for s in symbols:
    getSymbolInfo(s, "1y")



