# squares = {1: 1, 2: 4, 3: 9}

# for key in squares.keys():
#     print(key, end=" ")
# print()
# for value in squares.values():
#     print(value, end=" ")
# for k, v in squares.items():
#     print("key =", k, "; Value =",v)
my_dict = {"name": "Ivan", "age": 22}

if "name" in my_dict.keys():
    print(my_dict.get("name"))
if 22 in my_dict.values():
    print("22 is value in the dictionary")
