# sequence_of_numbers = list(map(int, input().split(", ")))
sequence_of_numbers = [int(n) for n in input().split(', ')]
group = 0
while sequence_of_numbers:   # while not len(sequence_of_numbers) == 0:
    group += 10
    current_group_list = [num for num in sequence_of_numbers if num in range(group - 10, group + 1)]
    # for group_number in sequence_of_numbers:
    #     if group_number in range(group - 10, group + 1):
    #         current_group_list.append(group_number)
    sequence_of_numbers = [number for number in sequence_of_numbers if number not in current_group_list ]
    # for item in current_group_list:
    #     sequence_of_numbers.remove(item)
    print(f"Group of {group}'s: {current_group_list}")
