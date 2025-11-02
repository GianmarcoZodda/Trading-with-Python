import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# me traigo las ultimas 30 de cada archivos
btc_data = pd.read_csv("BTCUSDT.csv").tail(30)
eth_data = pd.read_csv("ETHUSDT.csv").tail(30)

# elimino nulos (inplace=true) significa que es sobre el mismo df, no sobre alguna copia
btc_data.dropna(inplace=True)
eth_data.dropna(inplace=True)

# me agarro el precio cierre del anteúltimo dia, no el ultimo
btc_data['Close'] = btc_data['Close'].shift(1)

# usando date como pk e inner para tomar solo las fechasque estan en ambos df, los uno
merged_data = pd.merge(btc_data[['Date', 'Close']], eth_data[['Date', 'Close']], on='Date', how='inner')

# divido en datos de test y de entrenamiento
train_data = merged_data.iloc[:-1, :]
test_data = merged_data.iloc[-1:, :]

# reemplazo valores vacios con el promedio,  
imputer = SimpleImputer(strategy='mean')
train_predictors = imputer.fit_transform(train_data.iloc[:, 1].values.reshape(-1, 1))
test_predictors = imputer.transform(test_data.iloc[:, 1].values.reshape(-1, 1))

# uso regresion lineal
regression = LinearRegression()
regression.fit(train_predictors, train_data.iloc[:, 2].values.reshape(-1, 1))

# hago la prediccion"
predicted_price = regression.predict(test_predictors)

# depende si sube o baja
if predicted_price > test_data.iloc[0, 2]:
    print("The price of ETHUSDT is predicted to go up.")
else:
    print("The price of ETHUSDT is predicted to go down.")