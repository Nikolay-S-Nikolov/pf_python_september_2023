import re

locations = input()
pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"

destinations_list = re.findall(pattern, locations)
travel_points = sum(len(x[1]) for x in destinations_list)
destinations = []
for destination in destinations_list:
    destinations.append((destination[1]))
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
