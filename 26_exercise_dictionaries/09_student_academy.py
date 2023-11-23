students_grade = {}
pair_of_rows = int(input())

for _ in range(pair_of_rows):
    student_name = input()
    grade = float(input())
    if student_name not in students_grade.keys():
        students_grade[student_name] = []
    students_grade[student_name].append(grade)

for name, grades in students_grade.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
