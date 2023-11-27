n_lines = int(input())

for _ in range(n_lines):
    string_text = input()
    name = ''
    age = ''
    if "@" in string_text and "|" in string_text:
        name = string_text[(string_text.index("@") + 1):string_text.index("|")]
    if "#" in string_text and "*" in string_text:
        age = string_text[(string_text.index("#") + 1):string_text.index("*")]
    print(f"{name} is {age} years old.")
