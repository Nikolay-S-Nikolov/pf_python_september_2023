judge_dict = {}
input_line = input()
users = []
while input_line != "no more time":
    username, contest, points = input_line.split(" -> ")
    if username not in users:
        users.append(username)
    points = int(points)
    if contest not in judge_dict.keys():
        judge_dict[contest] = {username: points}
    else:
        if username in judge_dict[contest].keys():
            if judge_dict[contest][username] < points:
                judge_dict[contest][username] = points
        else:
            judge_dict[contest][username] = points
    input_line = input()

for contest_name, username_points in judge_dict.items():
    print(f"{contest_name}: {len(username_points)} participants")
    count = 0
    username_points = {k: v for k, v in sorted(username_points.items(), key=lambda x: (-x[1], x[0]))}
    for user, user_points in username_points.items():
        count += 1
        print(f"{count}. {user} <::> {user_points}")
individual_dict = {}
for name in users:
    total_points = 0
    for contest_name, username_points in judge_dict.items():
        for user, user_points in username_points.items():
            if name == user:
                total_points += user_points
    individual_dict[name] = total_points
individual_dict = {k: v for k, v in sorted(individual_dict.items(), key=lambda x: (-x[1], x[0]))}
print("Individual standings:")
num = 0
for n, p in individual_dict.items():
    num += 1
    print(f"{num}. {n} -> {p}")
