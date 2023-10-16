seq_elements = input().split()
command = input()
moves = 0

while command != "end":
    idx1, idx2 = sorted([int(x) for x in command.split()])
    moves += 1
    if idx1 == idx2 or idx1 not in range(len(seq_elements)) \
            or idx2 not in range(len(seq_elements)):
        insert_idx = int(len(seq_elements) / 2)
        seq_elements.insert(insert_idx, f"-{moves}a")
        seq_elements.insert(insert_idx, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif seq_elements[idx1] == seq_elements[idx2]:
        element_removed = seq_elements[idx1]
        del seq_elements[idx2]
        del seq_elements[idx1]
        print(f"Congrats! You have found matching elements - {element_removed}!")
    elif seq_elements[idx1] != seq_elements[idx2]:
        print("Try again!")
    if not seq_elements:
        print(f"You have won in {moves} turns!")
        break
    command = input()
else:
    print("Sorry you lose :(")
    print(*seq_elements)
