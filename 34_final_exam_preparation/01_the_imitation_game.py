message = input()
while True:
    instruction = input()
    if instruction == 'Decode':
        break
    command = instruction.split('|')[0]
    if command == 'Move':
        number_of_letters = int(instruction.split('|')[1])
        message = message[number_of_letters:] + message[:number_of_letters]
    elif command == 'Insert':
        index = int(instruction.split('|')[1])
        value = instruction.split('|')[2]
        message = message[:index] + value + message[index:]
    elif command == 'ChangeAll':
        substring, replacement = instruction.split('|')[1], instruction.split('|')[2]
        if substring in message:
            message_list = message.split(substring)
            message = ''
            for idx in range(len(message_list)):
                if idx != (len(message_list) - 1):
                    message += message_list[idx] + replacement
                else:
                    message += message_list[idx]

print(f"The decrypted message is: {message}")
