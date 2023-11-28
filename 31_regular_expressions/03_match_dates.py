import re

input_string = input()

regex_pattern = r"(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})"

result = re.findall(regex_pattern,input_string)

for matches in result:
    print(f"Day: {matches[0]}, Month: {matches[2]}, Year: {matches[3]}")