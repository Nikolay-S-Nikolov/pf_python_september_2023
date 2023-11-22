some_dict = {"Pesho": 20, "Gosho": 30}
# print(sorted(some_dict))
print(dict(sorted(some_dict.items(), key=lambda x: x[0])))
