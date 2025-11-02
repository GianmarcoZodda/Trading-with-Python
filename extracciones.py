from datetime import date, timedelta
import time
import os
import pandas as pd
from binance import Client

from dotenv import load_dotenv
load_dotenv()  


api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

if not api_key or not api_secret:
    raise ValueError("Faltan las claves")

client = Client(api_key, api_secret)

today = date.today()
yesterday = today - timedelta(days=1)

# recibe un simbolo, como BTC, o el que quiera
def criptodata(symbol):
    try:
        # Info de precio actual
        price = client.get_symbol_ticker(symbol=symbol)
        print(f"\n💰 Precio actual {symbol}: {price['price']}")
        
        # le defino una fecha de inicio, fin y el lapso de tiempo para agarrar la info, que es de 1 dia
        start = "2023-01-01"
        end = str(yesterday)
        timeframe = "1d"
        
        # Obtener datos históricos
        klines = client.get_historical_klines(symbol, timeframe, start, end)
        
        # esto en caso de que no me logre traer nada
        if not klines:
            print(f"⚠️ No hay datos para {symbol}")
            return
        
        # de lo que me trae, agarro las 6 primeras columnas, que son las que me interesan
        df = pd.DataFrame(klines).iloc[:, :6]
        # las renombro
        df.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
        # parseo
        df["Date"] = pd.to_datetime(df["Date"], unit="ms")
        #pongo la fecha como indice
        df = df.set_index("Date")
        df = df.astype(float)
        
        # Crear carpeta si no existe, para guardar la info que me traigo
        os.makedirs("binance", exist_ok=True)
        
        # Guardar CSV
        output_path = os.path.join("binance", f"{symbol}.csv")
        df.to_csv(output_path, encoding="utf-8")
        
        print(f"✅ {symbol} descargado y guardado en {output_path}")
        
    except Exception as e:
        print(f"❌ Error con {symbol}: {e}")

# --- LISTA DE CRIPTOS ---
symbols = ["BTCUSDT", "ETHUSDT", "ADAUSDT", "XRPUSDT"]

for s in symbols:
    criptodata(s)
    time.sleep(0.3)  # pequeña pausa entre llamadas

print("\n🚀 Descarga completa.")