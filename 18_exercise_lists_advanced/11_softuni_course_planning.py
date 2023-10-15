def add_lesson(title: str, schedule_list: list) -> list:
    if title not in schedule_list:
        schedule_list.append(title)
    return schedule_list


def insert_lesson(title: str, index: str, schedule_list: list) -> list:
    if title not in schedule_list:
        schedule_list.insert(int(index), title)
    return schedule_list


def remove_lesson(title: str, schedule_list: list) -> list:
    if title in schedule_list:
        index = schedule_list.index(title)
        if index + 1 in range(len(schedule_list)):
            if "Exercise" in schedule_list[index + 1]:
                schedule_list.remove(schedule_list[index + 1])
        schedule_list.remove(title)
    return schedule_list


def swap_lesson(first_title: str, second_title: str, schedule_list: list) -> list:
    if first_title in schedule_list and second_title in schedule_list:
        first_title_index = schedule_list.index(first_title)
        second_title_index = schedule_list.index(second_title)
        schedule_list[first_title_index], schedule_list[second_title_index] = \
            schedule_list[second_title_index], schedule_list[first_title_index]
        if first_title_index + 1 in range(len(schedule_list)) \
                and second_title_index + 1 in range(len(schedule_list)) \
                and "Exercise" in schedule_list[first_title_index + 1] \
                and "Exercise" in schedule_list[second_title_index + 1]:
            schedule_list[first_title_index + 1], schedule_list[second_title_index + 1] = \
                schedule_list[second_title_index + 1], schedule_list[first_title_index + 1]
        elif first_title_index + 1 in range(len(schedule_list)) \
                and "Exercise" in schedule_list[first_title_index + 1]:
            schedule_list.insert(second_title_index + 1, schedule_list.pop(first_title_index + 1))
        elif second_title_index + 1 in range(len(schedule_list)) \
                and "Exercise" in schedule_list[second_title_index + 1]:
            schedule_list.insert(first_title_index + 1, schedule_list.pop(second_title_index + 1))
    return schedule_list


def exercise_lesson(title: str, schedule_list: list) -> list:
    if title not in schedule_list:
        schedule_list.append(title)
        schedule_list.append(f"{title}-Exercise")
    else:
        index = schedule_list.index(title)
        if index + 1 in range(len(schedule_list)):
            if "Exercise" not in schedule_list[index + 1]:
                schedule_list.insert(index + 1, f"{title}-Exercise")
        else:
            schedule_list.append(f"{title}-Exercise")

    return schedule_list


def course_planing(course_schedule: list, command: str) -> list:
    while not command == "course start":
        command_list = command.split(':')
        if len(command_list) == 2:
            action, lesson_title = command_list
            if action == "Add":
                add_lesson(lesson_title, course_schedule)
            elif action == "Remove":
                remove_lesson(lesson_title, course_schedule)
            elif action == "Exercise":
                exercise_lesson(lesson_title, course_schedule)
        else:
            action, lesson_title, index_or_lesson = command_list
            if action == "Insert":
                insert_lesson(lesson_title, index_or_lesson, course_schedule)
            elif action == "Swap":
                swap_lesson(lesson_title, index_or_lesson, course_schedule)
        command = input()
    return course_schedule


schedule = input().split(", ")
command_to_check = input()
final_schedule = course_planing(schedule, command_to_check)
for titles in final_schedule:
    print(f'{final_schedule.index(titles) + 1}.{titles}')
