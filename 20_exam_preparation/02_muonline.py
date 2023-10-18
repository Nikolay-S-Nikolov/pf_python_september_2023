rooms = input().split("|")
health = 100
bitcoins = 0
room_count = 0
you_pass_all_rooms = True

for room in rooms:
    room_count += 1
    action, value = room.split()
    value = int(value)
    if action == "potion":
        if health + value > 100:
            health_amount = 100 - health
            health = 100
        else:
            health_amount = value
            health += value
        print(f"You healed for {health_amount} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {room_count}")
            you_pass_all_rooms = False
            break
if you_pass_all_rooms:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
