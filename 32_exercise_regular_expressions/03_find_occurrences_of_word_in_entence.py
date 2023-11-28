import re

string_text = input()
word = input()

regex_pattern = fr"\b{word}\b"

result = re.findall(regex_pattern, string_text, re.I)
print(len(result))
