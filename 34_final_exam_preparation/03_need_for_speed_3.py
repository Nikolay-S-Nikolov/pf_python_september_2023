def drive(car_dict, command_string):
    car_model = command_string.split(' : ')[1]
    distance = int(command_string.split(' : ')[2])
    fuel = int(command_string.split(' : ')[3])
    if fuel > car_dict[car_model][1]:
        message = "Not enough fuel to make that ride"
        return car_dict, message
    car_dict[car_model][1] -= fuel
    car_dict[car_model][0] += distance
    message = f"{car_model} driven for {distance} kilometers. {fuel} liters of fuel consumed."
    if car_dict[car_model][0] >= 100000:
        message += f"\nTime to sell the {car_model}!"
        del car_dict[car_model]
    return car_dict, message


def refuel(car_dict, command_string):
    car_model = command_string.split(' : ')[1]
    fuel_to_add = int(command_string.split(' : ')[2])
    initial_car_fuel = car_dict[car_model][1]
    car_dict[car_model][1] += fuel_to_add
    if car_dict[car_model][1] > 75:
        fuel_to_add = (75 - initial_car_fuel)
        car_dict[car_model][1] = 75
    message = f"{car_model} refueled with {fuel_to_add} liters"
    return car_dict, message


def revert(car_dict, command_string):
    car_model = command_string.split(' : ')[1]
    kilometers = int(command_string.split(' : ')[2])
    car_dict[car_model][0] -= kilometers
    if car_dict[car_model][0] < 10000:
        car_dict[car_model][0] = 10000
        message = ''
    else:
        message = f"{car_model} mileage decreased by {kilometers} kilometers"
    return car_dict, message


number_n = int(input())
cars = {}
for _ in range(number_n):
    car, initial_mileage, initial_fuel = input().split('|')
    cars[car] = [int(initial_mileage), int(initial_fuel)]

command = input()
while command != 'Stop':
    action = command.split(' : ')[0]
    if action == 'Drive':
        cars, result = drive(cars, command)
        print(result)
    elif action == 'Refuel':
        cars, result = refuel(cars, command)
        print(result)
    elif action == 'Revert':
        cars, result = revert(cars, command)
        if result:
            print(result)
    command = input()

for car_name, data in cars.items():
    print(f"{car_name} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.")
