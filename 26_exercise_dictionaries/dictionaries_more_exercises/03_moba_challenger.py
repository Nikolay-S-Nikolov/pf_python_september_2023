command = input()
players_position = {}
player_skills = {}

while command != "Season end":
    if " -> " in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in players_position.keys():
            players_position[player] = [position]
            player_skills[player] = [skill]
        else:
            if position in players_position[player]:
                idx = players_position[player].index(position)
                if player_skills[player][idx] < skill:
                    player_skills[player][idx] = skill
            else:
                players_position[player].append(position)
                player_skills[player].append(skill)
    elif " vs " in command:
        player_1, player_2 = command.split(" vs ")
        # if player_1 in players_position.keys() and player_2 in players_position.keys():
        if (player_1 and player_2) in players_position.keys():
            total_points_1 = 0
            total_points_2 = 0
            for position_1 in players_position[player_1]:
                for position_2 in players_position[player_2]:
                    if position_1 == position_2:
                        idx1 = players_position[player_1].index(position_1)
                        idx2 = players_position[player_2].index(position_2)
                        total_points_1 += player_skills[player_1][idx1]
                        total_points_2 += player_skills[player_2][idx2]
            if total_points_1 > total_points_2:
                del players_position[player_2]
                del player_skills[player_2]
            elif total_points_1 < total_points_2:
                del players_position[player_1]
                del player_skills[player_1]
    command = input()
players_total_skill = {}
for k, v in player_skills.items():
    key = k
    value = sum(v)
    players_total_skill[key] = value
players_total_skill = {k: v for k, v in sorted(players_total_skill.items(), key=lambda x: (-x[1], x[0]))}
for a, b in players_total_skill.items():
    print(f"{a}: {b} skill")
    position_skill_dict = dict(zip(players_position[a], player_skills[a]))
    position_skill_dict = {k: v for k, v in sorted(position_skill_dict.items(), key=lambda x: (-x[1], x[0]))}
    for c, d in position_skill_dict.items():
        print(f"- {c} <::> {d}")
