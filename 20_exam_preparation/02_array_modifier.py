def swap(array_list: list, idx_1: int, idx_2: int):
    array_list[idx_1], array_list[idx_2] = array_list[idx_2], array_list[idx_1]
    return array_list


def multiply(array_list: list, idx_1: int, idx_2: int):
    array_list[idx_1] = array_list[idx_1] * array_list[idx_2]
    return array_list


def decrease(array_list: list):
    decreased_list = [(x - 1) for x in array_list]
    return decreased_list


list_integers = [int(x) for x in input().split()]
command = input()

while command != "end":
    command = command.split()
    action = command[0]

    if action == "swap":
        list_integers = swap(list_integers, int(command[1]), int(command[2]))

    elif action == "multiply":
        list_integers = multiply(list_integers, int(command[1]), int(command[2]))

    elif action == "decrease":
        list_integers = decrease(list_integers)

    command = input()

print(*list_integers, sep=", ")
