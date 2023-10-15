def switch_second_and_last_letter(word: str) -> str:
    word_as_list = [ch_ar for ch_ar in word]
    word_as_list[0], word_as_list[-1] = word_as_list[-1], word_as_list[0]
    switched_letter = ''
    for ch in word_as_list:
        switched_letter += ch
    return switched_letter


def decipher_secret_message(message: str) -> str:
    message_list = message.split()
    secret_message = ''
    for words in message_list:
        asci_letter = ''
        word = ''
        for char in words:
            if char.isnumeric():
                asci_letter += char
            elif char.isalpha():
                word += char
        letter = switch_second_and_last_letter(word)
        secret_word = chr(int(asci_letter)) + letter + ' '
        secret_message += secret_word
    return secret_message


result = decipher_secret_message(input())
print(result)
#
# secret_message = input().split()
#
# for words in secret_message:
#     letters = []
#     letter = ''
#     asci_letter = ''
#     for char in words:
#         if char.isnumeric():
#             asci_letter += char
#         elif char.isalpha():
#             letters.append(char)
#     letters[0], letters[-1] = letters[-1], letters[0]
#     for char in letters:
#         letter += char
#     secret_word = chr(int(asci_letter)) + letter
#     print(secret_word, end=' ')
