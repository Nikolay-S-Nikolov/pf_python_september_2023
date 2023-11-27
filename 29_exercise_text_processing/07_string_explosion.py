string_text = input()
result = ''
count = 0
for idx in range(len(string_text)):
    if count > 0 and string_text[idx] != '>':
        count -= 1
    elif string_text[idx] == '>':
        result += string_text[idx]
        count += int(string_text[idx + 1])
    else:
        result += string_text[idx]
print(result)
