def shoot(targets_list: list, idx: int, count: int):
    if idx in range(len(targets_list)):
        shot = targets_list[idx]
        for i in range(len(targets_list)):
            if targets_list[i] != -1:
                if targets_list[i] > shot:
                    targets_list[i] -= shot
                else:
                    targets_list[i] += shot
        targets_list[idx] = -1
        count += 1
    return targets_list, count


targets_value = [int(x) for x in input().split()]
command = input()
shot_count = 0

while command != "End":
    targets_value, shot_count = shoot(targets_value, int(command), shot_count)
    command = input()

print(f"Shot targets: {shot_count} ->", end=" ")
print(*targets_value)
