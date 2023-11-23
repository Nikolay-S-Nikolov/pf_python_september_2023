stud_data = []
while True:
    Name = input("Enter the student name :")
    Age = input("Enter the age :")
    Gender = input("Enter the {} grade :")
    repeat = input("Do you want to add input more?: ")
    stud_data.append({
        "Name": Name,
        "Age": Age,
        "Gender": Gender
    })
    if repeat == "no" or repeat == "NO":
        break

print(stud_data)