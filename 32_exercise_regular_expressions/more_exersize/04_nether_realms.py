import re

pattern_letters = r"([^0-9+\-*\/.])"
pattern_num = r"([+]|[-]?[\d]+[.]?\d*)"
demons = sorted([x.strip() for x in input().split(',')])

for demon in demons:
    health_letters = re.findall(pattern_letters, demon)
    demon_total_health = 0.00
    for letter in health_letters:
        demon_total_health += ord(letter)
    damage_numbers = re.findall(pattern_num, demon)
    total_damage = sum(float(x) for x in damage_numbers)
    if '*' in demon:
        for _ in range(demon.count('*')):
            total_damage *= 2
    if '/' in demon:
        for _ in range(demon.count('/')):
            total_damage /= 2
    print(f"{demon} - {int(demon_total_health)} health, {total_damage:.2f} damage")
