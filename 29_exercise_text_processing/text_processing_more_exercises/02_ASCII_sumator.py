char_1 = input()
char_2 = input()
string_char = input()
start_range = min(ord(char_1), ord(char_2)) + 1
end_range = max(ord(char_1), ord(char_2))
total_sum = 0
for char in string_char:
    if ord(char) in range(start_range, end_range):
        total_sum += ord(char)

print(total_sum)
