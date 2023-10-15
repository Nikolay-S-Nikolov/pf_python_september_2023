encrypted_message = [i for i in input()]
number_list = [int(n) for n in encrypted_message if n.isdigit()]
non_number_list = [s for s in encrypted_message if not s.isdigit()]
take_list = [number_list[t] for t in range(0, len(number_list), 2)]
skip_list = [number_list[s] for s in range(1, len(number_list), 2)]
result_string = ""
for skip_take in range(len(skip_list)):
    if take_list[skip_take] != 0:
        for _ in range(take_list[skip_take]):
            if len(non_number_list) == 0:
                break
            result_string += non_number_list.pop(0)
    for _ in range(skip_list[skip_take]):
        if len(non_number_list) == 0:
            break
        del non_number_list[0]
# print(number_list)
# print(non_number_list)
# print(take_list)
# print(skip_list)
print(result_string)
#  skipTest_String044160
