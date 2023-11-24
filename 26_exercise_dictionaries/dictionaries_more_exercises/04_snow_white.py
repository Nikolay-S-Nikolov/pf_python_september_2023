command = input()
dwarf_data = {}

while command != "Once upon a time":
    name, hat_color, physics = command.split(" <:> ")
    physics = int(physics)
    if hat_color not in dwarf_data.keys():
        dwarf_data[hat_color] = {}
        dwarf_data[hat_color][name] = physics
    else:
        if name not in dwarf_data[hat_color].keys():
            dwarf_data[hat_color][name] = physics
        else:
            if physics > dwarf_data[hat_color][name]:
                dwarf_data[hat_color][name] = physics
    command = input()
dwarf_dict = {}

for color, dwarfs in dwarf_data.items():
    same_hat_dwarfs = len(dwarfs)
    for dwarf, physics_num in dwarfs.items():
        dwarf_name_color = f"{dwarf}|{color}"
        dwarf_dict[dwarf_name_color] = {"name": dwarf, "physics": physics_num, "color_member": same_hat_dwarfs,
                                        "hat_color": color}

for member in sorted(dwarf_dict, key=lambda x: (dwarf_dict[x]["physics"], dwarf_dict[x]["color_member"]), reverse=True):
    current_dwarf = dwarf_dict[member]
    print(f"({current_dwarf['hat_color']}) {current_dwarf['name']} <-> {current_dwarf['physics']}")
