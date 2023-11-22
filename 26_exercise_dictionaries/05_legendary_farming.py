items_dict = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = ""

while True:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items_dict.keys():
            items_dict[key] = 0
        items_dict[key] += value
        if items_dict["shards"] >= 250:
            items_dict["shards"] -= 250
            legendary_item = "Shadowmourne"
            break
        elif items_dict["fragments"] >= 250:
            items_dict["fragments"] -= 250
            legendary_item = "Valanyr"
            break
        elif items_dict["motes"] >= 250:
            items_dict["motes"] -= 250
            legendary_item = "Dragonwrath"
            break
    if legendary_item:
        break
print(f"{legendary_item} obtained!")
for material, quantity in items_dict.items():
    print(f"{material}: {quantity}")
