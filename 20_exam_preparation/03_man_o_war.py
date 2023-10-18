def fire(warship_status: list, index, damage):
    ship_sinks = False
    if index in range(len(warship_status)):
        warship_status[index] -= damage
        if warship_status[index] <= 0:
            ship_sinks = True
    return warship_status, ship_sinks


def defend(pirate_status: list, start_idx: int, end_idx: int, damage: int):
    ship_sinks = False
    if start_idx in range(len(pirate_status)) and end_idx in range(len(pirate_status)):
        for i in range(start_idx, end_idx + 1):
            pirate_status[i] -= damage
            if pirate_status[i] <= 0:
                ship_sinks = True
                break
    return pirate_status, ship_sinks


def repair(pirate_status: list, index: int, health: int, max_health: int):
    if index in range(len(pirate_status)):
        pirate_status[index] += health
        if pirate_status[index] > max_health:
            pirate_status[index] = max_health
    return pirate_status


def count_need_repair(pirate_status: list, max_health: int):
    count_to_repair = 0
    for section in pirate_status:
        if section / max_health * 100 < 20:
            count_to_repair += 1
    return count_to_repair


pirate_ship_status = [int(x) for x in input().split(">")]
war_ship_status = [int(x) for x in input().split(">")]
max_health_cap = int(input())
command = input()

while command != "Retire":
    command = command.split()
    action = command[0]

    if action == "Fire":
        war_ship_status, war_ship_sinks \
            = fire(war_ship_status, int(command[1]), int(command[2]))
        if war_ship_sinks:
            print("You won! The enemy ship has sunken.")
            break

    elif action == "Defend":
        pirate_ship_status, pirate_ship_sinks \
            = defend(pirate_ship_status, int(command[1]), int(command[2]), int(command[3]))
        if pirate_ship_sinks:
            print("You lost! The pirate ship has sunken.")
            break

    elif action == "Repair":
        pirate_ship_status \
            = repair(pirate_ship_status, int(command[1]), int(command[2]), max_health_cap)

    elif action == "Status":
        count = count_need_repair(pirate_ship_status, max_health_cap)
        print(f"{count} sections need repair.")
    command = input()

else:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(war_ship_status)}")
