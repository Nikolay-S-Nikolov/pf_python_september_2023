keys = ["name", "age", "major"]
values = ["Ivan", 33, 'Computer Science']

student = {}

for i in range(len(keys)):
    key = keys[i]
    value = values[i]
    student[key] = value
print(student)
