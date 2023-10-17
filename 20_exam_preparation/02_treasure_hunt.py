treasure_list = input().split("|")
command = input()

while command != "Yohoho!":
    command = command.split()
    if command[0] == "Loot":
        for idx_item in range(1, len(command)):
            if command[idx_item] not in treasure_list:
                treasure_list.insert(0, command[idx_item])

    elif command[0] == "Drop":
        idx_item = int(command[1])
        if idx_item in range(len(treasure_list)):
            drop_item = treasure_list.pop(idx_item)
            treasure_list.append(drop_item)

    elif command[0] == "Steal":
        stole_count = int(command[1])
        stole_list = []
        for _ in range(stole_count):
            if treasure_list:
                stole_list.append(treasure_list.pop())

        print(*stole_list[::-1], sep=", ")
    command = input()

if treasure_list:
    sum_len_items = 0
    for i in range(len(treasure_list)):
        sum_len_items += len(treasure_list[i])
    average_gain = sum_len_items / len(treasure_list)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

else:
    print("Failed treasure hunt.")
