import json

with open("clean_entries.json") as json_file:
    json_data = json.load(json_file)

lyrics = json_data[0]['lyrics']

print("lyrics sin arreglar\n", lyrics)

cachitos = lyrics.split('<br/>\n<br/>')

for i,cachito  in enumerate(cachitos):
    print(i,cachito)
    print("varias líneas", cachito.splitlines().__len__() > 1)