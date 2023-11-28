import re

input_string = input()
regex_pattern = r"(^|(?<=\s))(\-?)([0]|[1-9][0-9]*)(\.\d*)?($|(?=\s))"
result = re.findall(regex_pattern, input_string)
for match in result:
    number = ''
    for idx in range(len(match)):
        if match[idx] != '':
            number += match[idx]
    print(number, end=' ')
