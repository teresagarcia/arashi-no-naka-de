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
   
def final_transformation():   
    with open("data/preformat_entry.json") as json_file:
        json_data = json.load(json_file)
    lyricist = '100+'
    composer = '100+'
    arranger = 'Hirofumi Sasaki'
    album = 'Meikyuu Love Song (2011)'
    album_folder = "meikyuu_love_song"
    translations_info = "Letra en japonés: <a href=\"http://www.littleoslo.com/lyj/home/2011/10/%E5%B5%90-together-forever/\" target=\"_blank\">Oo Kashi</a>.<br/>\nRomaji y traducción al inglés: <a href=\"http://www.jpopasia.com/group/arashi/lyrics/meikyu-love-song/together-forever::71798.html\" target=\"_blank\">JpopAsia</a><br/>"
    
    credits_section = f"<span class='font-bold text-blue-secondary'>Créditos:</span><br />{translations_info}.<br/>Traducción al español publicada originalmente en <a href='https://yasashiiuta05.blogspot.com{json_data['blogger_link']}' target='_blank' class='text-blue-link'>Yasashii Uta</a>, mantenida y actualizada en <a href='https://arashinonakade.neocities.org/about.html' class='text-blue-link'>Arashi no naka de</a>."

    new_entry = {
        'artist': json_data['artist'],
        'song': json_data['song'],
        'intro': 'Tierna canción dentro del single <i>Meikyuu Love Song</i> &#10084;',
        'content': json_data['lyrics'],
        'lyricist': lyricist,
        'composer': composer,
        'arranger': arranger,
        'album': album,
        'credits': credits_section
    }

    entry_filename = limpiar_para_url(json_data['song'])
    route = Path(f"../site/arashi/{album_folder}/{entry_filename}.json")
    route.parent.mkdir(parents=True, exist_ok=True)
    
    with route.open("w", encoding="utf-8") as f:
        json.dump(new_entry, f, ensure_ascii=False, indent=2)
        
if __name__ == "__main__":
    final_transformation()