courses_info = {}
command = input()

while command != "end":
    course, name = command.split(" : ")
    if course not in courses_info.keys():
        courses_info[course] = []
    courses_info[course].append(name)
    command = input()

for course_name,registered_students in courses_info.items():
    print(f"{course_name}: {len(registered_students)}")
    for student_name in registered_students:
        print(f"-- {student_name}")
