import re

string_line = input()

regex_pattern = "\d+"

while string_line:
    result = re.findall(regex_pattern, string_line)
    if result:
        print(" ".join(result), end=" ")
    string_line = input()
