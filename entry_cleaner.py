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

