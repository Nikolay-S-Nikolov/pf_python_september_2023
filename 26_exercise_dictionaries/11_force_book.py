force_users_dict = {}
command = input()

while command != "Lumpawaroo":
    if " | " in command:
        force_side, force_user = command.split(" | ")
        user_is_part_of_the_force = False
        for user in force_users_dict.values():
            if force_user in user:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_users_dict.keys():
                force_users_dict[force_side] = []
            force_users_dict[force_side].append(force_user)
    if " -> " in command:
        force_user, force_side = command.split(" -> ")
        for user in force_users_dict.values():
            if force_user in user:
                user.remove(force_user)
                break
        if force_side not in force_users_dict.keys():
            force_users_dict[force_side] = []
        force_users_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for side, users in force_users_dict.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
