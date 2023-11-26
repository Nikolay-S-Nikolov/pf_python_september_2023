first_string, second_string = input().split()
total_sum = 0

if len(first_string) > len(second_string):
    for char in range(len(second_string)):
        total_sum += ord(first_string[char]) * ord(second_string[char])
    for ch in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[ch])
elif len(second_string) > len(first_string):
    for char in range(len(first_string)):
        total_sum += ord(first_string[char]) * ord(second_string[char])
    for ch in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[ch])
else:
    for char in range(len(second_string)):
        total_sum += ord(first_string[char]) * ord(second_string[char])
print(total_sum)