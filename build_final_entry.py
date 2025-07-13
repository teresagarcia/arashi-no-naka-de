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
    with open("preformat_entry.json") as json_file:
        json_data = json.load(json_file)
    lyricist = 'Paddy'
    composer = 'Peter Nord, Kevin Borg'
    arranger = 'Peter Nord, Hirofumi Sasaki'
    album = 'Tsunagu (2017), untitled (2017), 5x20 All the best!! 1999-2019 (2019)'
    album_folder = "untitled"
    translations_info = "Letra en japonés y traducción al coreano: <a href=\"http://blog.naver.com/PostView.nhn?blogId=jample&amp;logNo=221039771636\" target=\"_blank\" class='text-blue-link'>Jample</a>.<br/>\nRomaji: Yasashii Uta a partir de Jample.<br/>\nTraducción al inglés (versión corta):  <a href=\"https://onelovearashi.tumblr.com/post/162167432960/tsunagu-music-station-ver-translations\" target=\"_blank\" class='text-blue-link'>One love Arashi (Tumblr)</a>"
    
    info_section = f"<span class='font-bold text-blue-secondary'>Info de la canción:</span><br/>Letra: {lyricist}.<br/>Música: {composer}.<br/>Arreglos: {arranger}.<br/>Álbum: {album}.<br/><br/><span class='font-bold text-blue-secondary'>Créditos:</span><br />{translations_info}.<br/>Traducción al español publicada originalmente en <a href='https://yasashiiuta05.blogspot.com{json_data['blogger_link']}' target='_blank' class='text-blue-link'>Yasashii Uta</a>, mantenida y actualizada en <a href='https://arashinonakade.neocities.org/about.html' class='text-blue-link'>Arashi no naka de</a>."

    new_entry = {
        'artist': json_data['artist'],
        'song': json_data['song'],
        'intro': 'He de confesar que no está en mi Top 100 canciones de Arashi, pero aquí va.',
        'content': json_data['lyrics'],
        'info': info_section
    }

    entry_filename = limpiar_para_url(json_data['song'])
    with open(f"site/arashi/{album_folder}/{entry_filename}.json", "w", encoding="utf-8") as f:
        json.dump(new_entry, f, ensure_ascii=False, indent=2)
        
if __name__ == "__main__":
    final_transformation()