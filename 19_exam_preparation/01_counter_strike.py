energy = int(input())
distance = input()

count = 0
while distance != "End of battle":
    distance = int(distance)
    if energy >= distance:
        count += 1
        energy -= distance
        if count % 3 == 0:
            energy += count
    else:
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        break
    distance = input()
else:
    print(f"Won battles: {count}. Energy left: {energy}")
