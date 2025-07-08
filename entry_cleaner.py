import json
import re
with open("arashi_entries.json") as json_file:
    json_data = json.load(json_file)

texto = re.sub(r'\n(?=<)', '', json_data[0]['content'])
texto = re.sub(r'(?<=>)\n', '', texto)
texto_sin_saltos = texto.replace("\n", " ")

sin_comentarios = re.sub(r'<!--.*?-->', '', texto_sin_saltos, flags=re.DOTALL)
resultado = re.sub(r'<(?!/div\b)(?!a\b)(?!/a\b)[^>]+>', '', sin_comentarios)
resultado = resultado.replace('</div>', '<br/>')
resultado = re.sub(r'\s{2,}', ' ', resultado)
print(resultado)

