import json

with open("clean_entries.json") as json_file:
    json_data = json.load(json_file)

lyrics = json_data[0]['lyrics']

blocks = lyrics.split('<br/>\n<br/>')

rebuilt = []
for i,block  in enumerate(blocks):
    multiline = block.splitlines().__len__() > 1
    if multiline :
        split_block = block.splitlines()
        phrase, sep, _ = split_block[-2].partition('<br/>')
        split_block[-2] = f"<i>{phrase}</i>{sep}"
        blocks_joined = ''.join(split_block)
        rebuilt.append(blocks_joined)

final_result = '<br/>\n<br/>'.join(rebuilt) + '<br/>\n<br/>'
print(final_result)

lyricist = ''
composer = ''
arranger = ''
album = ''

info_section = f"<span class='font-bold text-blue-secondary'>Info de la canción:</span><br/>Letra: {lyricist}.<br/>Música: {composer}.<br/>Arreglos: {arranger}.<br/>Álbum: {album}, 5x20 All the Best!! 1999–2019 (2019).<br/><br/><span class='font-bold text-blue-secondary'>Créditos:</span><br />Letra en japonés: <a href='http://www.kasi-time.com/item-35945.html' target='_blank' class='text-blue-link'>Kasi Time</a>.<br />Romaji y traducción al inglés: <a href='http://taijiproject.livejournal.com/69480.html' target='_blank' class='text-blue-link'>Taiji Project</a>.<br />Traducción al español publicada originalmente en <a href='https://yasashiiuta05.blogspot.com/{json_data[0]['blogger_link']}' target='_blank' class='text-blue-link'>Yasashii Uta</a>, mantenida y actualizada en <a href='https://arashinonakade.neocities.org/about.html' class='text-blue-link'>Arashi no naka de</a>."

new_entry = {
    'artist': json_data[0]['artist'],
    'song': json_data[0]['song'],
    'intro': 'lo que se me ocurra',
    'content': final_result,
    'info': info_section
}

with open("archivo.json", "w", encoding="utf-8") as f:
    json.dump(new_entry, f, indent=4)
