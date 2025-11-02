# --- Librerías necesarias ---
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

# --- Configuración inicial ---
URL = "https://apewisdom.io/all-crypto/"
today = datetime.today().strftime("%Y-%m-%d")  # Fecha actual
print(f"📅 Fecha actual: {today}")

# --- Crear carpeta donde se guardarán los archivos ---
os.makedirs("reddit", exist_ok=True)  # Si no existe, la crea

# --- Función para obtener el HTML de la página ---
def get_page_html(url):
    try:
        # Hago la solicitud a la página (máx. 10 segundos)
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Si hay error (404, etc.), lanza excepción
        return BeautifulSoup(response.text, "html.parser")  # Parseo el HTML
    except Exception as e:
        print(f"❌ Error al obtener la página: {e}")
        return None


def obtenerCriptos(soup, cantidad):
    # Busco los divs con clase "company-name" (donde están los nombres)
    names = [div.text.strip() for div in soup.find_all("div", class_="company-name")]
    
    if not names:
        print("⚠️ No se encontraron criptomonedas.")
        return []
    
    print(f"🔹 Criptos encontradas: {names[:cantidad]}")
    return names[:cantidad]  # Devuelvo solo las primeras N


def obtenerPorcentajes(soup, cantidad):
    tds = soup.find_all("td", class_="td-center rh-sm")
    porcentajes = []

    for td in tds:
        text = td.get_text(strip=True)
        if "%" in text:
            porcentajes.append(text)
    
    if not porcentajes:
        print("⚠️ No se encontraron porcentajes.")
        return []
    
    print(f"📈 Porcentajes encontrados: {porcentajes[:cantidad]}")
    return porcentajes[:cantidad]


# --- Ejecuto el scraping ---
soup = get_page_html(URL)

if soup:
    cryptos = obtenerCriptos(soup, 3)
    percents = obtenerPorcentajes(soup, 3)

    # Me aseguro de que haya al menos 3 criptos y 3 porcentajes
    if len(cryptos) >= 3 and len(percents) >= 3:
        
        # --- Armo un diccionario con los datos extraídos ---
        data = {
            "Date": [today],
            "Ranking1": [cryptos[0]],
            "Ranking2": [cryptos[1]],
            "Ranking3": [cryptos[2]],
            "Ranking1_Percent": [percents[0]],
            "Ranking2_Percent": [percents[1]],
            "Ranking3_Percent": [percents[2]],
        }

        # --- Convierto el diccionario en DataFrame ---
        df = pd.DataFrame(data)

        # --- Defino la ruta del archivo dentro de la carpeta data/reddit ---
        file_path = os.path.join("reddit", "RedditData.csv")

        # --- Guardo el CSV ---
        # 'mode="a"' → agrega nuevas filas sin borrar lo anterior
        # 'header=not os.path.exists(file_path)' → agrega encabezado solo si el archivo no existe
        df.to_csv(file_path, mode="a", index=False, header=not os.path.exists(file_path))
        
        print(f"✅ Datos guardados correctamente en {file_path}")
    
    else:
        print("⚠️ No hay suficientes datos para guardar.")

else:
    print("❌ No se pudo obtener la página.")