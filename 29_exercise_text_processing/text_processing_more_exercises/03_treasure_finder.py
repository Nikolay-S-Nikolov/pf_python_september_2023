treasure_key = [int(x) for x in input().split()]

while True:
    string_lines = input()
    if string_lines == 'find':
        break
    decrypted_message = ''
    reset_key_idx = len(treasure_key)
    key_idx = 0
    for idx in range(len(string_lines)):
        if key_idx == reset_key_idx:
            key_idx = 0
        current_char = string_lines[idx]
        decrypted_message += chr(ord(current_char) - treasure_key[key_idx])
        key_idx += 1
    treasure_type = ''
    it_is_treasure_type = False
    for t in decrypted_message:
        if it_is_treasure_type:
            if t == "&":
                break
            treasure_type += t
        if t == "&":
            it_is_treasure_type = True
    coordinates = decrypted_message[(decrypted_message.index("<")+1):decrypted_message.index('>')]
    print(f"Found {treasure_type} at {coordinates}")
