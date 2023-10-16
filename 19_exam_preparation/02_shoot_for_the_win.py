MAX_CAP = 4
people = int(input())
lifts_state = [int(x) for x in input().split()]

for lift_idx in range(len(lifts_state)):
    free_space = MAX_CAP - lifts_state[lift_idx]
    if people >= free_space:
        lifts_state[lift_idx] += free_space
    else:
        lifts_state[lift_idx] += people
    people -= free_space
    if people < 0 and (lift_idx != len(lifts_state) - 1 or lifts_state[lift_idx] < MAX_CAP):
        print("The lift has empty spots!")
        break
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
print(*lifts_state)
