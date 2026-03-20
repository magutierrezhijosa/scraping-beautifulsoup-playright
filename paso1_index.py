
# paso1_index.py
import requests
from bs4 import BeautifulSoup

# Importamos las CONSTANTES
from config import URL_TO_SCRAP,BASE_URL

# Paso 1 : Descargar la pagina
# request.get() hace una peticion HTTP GET - como cuando tu navegador carga la pagina
respuesta = requests.get(URL_TO_SCRAP)

# Verificamos que fue bien (codigo 200 = OK)
print(f"Codigo de respuesta:{respuesta.status_code}")

# Paso 2: Parsear el HTML con BeautifulSoup
