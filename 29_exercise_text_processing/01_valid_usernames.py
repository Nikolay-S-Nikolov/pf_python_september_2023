usernames = input().split(', ')

for user in usernames:
    for ch in user:
        if not (ch.isalnum() or ch == "_" or ch == '-'):
            break
    else:
        if len(user) in range(3, 17):
            if ' ' not in user:
                print(user)

