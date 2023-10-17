def shoot_command(target_list: list, idx: int, pwr: int) -> list:
    if idx in range(len(target_list)):
        target_list[idx] -= pwr
        if target_list[idx] <= 0:
            target_list.pop(idx)
    return target_list


def add_target(target_list: list, idx: int, value_add: int) -> list:
    if idx in range(len(target_list)):
        target_list.insert(idx, value_add)
    else:
        print("Invalid placement!")
    return target_list


def strike_command(target_list: list, idx: int, rad: int) -> list:
    if idx in range(len(target_list)) and idx + rad in range(len(target_list)) \
            and idx - rad in range(len(target_list)):
        for _ in range(rad * 2 + 1):
            target_list.pop(idx - rad)
    else:
        print("Strike missed!")
    return target_list


targets = [int(x) for x in input().split()]
command = input()

while command != "End":
    command = command.split()
    if command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        targets = shoot_command(targets, index, power)

    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        targets = add_target(targets, index, value)

    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        targets = strike_command(targets,index,radius)

    command = input()

print('|'.join(str(x)for x in targets))
