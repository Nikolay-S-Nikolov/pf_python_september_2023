dragon_army = {}
number_n = int(input())

for _ in range(number_n):
    type_dragon, name, damage, health, armor = input().split()
    if damage == 'null':
        damage = 45
    if health == 'null':
        health = 250
    if armor == 'null':
        armor = 10
    damage = int(damage)
    armor = int(armor)
    health = int(health)
    dragon = {name: [damage, health, armor]}
    if type_dragon not in dragon_army.keys():
        dragon_army[type_dragon] = dragon
    else:
        for n, d in dragon_army[type_dragon].items():
            if name == n:
                dragon_army[type_dragon][n] = [damage, health, armor]
                break
        else:
            dragon_army[type_dragon].update(dragon)
for color, dragon_data in dragon_army.items():
    av_damage = sum(x[0] for x in dragon_data.values())/len(dragon_data)
    av_health = sum(x[1] for x in dragon_data.values())/len(dragon_data)
    av_armor = sum(x[2] for x in dragon_data.values())/len(dragon_data)
    print(f"{color}::({av_damage:.2f}/{av_health:.2f}/{av_armor:.2f})")
    for dragon_name, data in sorted(dragon_data.items()):
        print(f"-{dragon_name} -> damage: {data[0]}, health: {data[1]}, armor: {data[2]}")
