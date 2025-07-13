import json

def divide_lyrics_info():
    with open("clean_entry.json") as json_file:
        json_data = json.load(json_file)

    lines = json_data['content'].splitlines()

    for i, line in enumerate(lines):
        if "Créditos:" in line or "Info de la canción" in line:
            index = i
            break

    lyrics = "\n".join(lines[:index])     
    song_info = "\n".join(lines[index:])     

    print("Sólo letra:\n", lyrics)
    print("Créditos:\n", song_info)

    # Separar partes del título
    title = json_data['title'].replace('[Letra]', '')
    title_parts = title.split('-')
    artist = title_parts[0].strip()
    song = title_parts[1].strip()

    print("Artista:", artist, ", song:", song)

    #Save data in json file

    new_entry = {
        "artist": artist, 
        "song": song, 
        "lyrics": lyrics, 
        "info": song_info, 
        "blogger_link": json_data['link']
        }

    with open("preformat_entry.json", "w", encoding="utf-8") as f:
        json.dump(new_entry, f, indent=2, ensure_ascii=False)
        
if __name__ == "__main__":
    divide_lyrics_info()
    
    