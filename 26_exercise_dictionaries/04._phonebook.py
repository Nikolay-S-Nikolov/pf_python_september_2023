phone_numbers = {}

while True:
    entry = input()
    if "-" not in entry:
        break
    name, number = entry.split("-")
    phone_numbers[name] = number

num_n = int(entry)
for _ in range(num_n):
    searched_name = input()
    if searched_name in phone_numbers.keys():
        print(f"{searched_name} -> {phone_numbers[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
