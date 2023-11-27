text = input()

for idx in range(len(text)):
    if text[idx] == ":":
        print(text[idx] + text[idx + 1])
