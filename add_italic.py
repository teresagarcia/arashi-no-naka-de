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
