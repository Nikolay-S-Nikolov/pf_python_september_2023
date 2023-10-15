# # print("It is working!")
# # print("It is working!")
# # print("It is working!")
# # test_list = ['end', 'command', 'list', 'elif']
# # print(test_list.index('list'))
#
# # schedule = input()
# # print("Exercise" in schedule)
#
# # string = "oellH"
# # string[0], string[-1] = string[-1], string[0]
# # print(string)
# test_list = ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz']
# test_list[4:10] = [''.join(test_list[4:10])]
# print(test_list)
# partition = 5
# divide_partition = test_list[4]
# result = len(divide_partition) // partition
# del test_list[4]
# counter = 0
# divided_element = ''
# divided_element_list = []
# for char in range(len(divide_partition)):
#     divided_element += divide_partition[char]
#     counter += 1
#     if partition == 1:
#         continue
#     elif partition > 1 and counter == result:
#         divided_element_list.append(divided_element)
#         divided_element = ''
#         partition -= 1
#         counter = 0
# divided_element_list.append(divided_element)
# print(divided_element_list)
# index = 4
# for items in divided_element_list[::-1]:
#     test_list.insert(index, items)
# print(" ".join(test_list))
# pokemon_list = [int(i) for i in input().split()]
# element = pokemon_list[int(input())]
# increased_decreased_pokemon_list = []
# for item in pokemon_list:
#     if element < item:
#         item -= element
#         increased_decreased_pokemon_list.append(item)
#     else:
#         item += element
#         increased_decreased_pokemon_list.append(item)
# print(increased_decreased_pokemon_list)
ind_list = [22, 15, 20, 22]
del ind_list[0]
print(ind_list)