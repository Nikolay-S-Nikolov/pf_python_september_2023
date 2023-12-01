import re

pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"

string_input = input()
emoji = list(re.finditer(pattern, string_input))
threshold = re.findall(r'\d', string_input)
cool_threshold = 1
for idx in range(len(threshold)):
    cool_threshold = cool_threshold * int(threshold[idx])
print(f"Cool threshold: {cool_threshold}")
print(f"{len(emoji)} emojis found in the text. The cool ones are:")
for cool_emoji in emoji:
    emoji_value = sum(ord(x) for x in cool_emoji.group() if not x.isdigit())
    if emoji_value >= cool_threshold:
        print(cool_emoji.group())
