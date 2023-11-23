contest_data = {}
command_contest = input()

while command_contest != "end of contests":
    contest_name, contest_password = command_contest.split(":")
    contest_data[contest_name] = contest_password
    command_contest = input()

command_submission = input()
user_data_contest = {}
user_data_points = {}

while command_submission != "end of submissions":
    contest, password, username, points = command_submission.split("=>")
    points = int(points)
    if (contest, password) in contest_data.items():
        if username not in user_data_contest.keys():
            user_data_contest[username] = [contest]
            user_data_points[username] = [points]
        elif contest in user_data_contest[username]:
            idx = user_data_contest[username].index(contest)
            if user_data_points[username][idx] < points:
                user_data_points[username][idx] = points
        else:
            user_data_contest[username].append(contest)
            user_data_points[username].append(points)
    command_submission = input()
data_contest_sorted = {key: value for key, value in sorted(user_data_contest.items(), key=lambda x: x[0])}
data_points_sorted = {key: value for key, value in sorted(user_data_points.items(), key=lambda x: x[0])}
best_candidate_name = ""
best_candidate_points = 0
for name, points in data_points_sorted.items():
    if sum(points) > best_candidate_points:
        best_candidate_name = name
        best_candidate_points = sum(points)
print(f"Best candidate is {best_candidate_name} with total {best_candidate_points} points.")
candidate_name_dict = {}
for candidate_name, contest_n in data_contest_sorted.items():
    key = candidate_name
    value = {k: v for k, v in zip(data_contest_sorted[candidate_name], data_points_sorted[candidate_name])}
    value_sorted = {k: v for k, v in sorted(value.items(), key=lambda x: x[1], reverse=True)}
    candidate_name_dict[key] = value_sorted
print("Ranking:")
for user_name, contest_points in candidate_name_dict.items():
    print(user_name)
    for contest_print, points_print in contest_points.items():
        print(f"#  {contest_print} -> {points_print}")
