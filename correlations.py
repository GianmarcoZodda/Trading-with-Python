import pandas as pd
import numpy as np

#select csv
xrp_df = pd.read_csv("binance/XRPUSDT.csv").tail(30)    #con tail le defino el tiempo atrás, en este caso, 30 filas, que serian 30 dias, sin importar si hubo operacion o no, o sea sabado o domingo que en criptos no importa pero en etf/acciones si,, para que compare solo con eso
ada_df = pd.read_csv("binance/ADAUSDT.csv").tail(30)

#columns for study
xrp_prices = xrp_df[["Date","Close"]]
ada_prices = ada_df[["Date","Close"]]

#fusion in a dame dataframe
df = pd.merge(xrp_prices,ada_prices,on="Date",how="inner")

#correlation
correlation = np.corrcoef(df["Close_x"],df["Close_y"])[0,1]
print(correlation)

# asignar una puntuación basada en el nivel de correlación
if correlation > 0.8:
    score = 10
elif correlation > 0.78:
    score = 9
elif correlation > 0.4:
    score = 8
elif correlation > 0.2:
    score = 7
elif correlation > 0:
    score = 6
elif correlation > -0.2:
    score = 5
elif correlation > -0.4:
    score = 4
elif correlation > -0.6:
    score = 3
elif correlation > -0.8:
    score = 2
else:
    score = 1

# imprimir la puntuación
print(f"La puntuación de correlación entre xrp y ada es: {score}")