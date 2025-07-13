import json

def add_italic():
    with open("data/preformat_entry.json") as json_file:
        json_data = json.load(json_file)

    lyrics = json_data['lyrics']

    blocks = lyrics.split('<br/>\n<br/>')

    rebuilt = []
    for i,block  in enumerate(blocks):
        multiline = len(block.splitlines()) > 1
        index = -2 if multiline else 0
        split_block = block.splitlines()
        phrase, sep, _ = split_block[index].partition('<br/>')
        split_block[index] = f"<i>{phrase}</i>{sep}"
        blocks_joined = ''.join(split_block)
        rebuilt.append(blocks_joined)
            
    final_result = '<br/>\n<br/>'.join(rebuilt) + '<br/>'
    print(final_result)
    json_data['lyrics'] = final_result
    with open("data/preformat_entry.json", "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

    
if __name__ == "__main__":
    add_italic()



