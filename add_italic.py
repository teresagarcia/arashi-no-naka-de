import json

with open("clean_entries.json") as json_file:
    json_data = json.load(json_file)

lyrics = json_data[0]['lyrics']

cachitos = lyrics.split('<br/>\n<br/>')

new_cachitos = []
for i,cachito  in enumerate(cachitos):
    multiline = cachito.splitlines().__len__() > 1
    if multiline :
        cachitos_a_cachitos = cachito.splitlines()
        parte1, sep, _ = cachitos_a_cachitos[-2].partition('<br/>')
        cachitos_a_cachitos[-2] = f"<i>{parte1}</i>{sep}"
        cachitos_joined = ''.join(cachitos_a_cachitos)
        new_cachitos.append(cachitos_joined)

final_result = '<br/>\n<br/>'.join(new_cachitos) + '<br/>\n<br/>'
print(final_result)
