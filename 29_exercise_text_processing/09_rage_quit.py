string_numbers = input()
result = ""
current_string = ''
unique_symbols = []
num_repeat = ''
for idx in range(len(string_numbers)):
    if string_numbers[idx].isnumeric():
        if (idx + 1) in range(len(string_numbers)) and string_numbers[idx + 1].isnumeric():
            num_repeat += string_numbers[idx]
        else:
            num_repeat += string_numbers[idx]
            result += current_string * int(num_repeat)
            current_string = ''
            num_repeat = ''

    else:
        current_string += string_numbers[idx].upper()
        if string_numbers[idx].upper() not in unique_symbols:
            unique_symbols.append(string_numbers[idx].upper())

print(f"Unique symbols used: {len(unique_symbols)}")
print(result)
