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
            same_name_color = True
    if not same_name_color:
        dwarf_data.append({"dwarf_name": dwarf_name, "dwarf_hat_color": dwarf_hat_color,
                           "dwarf_physics": dwarf_physics})
    command = input()
dwarf_dict = {}
for dwarf_info in dwarf_data:
    color_1 = dwarf_info["dwarf_hat_color"]
    name_1 = dwarf_info["dwarf_name"]
    physics_1 = dwarf_info["dwarf_physics"]
    if color_1 not in dwarf_dict:
        dwarf_dict[color_1] = {}
    dwarf_dict[color_1][name_1] = physics_1

dwarf_data = {}
for color, dwarfs in dwarf_dict.items():
    same_hat_dwarfs = len(dwarfs)
    for name, physics in dwarfs.items():
        name_color = f"{name}|{color}"
        dwarf_data[name_color] = {"name": name, "physics": physics,
                                  "color_member": same_hat_dwarfs, "hat_color": color}

for members in sorted(dwarf_data, key=lambda x: (dwarf_data[x]['physics'], dwarf_data[x]['color_member']),
                      reverse=True):
    current_dwarf = dwarf_data[members]
    print(f"({current_dwarf['hat_color']}) {current_dwarf['name']} <-> {current_dwarf['physics']}")
