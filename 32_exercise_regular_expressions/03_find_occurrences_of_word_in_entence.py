import re

string_text = input()
word = input()

regex_pattern = fr"(?i)\b{word}\b"

result = re.findall(regex_pattern, string_text)
print(len(result))
