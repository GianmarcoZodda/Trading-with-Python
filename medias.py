import pandas as pd

df = pd.read_csv("binance/ETHUSDT.csv")

# asegurar formato numérico
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

# usar últimos 360 precios, o lo que quieras. (siempre y cuando el csv sea mayor o igual a ese lapso)
last_prices = df["Close"].tail(360)

# esto se puede sacar, es uina validacion para que haya siempre cierta cantidad de datos
if len(last_prices) < 10:
    raise ValueError("No hay suficientes datos para analizar")

# saco la media y desviacion estandar, la necesito para sacar soportes y resistencias
mean_price = last_prices.mean()
std_price = last_prices.std()

# saco soportes, piso, y resistencia, techo
support_price = mean_price - std_price
resistance_price = mean_price + std_price

# agarro el ultimo precio
last_price = df["Close"].iloc[-1]

# comparar con soporte/resistencia
if last_price > resistance_price:
    status = "resistance"   #si el ultimo precio es mayor a la resistencia, es resistencia
    difference = last_price - resistance_price
elif last_price <= support_price:
    status = "support"   #si el ultimo precio es menor o igual al soporte, es soporte
    difference = support_price - last_price
else:
    status = "neutral"
    diff_to_res = resistance_price - last_price
    diff_to_sup = last_price - support_price
    difference = min(diff_to_res, diff_to_sup)

# salida
print(f"""
📊 Análisis ETH/USDT
Último precio: {last_price:.2f}
Media (360): {mean_price:.2f}
Desv. estándar: {std_price:.2f}
Soporte: {support_price:.2f}
Resistencia: {resistance_price:.2f}
Estado actual: {status.upper()} (Δ {difference:.2f})
""")

if status == "resistance":
    print("🚨 En resistencia → sugerencia: VENDER")
elif status == "support":
    print("🟢 En soporte → sugerencia: COMPRAR")
else:
    print("⚪ Neutral → mantener posición")
