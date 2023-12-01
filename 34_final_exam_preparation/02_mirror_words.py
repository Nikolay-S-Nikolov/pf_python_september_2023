import re

text_string = input()
pattern = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

hidden_words = re.findall(pattern, text_string)
valid_pairs_count = len(hidden_words)
mirror_words = []
for word in hidden_words:
    if word[1] == word[2][::-1]:
        mirror_words.append(f'{word[1]} <=> {word[2]}')
if not hidden_words:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{valid_pairs_count} word pairs found!")
    if not mirror_words:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(', '.join(mirror_words))
