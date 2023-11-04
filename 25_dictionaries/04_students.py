students = []

while True:
    student_info = input()
    if ":" not in student_info:
        course_to_search = student_info
        break
    name, student_id, course = student_info.split(":")
    students.append({"name": name, "ID": student_id, "course": course})

for student in students:
    if course_to_search.startswith(student["course"][0:3]):
        # if course_to_search in student.values()
        print(f"{student['name']} - {student['ID']}")
