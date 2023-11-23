commands_number = int(input())
registered_users = {}

for _ in range(commands_number):
    command = input().split()
    action = command[0]
    if action == "register":
        username = command[1]
        license_plate_number = command[2]
        if username in registered_users.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            registered_users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif action == "unregister":
        username = command[1]
        if username not in registered_users.keys():
            print(f"ERROR: user {username} not found")
        else:
            del registered_users[username]
            print(f"{username} unregistered successfully")

for user, license_plate in registered_users.items():
    print(f"{user} => {license_plate}")
