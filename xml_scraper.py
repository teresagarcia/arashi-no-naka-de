from pathlib import Path
from bs4 import BeautifulSoup
import json

xml_path = Path("feed.atom")  # Cambia la ruta
with xml_path.open(encoding="utf-8") as f:
    xml_string = f.read()

soup = BeautifulSoup(xml_string, "xml")

entries = []
for entry in soup.find_all("entry"):
    title_tag = entry.find("title")
    if title_tag and "Arashi" in title_tag.get_text() and "Letras y traducciones" not in title_tag.get_text() :
        contenido = entry.find("content")
        filename = entry.find("blogger:filename")
        
        entries.append({
            "title": title_tag.get_text(strip=True),
            "content": contenido.get_text() if contenido else "",
            "link": filename.get_text() if filename else ""
        })

with open("arashi_entries.json", "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

for entry in entries:
    print(entry['title'])
print("total:", entries.__len__())
