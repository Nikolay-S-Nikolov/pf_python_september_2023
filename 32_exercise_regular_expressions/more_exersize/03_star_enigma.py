import re


def letters_count(message):
    pattern = r'[star]'
    result = re.findall(pattern, message, flags=re.IGNORECASE)
    decrypted_message = ''
    for char in message:
        decrypted_message += chr(ord(char) - len(result))
    return decrypted_message


attacked_planets = []
destroyed_planets = []
number_n = int(input())
messages_list = []
for _ in range(number_n):
    current_message = input()
    message_after_count_decryption = letters_count(current_message)
    pattern_final = r"@([A-Za-z]+)[^@\-!:>]*?:[^@\-!:>]*?(\d+)[^@\-!:>]*?![^@\-!:>]*?" \
                    r"([A|D])[^@\-!:>]*?![^@\-!:>]*?->[^@\-!:>]*?(\d+)[^@\-!:>]*?"
    result_list = list(re.findall(pattern_final, message_after_count_decryption))
    if result_list:
        planet_name, population, attack_type, soldier_count = result_list[0]
        if attack_type == "A":
            attacked_planets.append(planet_name)
        elif attack_type == "D":
            destroyed_planets.append(planet_name)
print(f"Attacked planets: {len(attacked_planets)}")
for attacked_planet in sorted(attacked_planets):
    print(f"-> {attacked_planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for destroyed_planet in sorted(destroyed_planets):
    print(f"-> {destroyed_planet}")
