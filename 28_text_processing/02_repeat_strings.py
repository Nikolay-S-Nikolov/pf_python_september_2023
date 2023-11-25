text = input().split()
result = ''
for item in text:
    result += item * len(item)
print(result)
