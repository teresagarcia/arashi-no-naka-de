import json    
import re
from unidecode import unidecode
from pathlib import Path

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
   
def final_transformation(song_info):   
    with open("data/preformat_entry.json") as json_file:
        json_data = json.load(json_file)
    
    credits_section = f"<span class='font-bold text-blue-secondary'>Créditos:</span><br />{song_info['translations_info']}.<br/>Traducción al español publicada originalmente en <a href='https://yasashiiuta05.blogspot.com{json_data['blogger_link']}' target='_blank' class='text-blue-link'>Yasashii Uta</a>, mantenida y actualizada en <a href='https://arashinonakade.neocities.org/about.html' class='text-blue-link'>Arashi no naka de</a>."

    new_entry = {
        'artist': json_data['artist'],
        'song': json_data['song'],
        'intro': song_info['intro'],
        'content': json_data['lyrics'],
        'lyricist': song_info['lyricist'],
        'composer': song_info['composer'],
        'arranger': song_info['arranger'],
        'album': song_info['album'],
        'credits': credits_section
    }

    entry_filename = limpiar_para_url(json_data['song'])
    route = Path(f"../site/arashi/{song_info['album_folder']}/{entry_filename}.json")
    route.parent.mkdir(parents=True, exist_ok=True)
    
    with route.open("w", encoding="utf-8") as f:
        json.dump(new_entry, f, ensure_ascii=False, indent=2)
        
if __name__ == "__main__":
    song_info = { 'lyricist' : 'HIKARI',
        'composer': 'Tomoki Ishizuka',
        'arranger': 'Tomoki Ishizuka',
        'album': 'Five (2026)',
        'album_folder': "five",
        'intro': 'Canción adorable como ellos.',
        'translations_info':" Letra en japonés y romaji: <a href=\"https://www.azlyrics.com/lyrics/arashi/five.html\" target=\"_blank\">AZLyrics</a>"
        }
    final_transformation(song_info)