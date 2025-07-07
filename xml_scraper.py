from pathlib import Path
from bs4 import BeautifulSoup
import json

# 1. Carga el XML desde disco
xml_path = Path("feed.atom")  # Cambia la ruta
with xml_path.open(encoding="utf-8") as f:
    xml_string = f.read()

# 2. Crea el árbol BeautifulSoup
#    Usa "xml" (o "lxml-xml" si tienes lxml instalado) para un parser que
#    respete la sintaxis XML.
soup = BeautifulSoup(xml_string, "xml")

entries = []
for entry in soup.find_all("entry"):
    title_tag = entry.find("title")
    if title_tag and "Arashi" in title_tag.get_text():
        contenido = entry.find("content")
        filename = entry.find("blogger:filename")
        
        entries.append({
            "title": title_tag.get_text(strip=True),
            "content": contenido.get_text() if contenido else "",
            "link": filename.get_text() if filename else ""
        })

# 3. Guardamos en un archivo JSON
with open("arashi_entries.json", "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)


