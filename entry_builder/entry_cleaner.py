import json
import re
import sys

def clean_entry(only_save=False):
    with open("data/arashi_entries.json") as json_file:
        json_data = json.load(json_file)

    result = json_data[0]['content']

    # Remove \n before and after tags
    result = re.sub(r'\n(?=<)', '', result)
    result = re.sub(r'(?<=>)\n', '', result)

    # Replace \n with whitespace in other cases
    result = result.replace("\n", " ")
    if not only_save:

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
    json_data[0]['content'] = result

    #guardar en fichero intermedio
    with open("data/clean_entry.json", "w", encoding="utf-8") as f:
        json.dump(json_data[0], f, indent=2, ensure_ascii=False)
        
if __name__ == "__main__":
    only_save = False
    if len(sys.argv) > 1:
        only_save = True if sys.argv[1]=='S' else False
    clean_entry(only_save)
