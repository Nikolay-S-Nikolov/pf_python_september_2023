neighborhood = [int(x) for x in input().split("@")]
command = input()
index = 0
while command != "Love!":
    index += int(command.split()[1])
    if index > len(neighborhood) - 1:
        index = 0
    if neighborhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        neighborhood[index] -= 2
        if neighborhood[index] == 0:
            print(f"Place {index} has Valentine's day.")
    command = input()
print(f"Cupid's last position was {index}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    house_count = len([x for x in neighborhood if x != 0])
    # house_count = 0
    # for i in neighborhood:
    #     if i != 0:
    #         house_count += 1
    print(f"Cupid has failed {house_count} places.")
