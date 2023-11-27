text = input()
result = text[0]
for char in text:
    if result[-1] != char:
        result += char
print(result)
