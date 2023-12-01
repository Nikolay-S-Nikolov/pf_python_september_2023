import re

string_text = input()
pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"

valid_emojis = re.findall(pattern, string_text)
# cool_threshold = sum(int(x) for x in string_text if x.isdigit())
cool_threshold = 1
for char in string_text:
    if char.isdigit():
        cool_threshold *= int(char)
print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
for emoji in valid_emojis:
    coolness = sum(ord(x) for x in emoji[1])
    if coolness > cool_threshold:
        print(emoji[0] + emoji[1] + emoji[0])
# print(valid_emojis)
