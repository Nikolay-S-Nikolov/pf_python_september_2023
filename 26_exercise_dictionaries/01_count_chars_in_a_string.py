characters = [char for char in input() if char != " "]
letters = {}
for letter in characters:
    if letter not in letters.keys():
        letters[letter] = 0
    letters[letter] += 1
for key, value in letters.items():
    print(f"{key} -> {value}")
