city_dict = {}

city_data = input()

while city_data != 'Sail':
    city, population, gold = city_data.split("||")
    population = int(population)
    gold = int(gold)
    if city in city_dict.keys():
        city_dict[city][0] += population
        city_dict[city][1] += gold
    else:
        city_dict[city] = [population, gold]
    city_data = input()

events = input()
while events != 'End':
    command = events.split('=>')[0]
    if command == 'Plunder':
        town = events.split('=>')[1]
        people = int(events.split('=>')[2])
        gold_stolen = int(events.split('=>')[3])
        print(f"{town} plundered! {gold_stolen} gold stolen, {people} citizens killed.")
        city_dict[town][0] -= people
        city_dict[town][1] -= gold_stolen
        if city_dict[town][0] == 0 or city_dict[town][1] == 0:
            print(f"{town} has been wiped off the map!")
            del city_dict[town]
    elif command == 'Prosper':
        town = events.split('=>')[1]
        gold_added = int(events.split('=>')[2])
        if gold_added < 0:
            print("Gold added cannot be a negative number!")
        else:
            city_dict[town][1] += gold_added
            print(f"{gold_added} gold added to the city treasury. {town} now has {city_dict[town][1]} gold.")
    events = input()

if city_dict:
    print(f"Ahoy, Captain! There are {len(city_dict)} wealthy settlements to go to:")
    for city, data in city_dict.items():
        print(f'{city} -> Population: {data[0]} citizens, Gold: {data[1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
