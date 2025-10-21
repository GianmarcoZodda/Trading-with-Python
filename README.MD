# 📊 Crypto Price Analysis & Prediction

Este proyecto analiza los precios de criptomonedas como **Bitcoin (BTC)** y **Ethereum (ETH)** utilizando **Python**, con el objetivo de detectar niveles de soporte y resistencia, además de hacer una predicción sobre el comportamiento del precio. Lo hice con el objetivo de practicar este lenguaje y algo de Machine Learning básico. Nota: también se puede hacer con el precio de otros activos cambiando el símbolo o la fuente, ejemplop, cambiar binance por otro exchange, o el símbolo "BTC" por "SYP500"

---

## 🚀 ¿Qué hace el proyecto?

El sistema:
1. Lee los datos históricos de precios de BTC y ETH desde archivos `.csv`.
2. Calcula promedios y desviaciones estándar para estimar **niveles de soporte y resistencia**.
3. Usa **regresión lineal** para intentar predecir si el precio del ETH va a subir o bajar en base al comportamiento del BTC.
4. Muestra los resultados por consola.
5. (Opcional) Permite graficar los precios usando **mplfinance**.

---

## 🧠 Librerías utilizadas

- `pandas` → para manejar datos
- `numpy` → para cálculos numéricos
- `sklearn` → para aplicar regresión lineal
- `mplfinance` → para graficar velas (candlesticks)

---

## ⚙️ Cómo ejecutarlo

1. Cloná el repositorio:

2. Instala las dependencias necesarias. Además de las mencionadas, hay otras como Beautifull soap para scraping, o la de yahoo finance para ver datos de la bolsa. Vos podés modificar el código a tu gusto y optar por otras librerías

3. Ejecutá primeros los archivos de extracción de datos, ya sea de la bolsa o binance, para generar los csv. Luego podés ir a los archivo de gráficos, tendencias y ML, pero primero necesitás tener los csv.

Nota: recorda instalar las dependencias necesarias y ejecutar primero los archivos que generan los csv a utilizar. Desde "extracciones.py" saco los datos de binance (reemplaza por tus keys), y desde "databolsa.py", la info de la bolsa desde yahoo finance. En "redditdata.py", podemos ver el top de criptos que más se habla. En "medias.py", veremos el sopórte y resistencia para saber en que momento deberiamos comprar, (con el básico de análisis técnico se puede saber que no se compra en el techo, se compra en el piso de las bandas). Luego, está el archivo "graficos.py", se puede ver el gráfico del símbolo que le pases, (según el csv  que hayas generado anteriormente, ya quee trabaja con ese archivo).  En "correlations.py", podes ver la correlacion entre 2 activos (también necesitas haber generado los csv de ambos en los ejecutables anteriores) y, por último, está el archivo de "entrenamiento", donde usando la regresión lineal predecimos el precio de un activo considerando otro. Importante: en mi caso use a Bitcoin para predecir Etherium, ya que en la mayoría de los casos, los movimientos (alcistas o bajistas) originados en BTC terminan impactando en ETH y todas las criptos, por lo que me pareció lógico hacer esa comparación.

Espero que lo pruebes y me digas si te sirvió. A mí me sorprendió que en varias oportunidades acertó si el precio iba a subir o bajar. Quién sabe, tal veces siga mejorando este proyecto y termine invirtiendo por mí
