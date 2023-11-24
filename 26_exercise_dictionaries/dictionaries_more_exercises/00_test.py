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
# #     program_exit = input("To exit print 'y':")
# #     if program_exit == "y":
# #         break
# # print(student_info)
# my_dict1 = {'Peter': [{'Adc': 400}], 'George': [{'Jungle': 300}], 'Simon': [{'Mid': 200}, {'Support': 250}]}
# # for name, skills in my_dict1.items():
# #     print(name)
# #     for skill in skills:
# #         for k, v in skill.items():
# #             print(f"{k} -> {v}")
# result = [k for k in my_dict1['Simon'] if 'Support' in k.keys()]
# print(result)

dwarf_data = [{'dwarf_name': 'Peter', 'dwarf_hat_color': 'Red', 'dwarf_physics': 2000},
              {'dwarf_name': 'Teodor', 'dwarf_hat_color': 'Blue', 'dwarf_physics': 1000},
              {'dwarf_name': 'George', 'dwarf_hat_color': 'Green', 'dwarf_physics': 1000},
              {'dwarf_name': 'Simon', 'dwarf_hat_color': 'Blue', 'dwarf_physics': 4500},
              {'dwarf_name': 'Dopey', 'dwarf_hat_color': 'Simon', 'dwarf_physics': 1000}]
dwarf_new_name = "Peter"
dwarf_new_hat = "Red"
dwarf_new_physics = 3000
for items in dwarf_data:
    if items["dwarf_name"] == dwarf_new_name \
            and items["dwarf_hat_color"] == dwarf_new_hat \
            and items["dwarf_physics"] < dwarf_new_physics:
        del dwarf_data.index[items]
# dwarf_data.append({"dwarf_name": dwarf_new_name, "dwarf_hat_color": dwarf_new_hat, "dwarf_physics": dwarf_new_physics})
color_list = [y['dwarf_hat_color'] for y in dwarf_data]
# color_list = [a for a in sorted(color_list, key=lambda b: color_list.count(b))]
print(color_list)
dwarf_data = [x for x in
              sorted(dwarf_data, key=lambda z: (-z["dwarf_physics"], color_list.count(z['dwarf_hat_color'])))]
print(dwarf_data)
# dwarf_new_name = "George"
# dwarf_new_hat = "Green"
# dwarf_new_physics = 2000
# for items in my_list:
#     if items["dwarf_name"] == dwarf_new_name \
#             and items["dwarf_hat_color"] == dwarf_new_hat \
#             and items["dwarf_physics"] < dwarf_new_physics:
#         items["dwarf_physics"] = dwarf_new_physics
# print(my_list)
