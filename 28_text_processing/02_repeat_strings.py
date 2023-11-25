command = input()
dwarf_data = []

while command != "Once upon a time":
    dwarf_name, dwarf_hat_color, dwarf_physics = command.split(" <:> ")
    dwarf_physics = int(dwarf_physics)
    same_name_color = False
    for items in dwarf_data:
        if items["dwarf_name"] == dwarf_name \
                and items["dwarf_hat_color"] == dwarf_hat_color:
            same_name_color = True
            if items["dwarf_physics"] < dwarf_physics:
                items["dwarf_physics"] = dwarf_physics
    if not same_name_color:
        dwarf_data.append({"dwarf_name": dwarf_name, "dwarf_hat_color": dwarf_hat_color,
                           "dwarf_physics": dwarf_physics})
    command = input()
color_list = [y['dwarf_hat_color'] for y in dwarf_data]
dwarf_data = [x for x in
              sorted(dwarf_data, key=lambda z: (z["dwarf_physics"], color_list.count(z['dwarf_hat_color'])),reverse=True)]
for dwarf in dwarf_data:
    color = dwarf['dwarf_hat_color']
    name = dwarf["dwarf_name"]
    physics = dwarf["dwarf_physics"]
    print(f"({color}) {name} <-> {physics}")
