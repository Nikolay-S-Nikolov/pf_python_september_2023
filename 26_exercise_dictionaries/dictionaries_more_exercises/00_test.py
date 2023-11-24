# stud_data = []
# while True:
#     Name = input("Enter the student name :")
#     Age = input("Enter the age :")
#     Gender = input("Enter the {} grade :")
#     repeat = input("Do you want to add input more?: ")
#     stud_data.append({
#         "Name": Name,
#         "Age": Age,
#         "Gender": Gender
#     })
#     if repeat == "no" or repeat == "NO":
#         break
#
# print(stud_data)

# some_dict = {"abb": 1, "aaa": 1, "bbc": 2, "bvd": 2, "dfasdf": 43, "asdw": 22, "alds": 12}
# some_dict = {k: v for k, v in sorted(some_dict.items(), key=lambda x: (-x[1], x[0]))}
# print(some_dict)


# student_info = []
#
# while True:
#     key = input("Enter student name:")
#     value = input("Enter student age:")
#     student_info.append({"Name": key, "Age": value})
#     program_exit = input("To exit print 'y':")
#     if program_exit == "y":
#         break
# print(student_info)
my_dict1 = {'Peter': [{'Adc': 400}], 'George': [{'Jungle': 300}], 'Simon': [{'Mid': 200}, {'Support': 250}]}
# for name, skills in my_dict1.items():
#     print(name)
#     for skill in skills:
#         for k, v in skill.items():
#             print(f"{k} -> {v}")
result = [k for k in my_dict1['Simon'] if 'Support' in k.keys()]
print(result)
