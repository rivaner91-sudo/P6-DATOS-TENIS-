import requests
from bs4 import BeautifulSoup
import pandas as pd
# Guardar el script completo en un archivo .py local
script_code = """import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.taf.com.mx/asics"
response = requests.get(url)
response.encoding = 'utf-8'

texto = BeautifulSoup(response.text, "html.parser")
texto
tenis = texto.find_all("article", class_='vtex-product-summary-2-x-element')
tenis

for articulo in tenis:
  nombre = articulo.find("div", class_="vtex-flex-layout-0-x-flexRow--ProductItemName").text
  precio_prev = articulo.find("div", class_="vtex-flex-layout-0-x-flexRow--ProductItem-Price").text
  precio = float(precio_prev.replace("$", "").replace(",", ""))
  genero = articulo.find("div", class_="vtex-flex-layout-0-x-flexRow--ProductBrand").text

    datos.append({
        "nombre": nombre,
        "precio": precio,
        "genero": genero
    })

df = pd.DataFrame(datos)
df

print("Scraping exitoso y archivo catalogo_libros.csv creado.")
"""

with open("scraper.py", "w", encoding="utf-8") as f:
    f.write(script_code)
