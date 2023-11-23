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

some_dict = {"abb": 1, "aaa": 1, "bbc": 2, "bvd": 2, "dfasdf": 43, "asdw": 22, "alds": 12}
some_dict = {k: v for k, v in sorted(some_dict.items(), key=lambda x: (-x[1], x[0]))}
print(some_dict)
