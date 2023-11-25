string = input()

while string != 'end':
    # print(f'{string} = {string[::-1]}')
    reversed_text = ''
    for ch in reversed(string):
        reversed_text += ch
    print(f'{string} = {reversed_text}')
    string = input()
