groceries_list = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()

    if command[0] == "Urgent":
        if command[1] not in groceries_list:
            groceries_list.insert(0, command[1])

    elif command[0] == "Unnecessary":
        if command[1] in groceries_list:
            groceries_list.remove(command[1])

    elif command[0] == "Correct":
        if command[1] in groceries_list:
            index = groceries_list.index(command[1])
            groceries_list[index] = command[2]

    elif command[0] == "Rearrange":
        if command[1] in groceries_list:
            groceries_list.remove(command[1])
            groceries_list.append(command[1])

    command = input()

print(*groceries_list, sep=", ")
