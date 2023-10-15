def merge_command(command_list: list, data_list: list) -> list:
    _, start_index, end_index = command_list
    data_list[int(start_index):int(end_index)+1] = ["".join(data_list[int(start_index):int(end_index)+1])]
    return data_list


def divide_command(command_list: list, data_list: list) -> list:
    _, ind, partitions = command_list
    index = int(ind)
    partition = int(partitions)
    divide_partition = data_list[index]
    partition_size = len(divide_partition) // partition
    del data_list[index]
    divided_element = ''
    divided_element_list = []
    for char in range((partition-1)*partition_size):
        divided_element += divide_partition[char]
        if len(divided_element) == partition_size:
            divided_element_list.append(divided_element)
            divided_element = ''
    divided_element_list.append(divided_element)
    for items in divided_element_list[::-1]:
        data_list.insert(index, items)
    return data_list


array_of_data = input().split()
command = input()
result = ''
while not command == '3:1':
    command_as_list = command.split()
    if command_as_list[0] == "merge":
        result = merge_command(command_as_list, array_of_data)
    elif command_as_list[0] == "divide":
        result = divide_command(command_as_list, array_of_data)
    command = input()
print(" ".join(result))
