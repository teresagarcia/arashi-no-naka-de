import json
import re
with open("arashi_entries.json") as json_file:
    json_data = json.load(json_file)

texto_sin_saltos = json_data[0]['content'].replace("\n", "")
print(texto_sin_saltos)

print(json_data[0]['title'])
print(texto_sin_saltos)
sin_comentarios = re.sub(r'<!--.*?-->', '', texto_sin_saltos, flags=re.DOTALL)
resultado = re.sub(r'<(?!/div\b)[^>]+>', '', sin_comentarios)
resultado = resultado.replace('</div>', '<br/>')
print(resultado)

