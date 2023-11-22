items_dict = {"shards": 0, "fragments": 0, "motes": 0}
current_items = input().split()
legendary_item = ""
legendary = False

while not legendary:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items_dict.keys():
            items_dict[key] = 0
        items_dict[key] += value
        if items_dict["shards"] >= 250:
            items_dict["shards"] -= 250
            legendary = True
            legendary_item = "Shadowmourne"
        elif items_dict["fragments"] >= 250:
            items_dict["fragments"] -= 250
            legendary = True
            legendary_item = "Valanyr"
        elif items_dict["motes"] >= 250:
            items_dict["motes"] -= 250
            legendary = True
            legendary_item = "Dragonwrath"
        if legendary:
            break
    if legendary:
        break
    current_items = input().split()

print(f"{legendary_item} obtained!")
for material, quantity in items_dict.items():
    print(f"{material}: {quantity}")
