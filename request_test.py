import requests
from bs4 import BeautifulSoup

respuesta = requests.get("https://www.larazondechivilcoy.com.ar/")
respuesta.encoding = "utf-8"
soup = BeautifulSoup(respuesta.text, "html.parser")

for h in soup.find_all(["h2"])[:10]:
    print(h.get_text().strip())