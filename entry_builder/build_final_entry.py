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
    lyricist = 'Tatsurō Mashiko'
    composer = 'Tatsurō Mashiko'
    arranger = 'Tatsurō Mashiko'
    album = 'Boku no Miteiru Fuukei (2010)'
    album_folder = "boku_no_miteiru_fuukei"
    translations_info = "Letra en japonés, romaji y traducción al inglés: <a href=\"http://yarukizero.livejournal.com/20098.html\" target=\"_blank\" class='text-blue-link'>Yarukizero</a>"
    
    info_section = f"<span class='font-bold text-blue-secondary'>Info de la canción:</span><br/>Letra: {lyricist}.<br/>Música: {composer}.<br/>Arreglos: {arranger}.<br/>Álbum: {album}.<br/><br/><span class='font-bold text-blue-secondary'>Créditos:</span><br />{translations_info}.<br/>Traducción al español publicada originalmente en <a href='https://yasashiiuta05.blogspot.com{json_data['blogger_link']}' target='_blank' class='text-blue-link'>Yasashii Uta</a>, mantenida y actualizada en <a href='https://arashinonakade.neocities.org/about.html' class='text-blue-link'>Arashi no naka de</a>."

    new_entry = {
        'artist': json_data['artist'],
        'song': json_data['song'],
        'intro': '<i>Boku no Miteiru Fuukei</i> nos dio muchísimas joyas, entre ellas esta. Siempre me llena de melancolía y nostalgia pero también de la fuerza serena que estos chicos siempre saben transmitir.',
        'content': json_data['lyrics'],
        'info': info_section
    }

    entry_filename = limpiar_para_url(json_data['song'])
    route = Path(f"../site/arashi/{album_folder}/{entry_filename}.json")
    route.parent.mkdir(parents=True, exist_ok=True)
    
    with route.open("w", encoding="utf-8") as f:
        json.dump(new_entry, f, ensure_ascii=False, indent=2)
        
if __name__ == "__main__":
    final_transformation()