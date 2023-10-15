# -- list comprehension
version = [int(elements) for elements in input().split('.')]
# -- usage of for cycle
# version_list_int = []
# for elements in version:
#     version_list_int.append(int(elements))
# -- usage of map()
# version = list(map(int, input().split('.')))
next_version = []
version[-1] += 1
for index in range(len(version) - 1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        version[index - 1] += 1

result = [str(new_version) for new_version in version]
# result = ''
# for new_version in version:
#     result +=str(new_version)
print('.'.join(result))
