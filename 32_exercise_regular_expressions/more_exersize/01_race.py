import re

participants = input().split(", ")
pattern = r"([A-Za-z])"
race_info = input()
race_results = {}
for driver_name in participants:
    race_results[driver_name] = 0

while race_info != "end of race":

    name_find = re.findall(pattern, race_info)
    name = ''
    for char in name_find:
        name += char

    distance = sum(int(x) for x in race_info if x.isdigit())
    if name in race_results.keys():
        race_results[name] += distance
    race_info = input()
race_results = {k: v for k, v in sorted(race_results.items(), key=lambda x: x[1], reverse=True)}
place = 0
for driver in race_results.keys():
    place += 1
    if place == 1:
        print(f"{place}st place: {driver}")
    elif place == 2:
        print(f"{place}nd place: {driver}")
    else:
        print(f"{place}rd place: {driver}")

    if place == 3:
        break
