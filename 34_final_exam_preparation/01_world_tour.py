def command_add(stops, token):
    index = int(token.split(':')[1])
    insert_string = token.split(':')[2]
    if index in range(len(stops)):
        stops = stops[:index] + insert_string + stops[index:]
    return stops


def command_remove(stops, token):
    start_index = int(token.split(':')[1])
    end_index = int(token.split(':')[2])
    if start_index in range(len(stops)) and end_index in range(len(stops)):
        stops = stops[:start_index] + stops[end_index + 1:]
    return stops


def command_switch(stops, token):
    old_string = token.split(':')[1]
    new_string = token.split(':')[2]
    if old_string in stops:
        stops = stops.replace(old_string, new_string)
    return stops


stops_list = input()
command = input()

while command != 'Travel':
    action = command.split(':')[0]
    if action == 'Add Stop':
        stops_list = command_add(stops_list, command)
        print(stops_list)
    elif action == 'Remove Stop':
        stops_list = command_remove(stops_list, command)
        print(stops_list)
    elif action == 'Switch':
        stops_list = command_switch(stops_list, command)
        print(stops_list)
    command = input()

print(f"Ready for world tour! Planned stops: {stops_list}")
