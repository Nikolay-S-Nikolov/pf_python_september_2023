import re

string_text = input()
pattern = r"www\.[A-Za-z0-9-\.]+\.[a-z]+"
while string_text:
    result = re.findall(pattern,string_text)
    # print(result)
    for match in result:
        print(result[0])
    string_text = input()
