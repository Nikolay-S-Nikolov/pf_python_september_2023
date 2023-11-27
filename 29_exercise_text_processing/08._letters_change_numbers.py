string_of_numbers_between_two_letters = input()
string_list = string_of_numbers_between_two_letters.split()
total_sum = 0
for current_string in string_list:
    result = 0
    front_letter = current_string[0]
    after_letter = current_string[-1]
    number = int(current_string[1:-1])
    front_letter_num = ord(front_letter)
    after_letter_num = ord(after_letter)
    if front_letter.islower():
        result += number * (front_letter_num - 96)
    else:
        result += number / (front_letter_num - 64)
    if after_letter.islower():
        result +=(after_letter_num - 96)
    else:
        result -= after_letter_num - 64
    total_sum += result
print(f'{total_sum: .2f}')
