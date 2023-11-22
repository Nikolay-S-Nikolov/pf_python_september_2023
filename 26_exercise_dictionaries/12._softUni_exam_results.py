command = input()
username_dict = {}
submissions_dict = {}

while command != "exam finished":
    command_as_list = command.split("-")
    if command_as_list[1] == "banned":
        username = command_as_list[0]
        if username in username_dict.keys():
            del username_dict[username]
    else:
        username, language, points = command_as_list
        points = int(points)
        if language not in submissions_dict.keys():
            submissions_dict[language] = 0
        submissions_dict[language] += 1
        if username in username_dict.keys():
            if username_dict[username] < points:
                username_dict[username] = points
        else:
            username_dict[username] = points
    command = input()
print("Results:")
for user, user_points in username_dict.items():
    print(f"{user} | {user_points}")
print("Submissions:")
for user_language, submissions_count in submissions_dict.items():
    print(f"{user_language} - {submissions_count}")
