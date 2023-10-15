def merge_command(start_index: int, end_index: int, data_list: list) -> list:
    data_list[start_index:end_index + 1] = ["".join(data_list[start_index:end_index + 1])]
    return data_list


def divide_command(index: int, partition: int, data_list: list) -> list:
    divide_partition = data_list[index]
    letters = len(divide_partition) // partition
    del data_list[index]
    counter = 0
    divided_element = ''
    divided_element_list = []
    for char in range(len(divide_partition)):
        divided_element += divide_partition[char]
        counter += 1
        if partition > 1 and counter == letters:
            divided_element_list.append(divided_element)
            divided_element = ''
            partition -= 1
            counter = 0
    divided_element_list.append(divided_element)
    for items in divided_element_list[::-1]:
        data_list.insert(index, items)
    return data_list


array_of_data = input().split()
command = input()
result = ''
while not command == '3:1':
    command_1, first_arg, second_arg = command.split()

    if command_1 == "merge":
        start_idx = int(first_arg)
        end_idx = int(second_arg)
        start_idx = max(0, start_idx)
        end_idx = min(len(array_of_data) - 1, end_idx)
        result = merge_command(start_idx, end_idx, array_of_data)
    elif command_1 == "divide":
        command_idx = int(first_arg)
        command_partition = int(second_arg)
        result = divide_command(command_idx, command_partition, array_of_data)

    command = input()
print(" ".join(result))
