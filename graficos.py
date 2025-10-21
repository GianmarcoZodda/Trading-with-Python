import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# --- cargar datos, modificar por el archivo que quieras ---
df = pd.read_csv("binance/ETHUSDT.csv")

# asegurar formato correcto
df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
df["Open"] = pd.to_numeric(df["Open"], errors="coerce")
df["High"] = pd.to_numeric(df["High"], errors="coerce")
df["Low"] = pd.to_numeric(df["Low"], errors="coerce")

# establecer índice de tiempo
df.set_index("Date", inplace=True)

# usar últimos 180 registros (ajustable)
df = df.tail(180)

# --- cálculos de niveles ---
mean_price = df["Close"].mean()
std_price = df["Close"].std()
support_price = mean_price - std_price
resistance_price = mean_price + std_price
last_price = df["Close"].iloc[-1]

# --- definir líneas horizontales ---
hlines = dict(
    hlines=[support_price, mean_price, resistance_price, last_price],
    colors=["green", "blue", "red", "orange"],
    linestyle=["--", ":", "--", "-."],
    linewidths=[1.5, 1, 1.5, 1],
    alpha=0.8
)

# --- configurar estilo del gráfico ---
style = mpf.make_mpf_style(base_mpf_style='charles', rc={'font.size': 8})

# --- graficar ---
mpf.plot(
    df,
    type='candle',          # gráfico de velas
    style=style,
    title=f"ETH/USDT - {len(df)} últimas velas",
    ylabel="Precio (USDT)",
    volume=True,
    hlines=hlines,
    figratio=(16,9),
    figscale=1.2
)

plt.show()
