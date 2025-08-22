import os
import shutil
from datetime import datetime
import re

SRC_DIR = "site"
DIST_DIR = "dist"
VERSION = datetime.now().strftime("%Y%m%d%H%M")

# limpiar dist si existe
if os.path.exists(DIST_DIR):
    shutil.rmtree(DIST_DIR)
shutil.copytree(SRC_DIR, DIST_DIR)

# extensiones a renombrar
EXTENSIONS_TO_RENAME = (".js", ".css", ".json")

# mapping de nombres originales -> nuevos nombres
renamed_files = {}
# new_index_name = None

# 1️⃣ Renombrar archivos
for root, _, files in os.walk(DIST_DIR):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in EXTENSIONS_TO_RENAME:
            old_path = os.path.join(root, file)
            name, ext = os.path.splitext(file)
            new_file = f"{name}-{VERSION}{ext}"
            new_path = os.path.join(root, new_file)
            os.rename(old_path, new_path)
            renamed_files[file] = new_file
            # if file.lower() == "index.html":
            #     new_index_name = new_file

# 2️⃣ Actualizar referencias exactas en HTML, CSS, JS y JSON
FILES_TO_UPDATE = (".html", ".css", ".js", ".json")

for root, _, files in os.walk(DIST_DIR):
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in FILES_TO_UPDATE:
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            # reemplazo exacto por nombre de archivo
            for old_name, new_name in renamed_files.items():
                content = re.sub(rf'\b{re.escape(old_name)}\b', new_name, content)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

lyrics_path = os.path.join(DIST_DIR, f"scripts/lyrics-{VERSION}.js")

with open(lyrics_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Línea que queremos modificar (la 10 → índice 9)
line_index = 4
old_line = lines[line_index]

# Buscar ".json" y añadir el sufijo antes
lines[line_index] = re.sub(r'(\.json)', f'-{VERSION}\\1', old_line)

# Guardar de nuevo
with open(lyrics_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"✅ Línea {line_index+1} de lyrics.js actualizada con el sufijo")

# # 3️⃣ Crear nuevo index.html que redirija al index versionado
# if new_index_name:
#     index_path = os.path.join(DIST_DIR, "index.html")
#     with open(index_path, "w", encoding="utf-8") as f:
#         f.write(f"""<!DOCTYPE html>
# <html lang="es">
# <head>
# <meta charset="UTF-8">
# <meta http-equiv="refresh" content="0; url={new_index_name}">
# <title>Arashi no naka de</title>
# </head>
# <body>
# Redirigiendo a la versión más reciente...
# </body>
# </html>""")

print("✅ Build completo en", DIST_DIR)
# print(f"✅ Index principal redirige a {new_index_name}")
