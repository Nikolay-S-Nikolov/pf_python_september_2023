import re

input_string = input()

regex_pattern = r"\b_([a-zA-Z0-9]*)\b"
result = re.findall(regex_pattern, input_string)

print(",".join(result))
