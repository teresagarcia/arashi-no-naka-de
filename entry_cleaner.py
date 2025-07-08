import json
import re
with open("arashi_entries.json") as json_file:
    json_data = json.load(json_file)

full_text = json_data[0]['content']

# Remove \n before and after tags
result = re.sub(r'\n(?=<)', '', full_text)
result = re.sub(r'(?<=>)\n', '', result)

# Replace \n with whitespace in other cases
result = result.replace("\n", " ")

# Remove comments
result = re.sub(r'<!--.*?-->', '', result, flags=re.DOTALL)

# Remove all tags except </div> (used for linebreak), <a> and <b> 
result = re.sub(r'<(?!/div\b)(?!a\b)(?!/a\b)(?!b\b)(?!/b\b)[^>]+>', '', result)

# Replace </div> with <br/>
result = result.replace('</div>', '<br/>')

# Remove multiple whitespaces
result = re.sub(r'\s{2,}', ' ', result)

# Add \n after <br/> (except last line) for readability
result = re.sub(r'<br\s*/?>(?!\s*$)', '<br/>\n', result)
print(result)

# ----- esto debería ir separado ----
# Separar letra e info
lines = result.splitlines()

for i, line in enumerate(lines):
    if "Créditos:" in line or "Info de la canción" in line:
        index = i
        break

lyrics = "\n".join(lines[:index])     
song_info = "\n".join(lines[index:])     

print("Sólo letra:\n", lyrics)
print("Créditos:\n", song_info)

# Separar partes del título
title = json_data[0]['title'].replace('[Letra]', '')
title_parts = title.split('-')
artist = title_parts[0].strip()
song = title_parts[1].strip()

print("Artista:", artist, ", song:", song)

#Save data in json file
with open("clean_entries.json", "r", encoding="utf-8") as f:
    clean_entries = json.load(f)

new_entry = {"artist": artist, "song": song, "lyrics": lyrics, "info": song_info, "blogger_link": json_data[0]['link']}
clean_entries.append(new_entry)

# 3. Guardar de nuevo
with open("clean_entries.json", "w", encoding="utf-8") as f:
    json.dump(clean_entries, f, indent=2, ensure_ascii=False)