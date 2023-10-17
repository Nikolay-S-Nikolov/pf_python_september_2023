targets = [int(x) for x in input().split()]
command = input()

while command != "End":
    command = command.split()
    if command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        if index in range(len(targets)) and index + radius in range(len(targets)) \
                and index - radius in range(len(targets)):
            for _ in range(radius * 2 + 1):
                targets.pop(index - radius)
        else:
            print("Strike missed!")
    command = input()

print(*targets, sep="|")
