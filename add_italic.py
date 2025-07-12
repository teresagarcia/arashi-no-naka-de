import json
import re
from unidecode import unidecode


def limpiar_para_url(texto):
    # Quitar acentos y convertir a ASCII plano
    texto = unidecode(texto)
    # Convertir a minúsculas
    texto = texto.lower()
    # Reemplazar espacios y guiones por _
    texto = re.sub(r'[\s\-]+', '_', texto)
    # Eliminar cualquier carácter que no sea letra, número o _
    texto = re.sub(r'[^\w_]', '', texto)
    return texto

def final_transformation():
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

    final_result = '<br/>\n<br/>'.join(rebuilt) + '<br/>'
    print(final_result)

    lyricist = 'SQAREF, John World'
    composer = 'Pippi Svensson, Josef Melin'
    arranger = 'BJ Khan'
    album = 'Japonism (2015)'

    info_section = f"<span class='font-bold text-blue-secondary'>Info de la canción:</span><br/>Letra: {lyricist}.<br/>Música: {composer}.<br/>Arreglos: {arranger}.<br/>Álbum: {album}.<br/><br/><span class='font-bold text-blue-secondary'>Créditos:</span><br />Letra en japonés, romaji y traducción al inglés: <a href=\"http://yarukizero.livejournal.com/202210.html\" target=\"_blank\" class='text-blue-link'>Yarukizero</a>.<br/>Traducción al español publicada originalmente en <a href='https://yasashiiuta05.blogspot.com/{json_data[0]['blogger_link']}' target='_blank' class='text-blue-link'>Yasashii Uta</a>, mantenida y actualizada en <a href='https://arashinonakade.neocities.org/about.html' class='text-blue-link'>Arashi no naka de</a>."

    new_entry = {
        'artist': json_data[0]['artist'],
        'song': json_data[0]['song'],
        'intro': 'Una canción que comprendo mejor conforme pasan los años, cuando a pesar de los mil cambios en la vida sigue habiendo un par de lugares a los que puedo regresar.',
        'content': final_result,
        'info': info_section
    }

    entry_filename = limpiar_para_url( json_data[0]['song'])
    with open(f"site/japonism/{entry_filename}.json", "w", encoding="utf-8") as f:
        json.dump(new_entry, f, ensure_ascii=False, indent=2)

    
if __name__ == "__main__":
    final_transformation()



